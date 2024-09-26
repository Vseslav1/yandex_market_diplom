import time

from pages.base_page import BasePage
from helpers.url import PRODUCT_URL
from locators.headers_locators import HeadersLocators
from locators.product_locator import ProductLocator


class ProductPage(BasePage, ProductLocator):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver


    def open(self):
        self.driver.get(PRODUCT_URL)

    def assert_main_elements_is_visible(self):
        self.assertions.assert_that_element_is_visible(self.PHOTO)
        self.assertions.assert_that_element_is_visible(self.PRODUCT_NAME)
        self.assertions.assert_that_element_is_visible(self.SPECS_LIST_MINIMAL)
        self.assertions.assert_that_element_is_visible(self.CPA_OFFER)
        self.assertions.assert_that_element_is_visible(self.FILTERS)



    def assert_open_page(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_PAGE)


    def add_to_basket(self):
        self.click(self.ADD_TO_BASKET)
        time.sleep(1)

    def assert_product_in_basket(self):
        self.assertions.assert_that_element_contains_text(self.PRODUCT_IN_BASKET, '1 товар')

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


    def assert_product_in_favorites(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_IN_FAVORITES)


    def assert_buy_now_clickable(self):
        self.assertions.assert_that_element_is_clickable(self.PRODUCT_NAME)


    def click_on_gold(self):
        self.click(self.GOLD)
        time.sleep(2)


    def assert_gold_is_selected(self):
        self.assertions.assert_that_text_is_visible(self.COLOR, ': золотой')


    def click_on_grey(self):
        self.click(self.GREY)
        time.sleep(2)


    def assert_grey_is_selected(self):
        self.assertions.assert_that_text_is_visible(self.COLOR, ': серый космос')


    def click_read_moor(self):
        self.click(self.ALL_CHARACTERISTICS)


    def assert_open_characteristics(self):
        self.assertions.assert_that_element_is_visible(self.ABOUT_PRODUCT)
