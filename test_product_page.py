from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product = ProductPage(browser, link)
    product.open()
    product.add_to_basket()
    product.solve_quiz_and_get_code()
    product.should_be_added_product()


