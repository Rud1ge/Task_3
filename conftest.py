import random
import string

import allure
import pytest
import requests
from selenium import webdriver

from pages.login_page import LoginPage
from urls import (
    BASE_URL,
    INGREDIENTS_ENDPOINT,
    ORDERS_ENDPOINT,
    REGISTER_ENDPOINT,
    USER_ENDPOINT,
)


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def reset_browser_state(driver):
    driver.get(BASE_URL)
    driver.execute_script("localStorage.clear(); sessionStorage.clear();")
    driver.delete_all_cookies()
    yield


@pytest.fixture
def user():
    email = f"{''.join(random.choices(string.ascii_lowercase, k=10))}@example.com"
    password = "".join(random.choices(string.ascii_lowercase, k=10))
    name = "".join(random.choices(string.ascii_lowercase, k=10))
    body = requests.post(
        REGISTER_ENDPOINT,
        json={"email": email, "password": password, "name": name},
    ).json()
    data = {
        "email": email,
        "password": password,
        "name": name,
        "accessToken": body["accessToken"],
        "refreshToken": body["refreshToken"],
    }
    yield data
    requests.delete(USER_ENDPOINT, headers={"Authorization": data["accessToken"]})


@pytest.fixture
def ingredients():
    items = requests.get(INGREDIENTS_ENDPOINT).json()["data"]
    bun = next(item for item in items if item["type"] == "bun")
    sauce = next(item for item in items if item["type"] == "sauce")
    return {
        "bun_name": bun["name"],
        "sauce_name": sauce["name"],
        "bun_id": bun["_id"],
        "sauce_id": sauce["_id"],
    }


@pytest.fixture
def order(user, ingredients):
    return requests.post(
        ORDERS_ENDPOINT,
        json={
            "ingredients": [
                ingredients["bun_id"],
                ingredients["sauce_id"],
                ingredients["bun_id"],
            ]
        },
        headers={"Authorization": user["accessToken"]},
    ).json()


@pytest.fixture
def authorized_user(driver, user):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user["email"], user["password"])
    return user
