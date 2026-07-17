import allure

from locators import forgot_password_page_locators
from pages.base_page import BasePage
from urls import FORGOT_PASSWORD_URL


class ForgotPasswordPage(BasePage):
    @allure.step("Открываем страницу восстановления пароля")
    def open(self):
        self.driver.get(FORGOT_PASSWORD_URL)
        self.wait_for_visibility(forgot_password_page_locators.PAGE_TITLE)

    @allure.step("Вводим email: {email}")
    def enter_email(self, email):
        self.send_keys(forgot_password_page_locators.EMAIL_INPUT, email)

    @allure.step("Нажимаем кнопку «Восстановить»")
    def click_restore(self):
        self.click(forgot_password_page_locators.RESTORE_BUTTON)
        self.wait_for_url_contains("/reset-password")

    def is_reset_page_open(self):
        return "/reset-password" in self.driver.current_url
