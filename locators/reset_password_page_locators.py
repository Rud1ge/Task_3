from selenium.webdriver.common.by import By

PASSWORD_INPUT = (By.XPATH, ".//input[@name='Введите новый пароль']")
PASSWORD_VISIBILITY_TOGGLE = (
    By.XPATH,
    ".//input[@name='Введите новый пароль']" "/ancestor::div[contains(@class, 'input')]//div[contains(@class, 'icon')]",
)
PASSWORD_FIELD_LABEL = (
    By.XPATH,
    ".//input[@name='Введите новый пароль']" "/ancestor::div[contains(@class, 'input')]//label",
)
