import time

from pages.base_page import BasePage
from helpers.url import BASE_URL
from locators.headers_locators import HeadersLocators


class MainPage(BasePage, HeadersLocators):


    def __init__(self, driver):
        super().__init__(driver)



    def open(self):
        self.driver.get(BASE_URL)


    def assert_header_element_visible(self):
        self.assertions.assert_that_element_is_visible(self.BUTTON_LOGIN)
        self.assertions.assert_that_element_is_visible(self.LOGO)
        self.assertions.assert_that_element_is_visible(self.SEARCH)
        self.assertions.assert_that_element_is_visible(self.BASKET)
        self.assertions.assert_that_element_is_visible(self.WISH_LIST)
        self.assertions.assert_that_element_is_visible(self.ORDERS)
        self.assertions.assert_that_element_is_visible(self.CATALOG)
        self.assertions.assert_that_element_is_visible(self.REGION)
        self.assertions.assert_that_element_is_visible(self.CLICK_DELIVERY)
        self.assertions.assert_that_element_is_visible(self.SPLIT)
        self.assertions.assert_that_element_is_visible(self.FAVORITE_CATEGORY)
        self.assertions.assert_that_element_is_visible(self.CLOTHE)
        self.assertions.assert_that_element_is_visible(self.HOME)
        self.assertions.assert_that_element_is_visible(self.CHILD)
        self.assertions.assert_that_element_is_visible(self.MARKET_FOR_BISINESS)
        self.assertions.assert_that_element_is_visible(self.SELL_ON_THE_MARKET)



    def assert_header_element_click(self):
        self.assertions.assert_that_element_is_clickable(self.BASKET)
        self.assertions.assert_that_element_is_clickable(self.WISH_LIST)
        self.assertions.assert_that_element_is_clickable(self.ORDERS)
        self.assertions.assert_that_element_is_clickable(self.LOGO)
        self.assertions.assert_that_element_is_clickable(self.SEARCH_BUTTON)
        self.assertions.assert_that_element_is_clickable(self.BUTTON_LOGIN)
        self.assertions.assert_that_element_is_clickable(self.CATALOG)
        self.assertions.assert_that_element_is_clickable(self.REGION)
        self.assertions.assert_that_element_is_clickable(self.CLICK_DELIVERY)
        self.assertions.assert_that_element_is_clickable(self.SPLIT)
        self.assertions.assert_that_element_is_clickable(self.FAVORITE_CATEGORY)
        self.assertions.assert_that_element_is_clickable(self.CLOTHE)
        self.assertions.assert_that_element_is_clickable(self.HOME)
        self.assertions.assert_that_element_is_clickable(self.CHILD)
        self.assertions.assert_that_element_is_clickable(self.MARKET_FOR_BISINESS)
        self.assertions.assert_that_element_is_clickable(self.SELL_ON_THE_MARKET)


    def get_user_menu(self):
        self.click(self.CONTAIN_MENU)


    def assert_user_authorized(self):
        self.assert_that_element_contains_text(self.USER_EMAIL,'vselslav-test.1@yandex.by')


    def assert_go_to_main_page(self):
        self.assertions.assert_that_element_is_visible(self.LOGO)
        self.save_screenshot('assert_vhod.png')