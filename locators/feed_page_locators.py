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
FEED_ORDER_LINKS = (By.XPATH, ".//a[contains(@href, '/feed/')]")
ORDER_MODAL = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")
IN_PROGRESS_ORDER_ITEMS = (By.CSS_SELECTOR, "ul[class*='OrderFeed_orderListReady'] li")


def feed_order_link(order_number):
    return (
        By.XPATH,
        f".//a[contains(@href, '/feed/') and contains(., '#{order_number:07d}')]",
    )
