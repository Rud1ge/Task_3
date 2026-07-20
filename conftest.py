import pytest

from driver_factory import DriverFactory
from helpers import (
    clear_browser_session,
    create_order,
    delete_user,
    get_ingredients,
    register_user,
)
from pages.login_page import LoginPage
from urls import BASE_URL


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver(request):
    browser = DriverFactory.getWebdriver(request.param)
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
