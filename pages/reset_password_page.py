import allure

from locators import reset_password_page_locators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step("Нажимаем кнопку показать/скрыть пароль")
    def click_password_visibility_toggle(self):
        self.click(reset_password_page_locators.PASSWORD_VISIBILITY_TOGGLE)

    @allure.step("Проверяем, что поле пароля подсвечено")
    def is_password_field_active(self):
        label = self.wait_for_visibility(reset_password_page_locators.PASSWORD_FIELD_LABEL)
        return "input__placeholder-focused" in label.get_attribute("class")
