
import pytest
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators, LoginPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
@pytest.mark.xfail(reason='negative test case')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_not_be_displayed()

@pytest.mark.need_review
@pytest.mark.xfail(reason='negative test case')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    basket_page = BasketPage(browser,ProductPageLocators.LINK )
    page.open()
    page.click_on_basket_button()
    basket_page.wait_for_load_basket()
    basket_page.message_of_empty_basket_should_be_presented()

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LoginPageLocators.LINK)
        page.open()
        page.register_new_user(page.random_char(7)+"@gmail.com", '1235fghjhds6sfsgFFGH')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLocators.LINK)
        page.open()
        page.success_message_should_not_be_displayed()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLocators.LINK)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.message_of_success_should_be_displayed()
        page.book_name_in_message_should_be_correct()
        page.message_of_basket_should_be_displayed()
        page.amount_of_basket_in_message_should_be_correct()


