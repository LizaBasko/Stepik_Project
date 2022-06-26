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

    def register_new_user(self,email, password):
        email_field = self.browser.find_element(By.CSS_SELECTOR, LoginPageLocators.REGISTER_EMAIL)
        password_field = self.browser.find_element(By.CSS_SELECTOR, LoginPageLocators.REGISTER_PASSWORD)
        password_confirm = self.browser.find_element(By.CSS_SELECTOR, LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        button = self.browser.find_element(By.CSS_SELECTOR, LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm.send_keys(password)
        button.click()
