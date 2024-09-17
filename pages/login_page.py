from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from helpers.url import BASE_URL
from locators.headers_locators import HeadersLocators


class LoginPage(BasePage, LoginLocators, HeadersLocators):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_open_form_login(self):
        self.assert_that_element_is_visible(self.LOGIN_FORM)

    def login_input(self):
        self.fill(self.NAME, 'vselslav-test.1')
        self.click(self.SING_IN)


    def password_input(self):
        self.fill(self.PASSWORD_INPUT, 'qap18test')
        self.click(self.BUTTON_PASSWORD)



    def assert_login_by_phone(self):
        self.click(self.LOGIN_BY_PHONE_NUMBER)
        self.fill(self.PHONE_INPUT, '447955017')
        self.assertions.assert_that_element_is_clickable(self.SING_IN_BY_PHONE)


    def create_id(self):
        self.click(self.BUTTON_CREATE_ID)

    def create_id_for_me(self):
        self.click(self.FOR_ME)

    def create_id_for_child(self):
        self.click(self.CREATION_ID_FOR_CHILD)


    def back_button(self):
        self.click(self.BACK)


    def assert_create_id_for_me(self):
        self.assertions.assert_that_text_is_visible(self.TEXT_CREATE, 'Введите номер телефона для создания Яндекс ID')


    def assert_create_id_for_child(self):
        self.assertions.assert_that_text_is_visible(self.TEXT_CREATE, 'Создайте аккаунт ребёнку')


    def assert_login_through_services(self):
        self.assertions.assert_that_element_is_clickable(self.LOGIN_VK)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_GMAIL)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_QR)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_FACEBOOK)
        self.assertions.assert_that_element_is_clickable(self.BUTTON_MORE)


    def button_more(self):
        self.click(self.BUTTON_MORE)


    def assert_more_login_element(self):
        self.assertions.assert_that_element_is_clickable(self.LOGIN_MR)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_OK)
        self.assertions.assert_that_element_is_clickable(self.LOGIN_X)


    def input_incorrect_login(self):
        self.fill(self.NAME, 'Egaedszgaezh')
        self.click(self.SING_IN)
        self.assert_that_element_contains_text(self.TEXT_BY_INCORRECT_LOGIN,
                                        'Нет такого аккаунта. Проверьте логин или войдите по телефону')


    def input_incorrect_password(self):
        self.click(self.PASSWORD_INPUT)
        self.fill(self.PASSWORD_INPUT, '111111')
        self.click(self.BUTTON_PASSWORD)
        self.assert_that_element_contains_text (self.TEXT_BY_INCORRECT_PASSWORD,
                                               'Неверный пароль')


    def assert_forgot_password(self):
        self.assertions.assert_that_element_is_clickable(self.FORGOT_PASSWORD)


