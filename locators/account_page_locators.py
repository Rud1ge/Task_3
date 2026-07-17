from selenium.webdriver.common.by import By

ORDER_HISTORY_LINK = (By.XPATH, ".//a[contains(@href, '/account/order-history')]")
LOGOUT_BUTTON = (By.XPATH, ".//button[contains(., 'Выход')]")


def order_number_in_history(order_number):
    formatted_number = f"{order_number:07d}"
    return (By.XPATH, f".//*[contains(text(), '#{formatted_number}')]")
