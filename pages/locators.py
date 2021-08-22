from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    ADDED_PRODUCT_TITLE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
