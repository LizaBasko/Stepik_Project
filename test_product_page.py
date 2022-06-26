import time
import pytest

from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from .pages.main_page import MainPage

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.parametrize('promo_code', [1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail),8, 9, 10])
def test_guest_can_add_product_to_basket(browser, promo_code):
    url = ('http://selenium1py.pythonanywhere.com/catalogue/'
           f'coders-at-work_207/?promo=offer{promo_code}')
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_of_success_should_be_displayed()
    page.book_name_in_message_should_be_correct()
    page.message_of_basket_should_be_displayed()
    page.amount_of_basket_in_message_should_be_correct()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    page.success_message_should_not_be_displayed()


@pytest.mark.xfail(reason='negative test case')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_not_be_displayed()

@pytest.mark.xfail(reason='negative test case')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    basket_page = BasketPage(browser,ProductPageLocators.LINK )
    page.open()
    page.click_on_basket_button()
    basket_page.wait_for_load_basket()
    basket_page.message_of_empty_basket_should_be_presented()

