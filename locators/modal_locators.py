from selenium.webdriver.common.by import By

MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'modal__close')]")
LOADING_OVERLAY = (
    By.XPATH,
    ".//*[contains(@class, 'Modal_modal__loading')]"
    "/ancestor::*[contains(@class, 'Modal_modal')]"
    "//div[contains(@class, 'Modal_modal_overlay')]",
)
ORDER_NUMBER_READY = (
    By.XPATH,
    ".//h2[contains(@class, 'digits') and string-length(normalize-space()) >= 5]",
)
