from selenium.webdriver.common.by import By

MODAL_OPENED = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")
MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'modal__close')]")
ORDER_SUCCESS_MODAL = (
    By.XPATH,
    ".//h2[contains(text(), 'идентификатор заказа')]/ancestor::section[contains(@class, 'Modal')]",
)
ORDER_NUMBER_TEXT = (By.XPATH, ".//h2[contains(@class, 'digits')]")
