import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        password = '54321ytrewq'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product = ProductPage(browser, link)
        product.open()
        product.add_to_basket()
        product.should_be_added_product()

    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
        product = ProductPage(browser, link)
        product.open()
        product.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('number',
                         [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    product = ProductPage(browser, link)
    product.open()
    product.add_to_basket()
    product.solve_quiz_and_get_code()
    product.should_be_added_product()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    product = ProductPage(browser, link)
    product.open()
    product.add_to_basket()
    product.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    product = ProductPage(browser, link)
    product.open()
    product.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    product = ProductPage(browser, link)
    product.open()
    product.add_to_basket()
    product.should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_message()
