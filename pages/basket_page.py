from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait

class BasketPage(BasePage):
    def wait_for_load_basket(self):
        basket_content = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, MainPageLocators.BASKET_PAGE)))

    def message_of_empty_basket_should_be_presented(self):
        message = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, MainPageLocators.BASKET_MESSAGE))).text
        assert 'Your basket is empty.' in message, 'Message is not correct'