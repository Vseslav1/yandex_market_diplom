from pages.base_page import BasePage
from locators.basket_locators import BasketLocators
from helpers.url import BASE_URL
from locators.headers_locators import HeadersLocators


class BasketPage(BasePage,BasketLocators, HeadersLocators):


    def __init__(self, driver):
        super().__init__ (driver)
        self.driver = driver


    def assert_product_add_to_basket(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_IN_BASKET)
