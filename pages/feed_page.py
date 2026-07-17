import re

import allure
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
        return int(
            re.sub(r"\D", "", self.get_text(feed_page_locators.TOTAL_DONE_COUNTER))
        )

    @allure.step("Получаем значение «Выполнено за сегодня»")
    def get_today_done_count(self):
        return int(
            re.sub(r"\D", "", self.get_text(feed_page_locators.TODAY_DONE_COUNTER))
        )

    @allure.step("Проверяем, что заказ #{order_number} в работе")
    def is_order_in_progress(self, order_number):
        number = f"{order_number:07d}"
        return any(
            number in item.text
            for item in self.find_elements(feed_page_locators.IN_PROGRESS_ORDER_ITEMS)
        )

    @allure.step("Ждём появления заказа #{order_number} в разделе «В работе»")
    def wait_until_order_in_progress(self, order_number, timeout=20):
        WebDriverWait(self.driver, timeout, poll_frequency=0.3).until(
            lambda _: self.is_order_in_progress(order_number)
        )

    @allure.step("Получаем номера заказов из ленты")
    def get_order_numbers_from_feed(self):
        numbers = []
        for link in self.find_elements(feed_page_locators.FEED_ORDER_LINKS):
            match = re.search(r"#(\d+)", link.text)
            if match:
                numbers.append(int(match.group(1)))
        return numbers

    @allure.step("Проверяем, что модалка заказа открыта")
    def is_order_modal_visible(self):
        return self.is_displayed(feed_page_locators.ORDER_MODAL)

    @allure.step("Ждём увеличения счётчика")
    def wait_for_counter_increase(self, getter, previous_value, timeout=20):
        def counter_increased(_driver):
            self.driver.refresh()
            self.wait_for_visibility(feed_page_locators.FEED_TITLE)
            return getter() > previous_value

        WebDriverWait(self.driver, timeout, poll_frequency=1).until(counter_increased)
