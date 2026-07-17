import allure

from data import INGREDIENT_BUN, INGREDIENT_FILLING
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from urls import BASE_URL, CONSTRUCTOR_URL, FEED_URL


@allure.link(BASE_URL, name="Stellar Burgers")
class TestMainFunctionality:
    @allure.title("Переход в конструктор")
    @allure.description("По клику «Конструктор» открывается главная страница.")
    def test_navigate_to_constructor(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.go_to_constructor()

        assert CONSTRUCTOR_URL in driver.current_url

    @allure.title("Переход в ленту заказов")
    @allure.description("По клику «Лента заказов» открывается страница /feed.")
    def test_navigate_to_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_feed()

        assert FEED_URL in driver.current_url

    @allure.title("Открытие модалки ингредиента")
    @allure.description("При клике на ингредиент появляется всплывающее окно с деталями.")
    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient(INGREDIENT_BUN)

        assert main_page.is_ingredient_modal_visible()

    @allure.title("Закрытие модалки ингредиента")
    @allure.description("Модалка закрывается по клику на крестик.")
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient(INGREDIENT_BUN)
        main_page.close_modal()

        assert main_page.is_modal_closed()

    @allure.title("Увеличение счётчика ингредиента")
    @allure.description("При добавлении ингредиента в заказ его счётчик увеличивается.")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.open_sauces_tab()
        counter_before = main_page.get_ingredient_counter(INGREDIENT_FILLING)
        main_page.add_filling_to_order(INGREDIENT_FILLING)

        assert main_page.get_ingredient_counter(INGREDIENT_FILLING) == counter_before + 1

    @allure.title("Оформление заказа авторизованным пользователем")
    @allure.description("Залогиненный пользователь может оформить заказ из конструктора.")
    def test_logged_in_user_can_place_order(self, driver, user):
        main_page = MainPage(driver)
        main_page.open()
        main_page.authorize_by_token(user["accessToken"])
        main_page.build_default_burger(INGREDIENT_BUN, INGREDIENT_FILLING)
        main_page.click_place_order()

        assert main_page.is_order_success_modal_visible()
