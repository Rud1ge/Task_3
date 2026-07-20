from selenium.webdriver.common.by import By

FEED_TITLE = (By.XPATH, ".//h1[contains(text(), 'Лента заказов')]")
TOTAL_DONE_COUNTER = (
    By.XPATH,
    ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p",
)
TODAY_DONE_COUNTER = (
    By.XPATH,
    ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p",
)
ORDER_MODAL = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")


def format_order_number(order_number):
    return f"{order_number:07d}"


def feed_order_link(order_number):
    number = format_order_number(order_number)
    return (
        By.XPATH,
        f".//a[contains(@href, '/feed/') and contains(., '#{number}')]",
    )


def in_progress_order(order_number):
    number = format_order_number(order_number)
    return (
        By.XPATH,
        f".//p[contains(text(), 'В работе')]/following-sibling::ul/li[contains(., '{number}')]",
    )
