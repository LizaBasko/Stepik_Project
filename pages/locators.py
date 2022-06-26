from datetime import time as t

from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_LINK = "#login_link"
    BASKET_BUTTON = '.basket-mini .btn'
    BASKET_PAGE = '#default'
    BASKET_MESSAGE = '#content_inner p'

class LoginPageLocators():
    LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = '#login_form'
    REGISTER_FORM = '#register_form'
    REGISTER_EMAIL = '#id_registration-email'
    REGISTER_PASSWORD = '#id_registration-password1'
    REGISTER_PASSWORD_CONFIRM = '#id_registration-password2'
    REGISTER_BUTTON = '#register_form  button'

class ProductPageLocators():
    LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    SUBMIT_BUTTON = '#add_to_basket_form button'
    MESSAGE_OF_SUCCESS = '#messages .alert:nth-child(1)'
    TEXT_OF_MESSAGE_OF_SUCCESS = '#messages .alert:nth-child(1) strong'
    MESSAGE_OF_TOTAL_AMOUNT_BASKET = '#messages .alert:nth-child(3)'
    TEXT_OF_MESSAGE_OF_TOTAL_AMOUNT_BASKET = '#messages .alert:nth-child(3) strong'
    PRODUCT_NAME = '.product_main h1'
    PRODUCT_PRICE = '.product_main .price_color'

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")