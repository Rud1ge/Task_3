import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
        return (
            WebDriverWait(self.driver, 10)
            .until(
                expected_conditions.visibility_of_element_located(feed_page_locators.in_progress_order(order_number))
            )
            .is_displayed()
        )

    @allure.step("Проверяем, что заказ #{order_number} есть в ленте")
    def is_order_in_feed(self, order_number):
        return (
            WebDriverWait(self.driver, 10)
            .until(expected_conditions.visibility_of_element_located(feed_page_locators.feed_order_link(order_number)))
            .is_displayed()
        )

    @allure.step("Проверяем, что модалка заказа открыта")
    def is_order_modal_visible(self):
        return self.wait_for_visibility(feed_page_locators.ORDER_MODAL).is_displayed()
