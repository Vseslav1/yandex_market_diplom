from pages.base_page import BasePage
from helpers.url import PRODUCT_URL
from locators.headers_locators import HeadersLocators
from locators.product_locator import ProductLocator


class ProductPage(BasePage,ProductLocator):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver


    def open(self):
        self.driver.get(PRODUCT_URL)


    def assert_open_page(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_PAGE)


    def add_to_basket(self):
        self.click(self.ADD_TO_BASKET)


    def main_elements_is_visible(self):
        self.assertions.assert_that_element_is_visible(self.PHOTO)
        self.assertions.assert_that_element_is_visible(self.PRODUCT_NAME)
        self.assertions.assert_that_element_is_visible(self.SPECS_LIST_MINIMAL)
        self.assertions.assert_that_element_is_visible(self.CPA_OFFER)
        self.assertions.assert_that_element_is_visible(self.CREDIT)



    def main_elements_are_clickable(self):
        self.assertions.assert_that_element_is_clickable(self.SIMILAR)
        self.assertions.assert_that_element_is_clickable(self.COMPARISON)
        self.assertions.assert_that_element_is_clickable(self.GO_TO_WHISHLIST)
        self.assertions.assert_that_element_is_clickable(self.SHARE)
        self.assertions.assert_that_element_is_clickable(self.BUY_NOW)
        self.assertions.assert_that_element_is_clickable(self.SPLIT)
        self.assertions.assert_that_elements_are_clickable(self.MONTH)
        self.assertions.assert_that_element_are_clickable(self.MORE_PRICES)
        self.assertions.assert_that_element_are_clickable(self.MONTH)
        self.assertions.assert_that_element_is_clickable(self.ORDR_SPLIT)
