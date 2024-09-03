import time

from pages.base_page import BasePage
from helpers.url import BASE_URL
from locators.locators import MarketYandexLocators


class MainPage(BasePage, MarketYandexLocators):


    def __init__(self, driver):
        super().__init__(driver)



    def open(self):
        self.driver.get(BASE_URL)


    def assert_essential_element_visible(self):
        self.assertions.assert_that_element_is_visible(self.LOGIN)
        self.assertions.assert_that_element_is_visible(self.LOGO)
        self.assertions.assert_that_element_is_visible(self.SEARCH)
        self.assertions.assert_that_element_is_visible(self.BASKET)
        self.assertions.assert_that_element_is_visible(self.FAVORITES)
        self.assertions.assert_that_element_is_visible(self.ORDERS)


    def assert_basket_element_click(self):
        self.click(self.BASKET)
        self.assertions.assert_that_element_is_visible(self.BASKET_PAGE)

    def assert_favorites_element_click(self):
        self.click(self.FAVORITES)
        self.assertions.assert_that_element_is_visible(self.FAVORITES_PAGE)

    def assert_orders_element_click(self):
        self.click(self.ORDERS)
        self.assertions.assert_that_element_is_visible(self.ORDERS_PAGE)

    def get_user_menu(self):
        self.click(self.CONTAIN_MENU)


    def assert_user_authorized(self):
        self.assert_that_element_contains_text(self.USER_EMAIL,'vselslav-test.1@yandex.by')


    def assert_go_tomain_page(self):
        self.assertions.assert_that_element_is_visible(self.LOGO)
        self.save_screenshot('assert_vhod.png')