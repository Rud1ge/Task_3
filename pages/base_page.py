import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import header_locators, modal_locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_url_contains(self, url_part, timeout=3):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.url_contains(url_part))

    def wait_until_invisible(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def click(self, locator, timeout=10):
        self.wait_until_invisible(modal_locators.LOADING_OVERLAY, timeout)
        self.wait_for_clickable(locator, timeout).click()

    def send_keys(self, locator, text, timeout=3):
        element = self.wait_for_visibility(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=3):
        return self.wait_for_visibility(locator, timeout).text

    def drag_and_drop(self, source_locator, target_locator, timeout=3):
        source = self.wait_for_visibility(source_locator, timeout)
        target = self.wait_for_visibility(target_locator, timeout)
        # move_to_element: без него элемент вне viewport не попадает в корзину
        ActionChains(self.driver).move_to_element(source).drag_and_drop(source, target).perform()

    @allure.step("Переходим в конструктор")
    def go_to_constructor(self):
        self.click(header_locators.CONSTRUCTOR_LINK)

    @allure.step("Переходим в ленту заказов")
    def go_to_feed(self):
        self.click(header_locators.FEED_LINK)

    @allure.step("Переходим в личный кабинет")
    def go_to_personal_account(self):
        self.click(header_locators.PERSONAL_ACCOUNT_LINK)
        self.wait_for_url_contains("/account")
