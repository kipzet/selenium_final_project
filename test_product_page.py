import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


# @pytest.mark.parametrize('number',
#                          [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)])
# def test_guest_can_add_product_to_basket(browser, number):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
#     product = ProductPage(browser, link)
#     product.open()
#     product.add_to_basket()
#     product.solve_quiz_and_get_code()
#     product.should_be_added_product()

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
#     product = ProductPage(browser, link)
#     product.open()
#     product.add_to_basket()
#     product.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
#     product = ProductPage(browser, link)
#     product.open()
#     product.should_not_be_success_message()
#
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
#     product = ProductPage(browser, link)
#     product.open()
#     product.add_to_basket()
#     product.should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()



