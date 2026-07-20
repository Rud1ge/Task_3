import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from urls import BASE_URL, FORGOT_PASSWORD_URL


@allure.link(BASE_URL, name="Stellar Burgers")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    @allure.description("По кнопке «Восстановить пароль» открывается страница /forgot-password.")
    def test_navigate_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_forgot_password()

        assert FORGOT_PASSWORD_URL in driver.current_url

    @allure.title("Восстановление пароля по email")
    @allure.description("После ввода email и клика «Восстановить» открывается страница сброса пароля.")
    def test_restore_password_with_email(self, driver, user):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        forgot_password_page.enter_email(user["email"])
        forgot_password_page.click_restore()

        assert "/reset-password" in driver.current_url

    @allure.title("Переключатель видимости пароля подсвечивает поле")
    @allure.description("После восстановления пароля клик по иконке подсвечивает поле нового пароля.")
    def test_password_visibility_toggle_highlights_field(self, driver, user):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        forgot_password_page.enter_email(user["email"])
        forgot_password_page.click_restore()

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.click_password_visibility_toggle()

        assert reset_password_page.is_password_field_active()
