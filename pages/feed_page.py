import allure

from locators import feed_page_locators
from pages.base_page import BasePage
from urls import FEED_URL


class FeedPage(BasePage):
    @allure.step("Открываем ленту заказов")
    def open(self):
        self.driver.get(FEED_URL)
        self.wait_for_visibility(feed_page_locators.FEED_TITLE)

    @allure.step("Открываем заказ #{order_number} в ленте")
    def click_order(self, order_number):
        self.click(feed_page_locators.feed_order_link(order_number))

    @allure.step("Получаем значение «Выполнено за всё время»")
    def get_total_done_count(self):
        return int(self.get_text(feed_page_locators.TOTAL_DONE_COUNTER))

    @allure.step("Получаем значение «Выполнено за сегодня»")
    def get_today_done_count(self):
        return int(self.get_text(feed_page_locators.TODAY_DONE_COUNTER))

    @allure.step("Проверяем, что заказ #{order_number} в работе")
    def is_order_in_progress(self, order_number):
        self.wait_for_visibility(feed_page_locators.in_progress_order(order_number))
        return True

    @allure.step("Проверяем, что заказ #{order_number} есть в ленте")
    def is_order_in_feed(self, order_number):
        self.wait_for_visibility(feed_page_locators.feed_order_link(order_number))
        return True

    @allure.step("Проверяем, что модалка заказа открыта")
    def is_order_modal_visible(self):
        self.wait_for_visibility(feed_page_locators.ORDER_MODAL)
        return True

    @allure.step("Ждём увеличения счётчика «Выполнено за всё время»")
    def wait_until_total_done_increases(self, previous_value):
        for _ in range(20):
            self.driver.refresh()
            self.wait_for_visibility(feed_page_locators.FEED_TITLE)
            if self.get_total_done_count() > previous_value:
                return

    @allure.step("Ждём увеличения счётчика «Выполнено за сегодня»")
    def wait_until_today_done_increases(self, previous_value):
        for _ in range(20):
            self.driver.refresh()
            self.wait_for_visibility(feed_page_locators.FEED_TITLE)
            if self.get_today_done_count() > previous_value:
                return
