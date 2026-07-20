import random
import string

import pytest
import requests

from driver_factory import DriverFactory
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
    browser = DriverFactory.getWebdriver(request.param)
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def reset_browser_state(driver):
    driver.get(BASE_URL)
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
    driver.get(BASE_URL)
    yield


@pytest.fixture
def user():
    email = f"{''.join(random.choices(string.ascii_lowercase, k=8))}@example.com"
    password = "".join(random.choices(string.ascii_lowercase, k=8))
    name = "".join(random.choices(string.ascii_lowercase, k=8))
    body = requests.post(
        REGISTER_ENDPOINT,
        json={"email": email, "password": password, "name": name},
    ).json()
    data = {
        "email": email,
        "password": password,
        "name": name,
        "accessToken": body["accessToken"],
    }
    yield data
    requests.delete(USER_ENDPOINT, headers={"Authorization": data["accessToken"]})


@pytest.fixture
def ingredients():
    items = requests.get(INGREDIENTS_ENDPOINT).json()["data"]
    bun = None
    sauce = None
    for item in items:
        if bun is None and item["type"] == "bun":
            bun = item
        if sauce is None and item["type"] == "sauce":
            sauce = item
    return {
        "bun_name": bun["name"],
        "sauce_name": sauce["name"],
        "bun_id": bun["_id"],
        "sauce_id": sauce["_id"],
    }


@pytest.fixture
def create_order(user, ingredients):
    def _create_order():
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

    return _create_order


@pytest.fixture
def order(create_order):
    return create_order()


@pytest.fixture
def authorized_user(driver, user):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user["email"], user["password"])
    return user
