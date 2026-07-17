from selenium.webdriver.common.by import By

CONSTRUCTOR_LINK = (By.XPATH, ".//a[normalize-space()='Конструктор']")
FEED_LINK = (By.XPATH, ".//a[contains(normalize-space(), 'Лента')]")
ACCOUNT_LINK = (By.XPATH, ".//a[contains(@href, '/account')]")
LOGIN_BUTTON = (By.XPATH, ".//a[contains(@href, '/login')]")
PERSONAL_ACCOUNT_LINK = (By.XPATH, ".//a[contains(normalize-space(), 'Личный')]")
