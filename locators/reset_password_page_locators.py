from selenium.webdriver.common.by import By

PASSWORD_VISIBILITY_TOGGLE = (
    By.XPATH,
    ".//input[@name='Введите новый пароль']" "/ancestor::div[contains(@class, 'input')]//div[contains(@class, 'icon')]",
)
PASSWORD_FIELD_FOCUSED = (
    By.XPATH,
    ".//input[@name='Введите новый пароль']"
    "/ancestor::div[contains(@class, 'input')]"
    "//label[contains(@class, 'input__placeholder-focused')]",
)
