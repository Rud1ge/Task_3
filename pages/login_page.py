import allure

from locators import login_page_locators
from pages.base_page import BasePage
from urls import LOGIN_URL


class LoginPage(BasePage):
    @allure.step("Открываем страницу входа")
    def open(self):
        self.driver.get(LOGIN_URL)
        self.wait_for_visibility(login_page_locators.PAGE_TITLE)

    @allure.step("Переходим на страницу восстановления пароля")
    def click_forgot_password(self):
        self.click(login_page_locators.FORGOT_PASSWORD_LINK)

    @allure.step("Авторизуемся: email={email}")
    def login(self, email, password):
        self.send_keys(login_page_locators.EMAIL_INPUT, email)
        self.send_keys(login_page_locators.PASSWORD_INPUT, password)
        self.click(login_page_locators.LOGIN_BUTTON)
        self.wait_until_invisible(login_page_locators.PAGE_TITLE, timeout=10)
