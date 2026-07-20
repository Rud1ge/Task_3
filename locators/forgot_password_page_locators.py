from selenium.webdriver.common.by import By

PAGE_TITLE = (By.XPATH, ".//h2[contains(text(), 'Восстановление пароля')]")
EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
RESTORE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
