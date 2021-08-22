from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_button.click()

    def should_be_added_product(self):
        self.should_be_added_message()
        self.should_be_equal_price()

    def should_be_added_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), "Product title is not displayed"
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_TITLE), "Added product title is not displayed"
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        added_product = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_TITLE)
        assert product.text == added_product.text, 'Products is not equal'

    def should_be_equal_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not displayed"
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_PRICE), "Added product price is not displayed"
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        assert price.text == added_price.text, 'Prices is not equal'
