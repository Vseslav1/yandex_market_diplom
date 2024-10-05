import time
import allure
from pages.base_page import BasePage
from locators.product_locator import ProductLocator


class ProductPage(BasePage, ProductLocator):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open product page')
    def open_product_page(self):
        self.click_for_index(self.PRODUCT_ON_SEARCH, 1)
        self.switch_window(1)
        self.get_element(self.PRODUCT_PAGE)

    @allure.step('Assert product open')
    def assert_product_open(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_PAGE)

    @allure.step('Assert main elements visible')
    def assert_main_elements_is_visible(self):
        self.assertions.assert_that_element_is_visible(self.PHOTO)
        self.assertions.assert_that_element_is_visible(self.PRODUCT_NAME)
        self.assertions.assert_that_element_is_visible(self.DESCRIPTION)
        self.assertions.assert_that_element_is_visible(self.PRICE)

    @allure.step('Open simular')
    def open_simular(self):
        self.click(self.SIMILAR)

    @allure.step('Assert open simular')
    def assert_open_simular(self):
        self.assertions.assert_that_element_is_visible(self.PAGE_SIMULAR)

    @allure.step('Add compare')
    def add_compare(self):
        self.click(self.COMPARE)
        time.sleep(1)

    @allure.step('Assert add compare')
    def assert_product_add_compare(self):
        self.assertions.assert_that_element_contains_text(self.ADD_COMPARE, 'В сравнении')

    @allure.step('Add to favorites')
    def add_to_favorites(self):
        self.click(self.FAVORITES)
        time.sleep(1)

    @allure.step('Assert to favorites')
    def assert_product_in_favorites(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_IN_FAVORITES)

    @allure.step('Add to basket')
    def add_to_basket(self):
        self.click_mouse(self.ADD_TO_BASKET)
        self.get_element(self.QUANTITY)

    @allure.step('Assert product in basket')
    def assert_product_in_basket(self):
        self.assertions.assert_that_element_contains_text(self.PRODUCT_IN_BASKET, '1 товар')

    @allure.step('Other button clickable')
    def other_button_clickable(self):
        self.assertions.assert_that_element_is_clickable(self.PRODUCT_NAME)
        self.assertions.assert_that_element_is_clickable(self.CHARACTERISTICS)
        self.assertions.assert_that_element_is_visible(self.BUY_NOW)
        self.assertions.assert_that_element_is_clickable(self.MORE_PRICES)
