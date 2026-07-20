from selenium.webdriver.common.by import By

MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'modal__close')]")
ORDER_NUMBER_READY = (
    By.XPATH,
    ".//h2[contains(@class, 'digits') and string-length(normalize-space()) >= 5]",
)
