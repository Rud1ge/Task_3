import re

import allure

from locators import account_page_locators
from pages.base_page import BasePage
from urls import ACCOUNT_ORDERS_URL, ACCOUNT_URL


class AccountPage(BasePage):
    @allure.step("Переходим в историю заказов")
    def go_to_order_history(self):
        self.click(account_page_locators.ORDER_HISTORY_LINK)
        self.wait_for_url_contains("/account/orders")

    @allure.step("Выходим из аккаунта")
    def logout(self):
        self.click(account_page_locators.LOGOUT_BUTTON)
        self.wait_for_url_contains("/login")

    def is_order_in_history(self, order_number):
        return bool(self.find_elements(account_page_locators.order_number_in_history(order_number)))
