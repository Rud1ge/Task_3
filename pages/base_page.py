import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import header_locators


class BasePage:
    DEFAULT_TIMEOUT = 5

    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def wait_for_url_contains(self, url_part):
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(expected_conditions.url_contains(url_part))

    def wait_until_invisible(self, locator):
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def send_keys(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visibility(locator).text

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_for_visibility(source_locator)
        target = self.wait_for_visibility(target_locator)
        # HTML5 DnD: ActionChains здесь не срабатывает
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
