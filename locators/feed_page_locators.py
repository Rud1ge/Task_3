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


def feed_order_link(order_number):
    return (
        By.XPATH,
        f".//a[contains(@href, '/feed/') and contains(., '#{order_number:07d}')]",
    )


def in_progress_order(order_number):
    return (
        By.XPATH,
        ".//p[contains(text(), 'В работе')]/following-sibling::ul" f"/li[contains(., '{order_number:07d}')]",
    )
