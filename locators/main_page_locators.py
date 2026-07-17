from selenium.webdriver.common.by import By

CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")
BUN_TAB = (By.XPATH, ".//span[text()='Булки']/parent::div")
SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::div")
FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::div")
CONSTRUCTOR_TOP_DROP_ZONE = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
CONSTRUCTOR_BOTTOM_DROP_ZONE = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_bottom')]")
CONSTRUCTOR_BASKET = (By.XPATH, ".//div[contains(@class, 'BurgerConstructor_basket__container')]")
PLACE_ORDER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")
INGREDIENT_MODAL = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")


def ingredient_link_by_name(name):
    return (By.XPATH, f".//a[contains(@href, '/ingredient/') and .//p[contains(text(), '{name}')]]")


def ingredient_counter_by_name(name):
    return (
        By.XPATH,
        f".//a[contains(@href, '/ingredient/') and .//p[contains(text(), '{name}')]]"
        f"//div[contains(@class, 'counter')]",
    )
