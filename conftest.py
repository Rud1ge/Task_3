import allure
import pytest
from selenium.common.exceptions import JavascriptException

from helpers import WebDriverFactory, delete_user, register_new_user_and_return_data
from pages.base_page import BasePage
from urls import BASE_URL


@pytest.fixture(autouse=True)
def reset_browser_state(driver):
    driver.get(BASE_URL)
    try:
        driver.execute_script("localStorage.clear(); sessionStorage.clear();")
    except JavascriptException:
        pass
    driver.delete_all_cookies()
    yield
    BasePage(driver).close_modal_if_present()


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver(request):
    with allure.step(f"Открываем браузер {request.param}"):
        browser = WebDriverFactory.get_driver(request.param)
    yield browser
    with allure.step("Закрываем браузер"):
        browser.quit()


@pytest.fixture
def user():
    with allure.step("Создаём пользователя для теста"):
        user_data = register_new_user_and_return_data()
    yield user_data
    with allure.step("Удаляем пользователя после теста"):
        delete_user(user_data["accessToken"])
