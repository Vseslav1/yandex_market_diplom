import allure

from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from locators.headers_locators import HeadersLocators


class LoginPage(BasePage, LoginLocators, HeadersLocators):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Asert open form login')
    def assert_open_form_login(self):
        self.assertions.assert_that_element_is_visible(self.LOGIN_FORM)

    @allure.step('Login input')
    def login_input(self, login):
        self.fill(self.LOGIN, login)

    @allure.step('Click login')
    def click_login(self):
        self.click(self.SING_IN)

    @allure.step('Password input')
    def password_input(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    @allure.step('Click password')
    def click_password(self):
        self.click(self.BUTTON_PASSWORD)

    @allure.step('Login by phone')
    def login_by_phone(self):
        self.click(self.LOGIN_BY_PHONE)
        self.fill(self.PHONE_INPUT, '447955017')

    @allure.step('Form login visible')
    def assert_form_phone_login(self):
        self.assertions.assert_that_element_is_visible(self.PHONE_PHORM)

    @allure.step('Click create id')
    def create_id(self):
        self.click(self.BUTTON_CREATE_ID)

    @allure.step('Click create id for me')
    def create_id_for_me(self):
        self.click_for_index(self.CREATE_ID, 0)

    @allure.step('Back button')
    def back_button(self):
        self.click(self.BACK)

    @allure.step('Click create id for child')
    def create_id_for_child(self):
        self.click_for_index(self.CREATE_ID, 1)

    @allure.step('Assert form create id for me visible')
    def assert_open_form_for_me(self):
        self.assertions.assert_that_element_is_visible(self.FORM_FOR_ME)

    @allure.step('Assert open form create id for child visible')
    def assert_open_form_for_child(self):
        self.assertions.assert_that_element_is_visible(self.FORM_FOR_CHILD)

    @allure.step('Assert login using other service clickable')
    def assert_login_using_other_service(self):
        self.assertions.assert_that_element_is_clickable(self.LOGIN_VK)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_GMAIL)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_QR)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_FACEBOOK)
        self.assertions.assert_that_element_is_clickable(self.BUTTON_MORE)

    @allure.step('Click button more')
    def button_more(self):
        self.click(self.BUTTON_MORE)

    @allure.step('assert login using other elements visible and clickable')
    def assert_login_using_other_elements_visible_and_clickable(self):
        self.assertions.assert_that_element_is_visible(self.LOGIN_MR)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_MR)
        self.assertions.assert_that_element_is_visible(self.LOGIN_OK)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_OK)
        self.assertions.assert_that_element_is_visible(self.LOGIN_X)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_X)

    @allure.step('Assert login entered incorrectly')
    def assert_login_entered_incorrect(self):
        self.assert_that_element_contains_text(self.TEXT_EROR_LOGIN,
                                        'Нет такого аккаунта. Проверьте логин или войдите по телефону')

    @allure.step('Assert login not entered')
    def assert_login_not_entered(self):
        self.assertions.assert_that_element_contains_text(self.TEXT_EROR_LOGIN, 'Логин не указан')

    @allure.step('Assert password entered incorrectly')
    def assert_entered_incorrect_password(self):
        self.get_element(self.TEXT_EROR_PASSWORD)
        self.assert_that_element_contains_text(self.TEXT_EROR_PASSWORD,
                                               'Неверный пароль')

    @allure.step('Assert forgot password')
    def assert_forgot_password(self):
        self.get_element(self.FORGOT_PASSWORD)
        self.assertions.assert_that_element_is_clickable(self.FORGOT_PASSWORD)

    @allure.step('Assert password not entered')
    def assert_password_not_entered(self):
        self.assertions.assert_that_element_contains_text(self.TEXT_EROR_PASSWORD, 'Пароль не указан')
