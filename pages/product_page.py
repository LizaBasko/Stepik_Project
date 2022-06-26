from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ProductPageLocators.SUBMIT_BUTTON)))
        button.click()

    def message_of_success_should_be_displayed(self):
        message = self.is_element_present(By.CSS_SELECTOR, ProductPageLocators.MESSAGE_OF_SUCCESS)
        assert message is True, 'Message of success is not displayed on page'

    def message_of_basket_should_be_displayed(self):
        message = self.is_element_present(By.CSS_SELECTOR, ProductPageLocators.MESSAGE_OF_TOTAL_AMOUNT_BASKET)
        assert message is True, 'Message of total amount in basket is not displayed on page'

    def book_name_in_message_should_be_correct(self):
        name_in_message = self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.TEXT_OF_MESSAGE_OF_SUCCESS).text
        book_name = self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.PRODUCT_NAME).text
        assert name_in_message == book_name, f'Name of book in message is({name_in_message}) not the same as the name of added book({book_name})'

    def amount_of_basket_in_message_should_be_correct(self):
        amount_in_message = self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.TEXT_OF_MESSAGE_OF_TOTAL_AMOUNT_BASKET).text
        book_price = self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.PRODUCT_PRICE).text
        assert amount_in_message == book_price, f'Total amount in message({amount_in_message}) is not the same as book price({book_price})'

    def success_message_should_not_be_displayed(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, ProductPageLocators.MESSAGE_OF_SUCCESS)

    def basket_message_should_not_be_displayed(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, ProductPageLocators.MESSAGE_OF_TOTAL_AMOUNT_BASKET)

    def success_message_should_disappear(self):
        assert self.is_disappeared(By.CSS_SELECTOR, ProductPageLocators.MESSAGE_OF_SUCCESS)