import allure
from selenium.webdriver.common.by import By

from locators import reset_password_page_locators
from pages.base_page import BasePage
from urls import RESET_PASSWORD_URL


class ResetPasswordPage(BasePage):
    @allure.step("Открываем страницу сброса пароля")
    def open(self):
        self.driver.get(RESET_PASSWORD_URL)
        self.wait_for_visibility(reset_password_page_locators.PAGE_TITLE)

    @allure.step("Нажимаем кнопку показать/скрыть пароль")
    def click_password_visibility_toggle(self):
        self.wait_for_visibility(reset_password_page_locators.PASSWORD_INPUT)
        self.click(reset_password_page_locators.PASSWORD_VISIBILITY_TOGGLE)

    @allure.step("Проверяем, что поле пароля подсвечено")
    def is_password_field_active(self):
        password_input = self.wait_for_visibility(reset_password_page_locators.PASSWORD_INPUT)
        label = password_input.find_element(By.XPATH, "./ancestor::div[contains(@class, 'input')]//label")
        class_name = label.get_attribute("class") or ""
        return "input__placeholder-focused" in class_name
