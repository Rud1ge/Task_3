import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import header_locators


class BasePage:
    DEFAULT_TIMEOUT = 5

    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url

    def wait_for_presence(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def wait_for_visibility(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_url_contains(self, url_part, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.url_contains(url_part))

    def wait_until_invisible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_clickable(locator, timeout)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.close_modal_if_present()
            element = self.wait_for_clickable(locator, timeout)
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_visibility(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.wait_for_visibility(locator, timeout).text

    def is_displayed(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.wait_for_visibility(locator, timeout).is_displayed()

    def drag_and_drop(self, source_locator, target_locator, timeout=DEFAULT_TIMEOUT):
        source = self.wait_for_visibility(source_locator, timeout)
        target = self.wait_for_visibility(target_locator, timeout)
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = {
                data: {},
                setData(key, value) {
                    this.data[key] = value;
                },
                getData(key) {
                    return this.data[key];
                },
            };
            ["dragstart", "dragenter", "dragover", "drop", "dragend"].forEach((type, index) => {
                const element = index === 0 || index === 4 ? source : target;
                const event = new Event(type, { bubbles: true, cancelable: true });
                event.dataTransfer = dataTransfer;
                element.dispatchEvent(event);
            });
            """,
            source,
            target,
        )

    @allure.step("Закрываем модальное окно, если оно открыто")
    def close_modal_if_present(self):
        close_buttons = self.driver.find_elements(By.XPATH, ".//button[contains(@class, 'modal__close')]")
        for button in close_buttons:
            if button.is_displayed():
                button.click()
                return

    @allure.step("Переходим в конструктор")
    def go_to_constructor(self):
        self.click(header_locators.CONSTRUCTOR_LINK)

    @allure.step("Переходим в ленту заказов")
    def go_to_feed(self):
        self.click(header_locators.FEED_LINK)

    @allure.step("Переходим в личный кабинет")
    def go_to_personal_account(self):
        self.click(header_locators.PERSONAL_ACCOUNT_LINK)

    @allure.step("Авторизуем пользователя через localStorage")
    def authorize_by_token(self, access_token):
        self.driver.execute_script(
            'localStorage.setItem("accessToken", arguments[0]);',
            access_token,
        )
        self.driver.refresh()
        self.close_modal_if_present()
