import allure

from locators import main_page_locators, modal_locators
from pages.base_page import BasePage
from urls import CONSTRUCTOR_URL


class MainPage(BasePage):
    @allure.step("Открываем конструктор")
    def open(self):
        self.driver.get(CONSTRUCTOR_URL)
        self.wait_for_visibility(main_page_locators.CONSTRUCTOR_TITLE)

    @allure.step("Открываем вкладку «Соусы»")
    def open_sauces_tab(self):
        self.click(main_page_locators.SAUCES_TAB)

    @allure.step("Открываем ингредиент: {name}")
    def click_ingredient(self, name):
        self.click(main_page_locators.ingredient_link_by_name(name))
        self.wait_for_visibility(main_page_locators.INGREDIENT_MODAL)

    @allure.step("Получаем счётчик ингредиента: {name}")
    def get_ingredient_counter(self, name):
        return int(self.wait_for_visibility(main_page_locators.ingredient_counter_by_name(name)).text)

    @allure.step("Добавляем булку в заказ: {name}")
    def add_bun_to_order(self, name):
        self.drag_and_drop(
            main_page_locators.ingredient_link_by_name(name),
            main_page_locators.CONSTRUCTOR_BASKET,
        )

    @allure.step("Добавляем соус в заказ: {name}")
    def add_sauce_to_order(self, name):
        self.drag_and_drop(
            main_page_locators.ingredient_link_by_name(name),
            main_page_locators.CONSTRUCTOR_BASKET,
        )

    @allure.step("Нажимаем «Оформить заказ»")
    def click_place_order(self):
        self.click(main_page_locators.PLACE_ORDER_BUTTON)

    @allure.step("Проверяем, что модалка ингредиента открыта")
    def is_ingredient_modal_visible(self):
        self.wait_for_visibility(main_page_locators.INGREDIENT_MODAL)
        return True

    @allure.step("Закрываем модалку")
    def close_modal(self):
        self.click(modal_locators.MODAL_CLOSE_BUTTON)
        self.wait_until_invisible(main_page_locators.INGREDIENT_MODAL)

    @allure.step("Проверяем, что модалка закрыта")
    def is_modal_closed(self):
        self.wait_until_invisible(main_page_locators.INGREDIENT_MODAL)
        return True

    @allure.step("Получаем номер оформленного заказа")
    def get_order_number_from_modal(self):
        return int(self.get_text(modal_locators.ORDER_NUMBER_READY))
