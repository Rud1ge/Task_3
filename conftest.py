import pytest
from selenium import webdriver

from helpers import (
    clear_browser_session,
    create_order,
    delete_user,
    get_ingredients,
    register_user,
)
from pages.login_page import LoginPage
from urls import BASE_URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    browser = None

    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        # snap /usr/bin/firefox — обёртка, Selenium нужен реальный binary
        options = webdriver.FirefoxOptions()
        options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"
        browser = webdriver.Firefox(options=options)
    else:
        raise ValueError("Can't create instance for this browser param")

    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def reset_browser_state(driver):
    driver.get(BASE_URL)
    clear_browser_session(driver)
    driver.get(BASE_URL)
    yield


@pytest.fixture
def user():
    data = register_user()
    yield data
    delete_user(data["accessToken"])


@pytest.fixture
def ingredients():
    return get_ingredients()


@pytest.fixture
def order(user, ingredients):
    return create_order(user, ingredients)


@pytest.fixture
def authorized_user(driver, user):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user["email"], user["password"])
    return user
