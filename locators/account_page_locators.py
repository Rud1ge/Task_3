from selenium.webdriver.common.by import By

ORDER_HISTORY_LINK = (By.XPATH, ".//a[contains(@href, '/account/orders')]")
LOGOUT_BUTTON = (By.XPATH, ".//button[contains(., 'Выход')]")
ORDER_HISTORY_LINKS = (By.XPATH, ".//a[contains(@href, '/account/orders/')]")


def order_number_in_history(order_number):
    formatted_number = f"{order_number:07d}"
    return (
        By.XPATH,
        f".//a[contains(@href, '/account/orders/') and contains(., '#{formatted_number}')]",
    )
