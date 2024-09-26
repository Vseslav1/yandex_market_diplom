from pages.base_page import BasePage
from locators.search_locators import SearchLocators
from helpers.url import BASE_URL
from locators.headers_locators import HeadersLocators


class SearchPage(BasePage,SearchLocators, HeadersLocators):


    def __init__(self, driver):
        super().__init__ (driver)
        self.driver = driver


    def assert_search(self):
        self.assertions.assert_that_element_is_visible(self.PAGE_SEARCH)

    def assert_filters_visible(self):
        self.assertions.assert_that_element_is_visible(self.FILTERS)


    def assert_headers_search_visible(self):
        self.assertions.assert_that_element_is_visible(self.POPULAR)
        self.assertions.assert_that_element_is_visible(self.CHEAPER)
        self.assertions.assert_that_element_is_visible(self.EXPENSIVE)
        self.assertions.assert_that_element_is_visible(self.RAITING)
        self.assertions.assert_that_element_is_visible(self.LIST)
        self.assertions.assert_that_element_is_visible(self.GRID)

    def assert_headers_search_clickable(self):
        self.assertions.assert_that_element_is_clickable(self.CHEAPER)
        self.assertions.assert_that_element_is_clickable(self.EXPENSIVE)
        self.assertions.assert_that_element_is_clickable(self.RAITING)
        self.assertions.assert_that_element_is_clickable(self.LIST)
        self.assertions.assert_that_element_is_clickable(self.GRID)


    def click_all_filters(self):
        self.scroll(self.ALL_FILTERS)
        self.click(self.ALL_FILTERS)

    def assert_all_filters_page_open(self):
        self.assertions.assert_that_element_is_visible(self.ALL_FILTERS_PAGE)
