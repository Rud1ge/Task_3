from selenium.webdriver.common.by import By

from locators.feed_page_locators import format_order_number

ORDER_HISTORY_LINK = (By.XPATH, ".//a[contains(@href, '/account/order-history')]")
LOGOUT_BUTTON = (By.XPATH, ".//button[contains(., 'Выход')]")


def order_number_in_history(order_number):
    number = format_order_number(order_number)
    return (By.XPATH, f".//*[contains(text(), '#{number}')]")
