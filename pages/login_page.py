from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == LoginPageLocators.LINK, 'Link is not login page link'

    def should_be_login_form(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPageLocators.LOGIN_FORM)))
        assert self.is_element_present(By.CSS_SELECTOR, LoginPageLocators.LOGIN_FORM) is True, 'Login form is not presented on Login page'

    def should_be_register_form(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPageLocators.REGISTER_FORM)))
        assert self.is_element_present(By.CSS_SELECTOR,
            LoginPageLocators.REGISTER_FORM) is True, 'REGISTER form is not presented on Login page'
