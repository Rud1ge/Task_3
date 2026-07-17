from selenium.common.exceptions import TimeoutException

import allure

from locators import account_page_locators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step("Переходим в историю заказов")
    def go_to_order_history(self):
        self.click(account_page_locators.ORDER_HISTORY_LINK)
        self.wait_for_url_contains("/account/order-history")

    @allure.step("Выходим из аккаунта")
    def logout(self):
        self.click(account_page_locators.LOGOUT_BUTTON)
        self.wait_for_url_contains("/login")

    def is_order_in_history(self, order_number, timeout=15):
        try:
            self.wait_for_visibility(
                account_page_locators.order_number_in_history(order_number),
                timeout=timeout,
            )
            return True
        except TimeoutException:
            return False
