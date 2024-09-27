import time

from pages.base_page import BasePage
from locators.product_locator import ProductLocator
from pages.login_page import LoginPage


class ProductPage(BasePage, ProductLocator):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_product_page(self):
        self.click_for_index(self.PRODUCT_ON_SEARCH, 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.get_element(self.PRODUCT_PAGE)

    def assert_product_open(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_PAGE)

    def assert_main_elements_is_visible(self):
        self.assertions.assert_that_element_is_visible(self.PHOTO)
        self.assertions.assert_that_element_is_visible(self.PRODUCT_NAME)
        self.assertions.assert_that_element_is_visible(self.DESCRIPTION)
        self.assertions.assert_that_element_is_visible(self.PRICE)

    def open_simular(self):
        self.click(self.SIMILAR)

    def assert_open_simular(self):
        self.assertions.assert_that_element_is_visible(self.PAGE_SIMULAR)

    def compare(self):
        self.click(self.COMPARE)

    def assert_product_add_compare(self):
        self.assertions.assert_that_text_is_visible(self.ADD_COMPARE, 'В сравнении')

    def add_to_favorites(self):
        self.click(self.FAVORITES)
        time.sleep(1)

    def assert_product_in_favorites(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_IN_FAVORITES)

    def assert_buy_now_clickable(self):
        self.assertions.assert_that_element_is_clickable(self.PRODUCT_NAME)

    def click_read_moore(self):
        self.click_mouse(self.CHARACTERISTICS)

    def assert_open_characteristics(self):
        self.assertions.assert_that_element_is_visible(self.ALL_CHARACTERISTICS)

    def add_to_basket(self):
        self.click_mouse(self.ADD_TO_BASKET)
        self.get_element(self.QUANTITY)

    def assert_product_in_basket(self):
        self.assertions.assert_that_element_contains_text(self.PRODUCT_IN_BASKET, '1 товар')