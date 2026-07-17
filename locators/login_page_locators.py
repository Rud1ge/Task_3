from selenium.webdriver.common.by import By

PAGE_TITLE = (By.XPATH, ".//h2[text()='Вход']")
EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[contains(@href, '/forgot-password')]")
REGISTER_LINK = (By.XPATH, ".//a[contains(@href, '/register')]")
