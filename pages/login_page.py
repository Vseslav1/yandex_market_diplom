from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from locators.headers_locators import HeadersLocators


class LoginPage(BasePage, LoginLocators, HeadersLocators):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_open_form_login(self):
        self.assertions.assert_that_element_is_visible(self.LOGIN_FORM)

    def login_input(self, login):
        self.fill(self.LOGIN, login)

    def click_login(self):
        self.click(self.SING_IN)

    def password_input(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    def click_password(self):
        self.click(self.BUTTON_PASSWORD)

    def login_by_phone(self):
        self.click(self.LOGIN_BY_PHONE)
        self.fill(self.PHONE_INPUT, '447955017')

    def assert_form_phone_login(self):
        self.assertions.assert_that_element_is_visible(self.PHONE_PHORM)

    def create_id(self):
        self.click(self.BUTTON_CREATE_ID)

    def create_id_for_me(self):
        self.click_for_index(self.CREATE_ID, 0)

    def back_button(self):
        self.click(self.BACK)

    def create_id_for_child(self):
        self.click_for_index(self.CREATE_ID, 1)

    def assert_open_form_for_me(self):
        self.assertions.assert_that_element_is_visible(self.FORM_FOR_ME)

    def assert_open_form_for_child(self):
        self.assertions.assert_that_element_is_visible(self.FORM_FOR_CHILD)

    def assert_login_through_services(self):
        self.assertions.assert_that_element_is_clickable(self.LOGIN_VK)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_GMAIL)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_QR)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_FACEBOOK)
        self.assertions.assert_that_element_is_clickable(self.BUTTON_MORE)

    def button_more(self):
        self.click(self.BUTTON_MORE)

    def assert_login_through_element(self):
        self.assertions.assert_that_element_is_clickable(self.LOGIN_MR)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_OK)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_X)

    def assert_login_incorrect(self):
        self.assert_that_element_contains_text(self.TEXT_EROR_LOGIN,
                                        'Нет такого аккаунта. Проверьте логин или войдите по телефону')

    def assert_input_incorrect_password(self):
        self.get_element(self.TEXT_EROR_PASSWORD)
        self.assert_that_element_contains_text(self.TEXT_EROR_PASSWORD,
                                               'Неверный пароль')

    def assert_forgot_password(self):
        self.get_element(self.FORGOT_PASSWORD)
        self.assertions.assert_that_element_is_clickable(self.FORGOT_PASSWORD)

    def assert_password_not_entered(self):
        self.assertions.assert_that_element_contains_text(self.TEXT_EROR_PASSWORD, 'Пароль не указан')

    def assert_login_not_entered(self):
        self.assertions.assert_that_element_contains_text(self.TEXT_EROR_LOGIN, 'Логин не указан')