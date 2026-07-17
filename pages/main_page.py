import allure

from locators import main_page_locators, modal_locators
from pages.base_page import BasePage
from urls import CONSTRUCTOR_URL


class MainPage(BasePage):
    @allure.step("Открываем конструктор")
    def open(self):
        self.driver.get(CONSTRUCTOR_URL)
        self.close_modal_if_present()
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
        counter = self.wait_for_visibility(main_page_locators.ingredient_counter_by_name(name))
        return int(counter.text)

    @allure.step("Добавляем булку в заказ: {name}")
    def add_bun_to_order(self, name):
        self.drag_and_drop(
            main_page_locators.ingredient_link_by_name(name),
            main_page_locators.CONSTRUCTOR_BASKET,
        )

    @allure.step("Добавляем начинку или соус в заказ: {name}")
    def add_filling_to_order(self, name):
        if "Соус" in name:
            self.open_sauces_tab()
        self.drag_and_drop(
            main_page_locators.ingredient_link_by_name(name),
            main_page_locators.CONSTRUCTOR_BASKET,
        )

    @allure.step("Собираем бургер по умолчанию")
    def build_default_burger(self, bun_name, filling_name):
        self.add_bun_to_order(bun_name)
        self.add_filling_to_order(filling_name)
        self.wait_for_visibility(main_page_locators.PLACE_ORDER_BUTTON, timeout=10)

    @allure.step("Нажимаем «Оформить заказ»")
    def click_place_order(self):
        self.click(main_page_locators.PLACE_ORDER_BUTTON)

    @allure.step("Проверяем, что модалка ингредиента открыта")
    def is_ingredient_modal_visible(self):
        return self.is_displayed(main_page_locators.INGREDIENT_MODAL)

    @allure.step("Закрываем модалку")
    def close_modal(self):
        button = self.wait_for_clickable(modal_locators.MODAL_CLOSE_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)
        self.wait_until_invisible(main_page_locators.INGREDIENT_MODAL)

    @allure.step("Проверяем, что модалка закрыта")
    def is_modal_closed(self):
        return len(self.find_elements(main_page_locators.INGREDIENT_MODAL)) == 0

    @allure.step("Проверяем, что заказ оформлен")
    def is_order_success_modal_visible(self):
        return self.is_displayed(modal_locators.ORDER_SUCCESS_MODAL)

    @allure.step("Получаем номер оформленного заказа")
    def get_order_number_from_modal(self):
        heading = self.wait_for_visibility(modal_locators.ORDER_NUMBER_TEXT)
        return int(heading.text.strip())
