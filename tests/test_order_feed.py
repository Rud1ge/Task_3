import allure
import requests

from pages.account_page import AccountPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from urls import BASE_URL, ORDERS_ENDPOINT


@allure.link(BASE_URL, name="Stellar Burgers")
class TestOrderFeed:
    @allure.title("Открытие модалки заказа из ленты")
    @allure.description(
        "При клике на заказ в ленте открывается всплывающее окно с деталями."
    )
    def test_order_modal_opens_from_feed(self, driver, order):
        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.click_order(order["order"]["number"])

        assert feed_page.is_order_modal_visible()

    @allure.title("Заказы пользователя отображаются в ленте")
    @allure.description(
        "Заказ из истории пользователя виден на странице «Лента заказов»."
    )
    def test_user_orders_appear_in_feed(self, driver, authorized_user, order):
        order_number = order["order"]["number"]
        LoginPage(driver).go_to_personal_account()
        AccountPage(driver).go_to_order_history()

        assert AccountPage(driver).is_order_in_history(order_number)

        feed_page = FeedPage(driver)
        feed_page.open()

        assert order_number in feed_page.get_order_numbers_from_feed()

    @allure.title("Счётчик «Выполнено за всё время» увеличивается")
    @allure.description(
        "После создания заказа общий счётчик выполненных заказов растёт."
    )
    def test_total_done_counter_increases(self, driver, user, ingredients):
        feed_page = FeedPage(driver)
        feed_page.open()
        total_before = feed_page.get_total_done_count()

        requests.post(
            ORDERS_ENDPOINT,
            json={
                "ingredients": [
                    ingredients["bun_id"],
                    ingredients["sauce_id"],
                    ingredients["bun_id"],
                ]
            },
            headers={"Authorization": user["accessToken"]},
        )
        feed_page.open()
        feed_page.wait_for_counter_increase(
            feed_page.get_total_done_count, total_before
        )

        assert feed_page.get_total_done_count() > total_before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    @allure.description(
        "После создания заказа дневной счётчик выполненных заказов растёт."
    )
    def test_today_done_counter_increases(self, driver, user, ingredients):
        feed_page = FeedPage(driver)
        feed_page.open()
        today_before = feed_page.get_today_done_count()

        requests.post(
            ORDERS_ENDPOINT,
            json={
                "ingredients": [
                    ingredients["bun_id"],
                    ingredients["sauce_id"],
                    ingredients["bun_id"],
                ]
            },
            headers={"Authorization": user["accessToken"]},
        )
        feed_page.open()
        feed_page.wait_for_counter_increase(
            feed_page.get_today_done_count, today_before
        )

        assert feed_page.get_today_done_count() > today_before

    @allure.title("Новый заказ появляется в разделе «В работе»")
    @allure.description(
        "После оформления заказа его номер отображается в блоке «В работе»."
    )
    def test_new_order_appears_in_progress(self, driver, user, ingredients):
        feed_page = FeedPage(driver)
        feed_page.open()
        order_number = requests.post(
            ORDERS_ENDPOINT,
            json={
                "ingredients": [
                    ingredients["bun_id"],
                    ingredients["sauce_id"],
                    ingredients["bun_id"],
                ]
            },
            headers={"Authorization": user["accessToken"]},
        ).json()["order"]["number"]
        feed_page.wait_until_order_in_progress(order_number)

        assert feed_page.is_order_in_progress(order_number)
