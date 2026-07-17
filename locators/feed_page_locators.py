from selenium.webdriver.common.by import By

FEED_TITLE = (By.XPATH, ".//h1[contains(text(), 'Лента заказов')]")
TOTAL_DONE_COUNTER = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
TODAY_DONE_COUNTER = (By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
IN_PROGRESS_SECTION = (By.XPATH, ".//p[contains(text(), 'В работе')]")
FEED_ORDER_LINKS = (By.XPATH, ".//a[contains(@href, '/feed/')]")
ORDER_MODAL = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")


def feed_order_link(order_number):
    formatted_number = f"{order_number:07d}"
    return (
        By.XPATH,
        f".//a[contains(@href, '/feed/') and contains(., '#{formatted_number}')]",
    )


def order_in_progress(order_number):
    formatted_number = f"{order_number:07d}"
    return (
        By.XPATH,
        f".//p[contains(text(), 'В работе')]/following-sibling::*[contains(text(), '{formatted_number}')]",
    )
