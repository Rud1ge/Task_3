import allure

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from urls import ACCOUNT_ORDERS_URL, ACCOUNT_URL, BASE_URL, LOGIN_URL


@allure.link(BASE_URL, name="Stellar Burgers")
class TestPersonalAccount:
    @allure.title("Переход в личный кабинет")
    @allure.description(
        "После авторизации клик по «Личный кабинет» открывает /account."
    )
    def test_navigate_to_account(self, driver, authorized_user):
        LoginPage(driver).go_to_personal_account()

        assert ACCOUNT_URL in driver.current_url

    @allure.title("Переход в историю заказов")
    @allure.description("Из личного кабинета можно перейти в раздел «История заказов».")
    def test_navigate_to_order_history(self, driver, authorized_user):
        LoginPage(driver).go_to_personal_account()
        AccountPage(driver).go_to_order_history()

        assert ACCOUNT_ORDERS_URL in driver.current_url

    @allure.title("Выход из аккаунта")
    @allure.description("После выхода пользователь перенаправляется на страницу входа.")
    def test_logout(self, driver, authorized_user):
        LoginPage(driver).go_to_personal_account()
        AccountPage(driver).logout()

        assert LOGIN_URL in driver.current_url
