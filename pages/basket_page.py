from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_message(self):
        msg = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE)
        assert msg.text == 'Your basket is empty. Continue shopping'

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), 'The products are in the basket'

