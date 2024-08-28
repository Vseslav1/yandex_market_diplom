from pages.base_page import BasePage
from locators.locators import MarketYandexLocators


class LoginPage(BasePage, MarketYandexLocators):
    def __init__(self, driver):
        super().__init__(driver)

    def assert_form_visible(self):
        self.click(self.BUTTON_LOGIN)
        self.assertions.assert_that_element_is_visible(self.FORM_LOGIN)


    def assert_login_input(self):
        self.click(self.BUTTON_LOGIN)
        self.fill(self.NAME, 'Vseslav1234')
        self.click(self.SING_IN)
        self.assertions.assert_that_element_is_visible(self.NAME_ENTERED)