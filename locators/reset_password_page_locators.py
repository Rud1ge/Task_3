from selenium.webdriver.common.by import By

PAGE_TITLE = (By.XPATH, ".//h2[contains(text(), 'Восстановление пароля')]")
PASSWORD_INPUT = (By.XPATH, ".//input[@name='Введите новый пароль']")
PASSWORD_VISIBILITY_TOGGLE = (
    By.XPATH,
    ".//input[@name='Введите новый пароль']"
    "/ancestor::div[contains(@class, 'input')]//div[contains(@class, 'icon')]",
)
