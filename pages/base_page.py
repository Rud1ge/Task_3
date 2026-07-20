import allure
from selenium.common.exceptions import TimeoutException
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

    def wait_for_loading_finished(self, title_locator, timeout=5):
        # В Firefox спиннер иногда зависает — refresh снимает оверлей.
        try:
            self.wait_until_invisible(modal_locators.LOADING_OVERLAY, timeout)
        except TimeoutException:
            self.driver.refresh()
            self.wait_for_visibility(title_locator)

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
        # HTML5 DnD: ActionChains работает в Chrome, в Firefox — нет (geckodriver).
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = {
                data: {},
                setData(key, value) { this.data[key] = value; },
                getData(key) { return this.data[key]; },
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
