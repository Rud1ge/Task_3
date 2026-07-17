import allure

from data import INGREDIENT_BUN, INGREDIENT_FILLING
from helpers import create_order_via_api
from pages.account_page import AccountPage
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from urls import ACCOUNT_ORDERS_URL, BASE_URL


@allure.link(BASE_URL, name="Stellar Burgers")
class TestOrderFeed:
    @allure.title("Открытие модалки заказа из ленты")
    @allure.description("При клике на заказ в ленте открывается всплывающее окно с деталями.")
    def test_order_modal_opens_from_feed(self, driver, user):
        order_data = create_order_via_api(user["accessToken"])
        order_number = order_data["order"]["number"]

        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.click_order(order_number)

        assert feed_page.is_order_modal_visible()

    @allure.title("Заказы пользователя отображаются в ленте")
    @allure.description("Заказ из истории пользователя виден на странице «Лента заказов».")
    def test_user_orders_appear_in_feed(self, driver, user):
        order_data = create_order_via_api(user["accessToken"])
        order_number = order_data["order"]["number"]

        main_page = MainPage(driver)
        main_page.open()
        main_page.authorize_by_token(user["accessToken"], user["refreshToken"])
        driver.get(ACCOUNT_ORDERS_URL)

        account_page = AccountPage(driver)
        assert account_page.is_order_in_history(order_number)

        feed_page = FeedPage(driver)
        feed_page.open()

        assert order_number in feed_page.get_order_numbers_from_feed()

    @allure.title("Счётчик «Выполнено за всё время» увеличивается")
    @allure.description("После создания заказа общий счётчик выполненных заказов растёт.")
    def test_total_done_counter_increases(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open()
        total_before = feed_page.get_total_done_count()

        create_order_via_api(user["accessToken"])
        feed_page.open()
        feed_page.wait_for_counter_increase(feed_page.get_total_done_count, total_before)

        assert feed_page.get_total_done_count() > total_before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    @allure.description("После создания заказа дневной счётчик выполненных заказов растёт.")
    def test_today_done_counter_increases(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open()
        today_before = feed_page.get_today_done_count()

        create_order_via_api(user["accessToken"])
        feed_page.open()
        feed_page.wait_for_counter_increase(feed_page.get_today_done_count, today_before)

        assert feed_page.get_today_done_count() > today_before

    @allure.title("Новый заказ появляется в разделе «В работе»")
    @allure.description("После оформления заказа его номер отображается в блоке «В работе».")
    def test_new_order_appears_in_progress(self, driver, user):
        main_page = MainPage(driver)
        main_page.open()
        main_page.authorize_by_token(user["accessToken"], user["refreshToken"])
        main_page.build_default_burger(INGREDIENT_BUN, INGREDIENT_FILLING)
        main_page.click_place_order()
        order_number = main_page.get_order_number_from_modal()

        feed_page = FeedPage(driver)
        feed_page.open()

        assert feed_page.is_order_in_progress(order_number)
