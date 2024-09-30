from pages.base_page import BasePage
from helpers.url import URL
from locators.headers_locators import HeadersLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.select import Select


class MainPage(BasePage, HeadersLocators, MainPageLocators, URL):


    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.BASE_URL)

    def assert_go_to_main_page(self):
        self.assertions.assert_that_element_is_visible(self.LOGO)

    def assert_header_element_visible(self):
        self.assertions.assert_that_element_is_visible(self.LOGO)
        self.assertions.assert_that_element_is_visible(self.CATALOG)
        self.assertions.assert_that_element_is_visible(self.SEARCH_INPUT)
        self.assertions.assert_that_element_is_visible(self.SEARCH_BUTTON)
        self.assertions.assert_that_element_is_visible(self.BASKET)
        self.assertions.assert_that_element_is_visible(self.PLUS)
        self.assertions.assert_that_element_is_visible(self.FAVORITES)
        self.assertions.assert_that_element_is_visible(self.ORDERS)
        self.assertions.assert_that_element_is_visible(self.BUTTON_LOGIN)
        self.assertions.assert_that_element_is_visible(self.TOP_MENY)
        self.assertions.assert_that_element_is_visible(self.MARKET_FOR_BUSINESS)

    def assert_header_element_click(self):
        self.assertions.assert_that_element_is_clickable(self.LOGO)
        self.assertions.assert_that_element_is_clickable(self.CATALOG)
        self.assertions.assert_that_element_is_clickable(self.SEARCH_BUTTON)
        self.assertions.assert_that_element_is_clickable(self.PLUS)
        self.assertions.assert_that_element_is_clickable(self.ORDERS)
        self.assertions.assert_that_element_is_clickable(self.FAVORITES)
        self.assertions.assert_that_element_is_clickable(self.BASKET)
        self.assertions.assert_that_elements_are_clickable(self.TOP_MENY, 10)
        self.assertions.assert_that_element_is_clickable(self.MARKET_FOR_BUSINESS)

    def assert_open_catalog(self):
        self.assertions.assert_that_element_is_visible(self.CATALOG_WIDGET)

    def assert_click_logo_go_to_main_page(self):
        self.assertions.assert_that_page_open(self.BASE_URL)

    def assert_search_element_visible(self):
        self.assertions.assert_that_element_is_visible(self.PAGE_SEARCH)

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

    def assert_plus_page_open(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertions.assert_that_page_open(self.YANDEX_PLUS_PAGE)

    def assert_open_order_page(self):
        self.assertions.assert_that_page_open(self.ORDER_PAGE)

    def assert_open_favorite_page(self):
        self.assertions.assert_that_page_open(self.FAVORITE_PAGE)

    def assert_open_basket_page(self):
        self.assertions.assert_that_page_open(self.BASKET_URL)

    def assert_login_page_open(self):
        self.assertions.assert_that_page_open(self.LOGIN_PAGE)

    def assert_split_page_open(self):
        self.assertions.assert_that_page_open(self.SPLIT_PAGE)

    def assert_cloth_page_open(self):
        self.assertions.assert_that_page_open(self.CLOTH_PAGE)

    def assert_product_home_page_open(self):
        self.assertions.assert_that_page_open(self.PRODUCT_FOR_HOME_PAGE)

    def assert_product_child_page_open(self):
        self.assertions.assert_that_page_open(self.CHILD_PAGE)

    def assert_beauty_page_open(self):
        self.assertions.assert_that_page_open(self.BEAUTY_PRODUCT_PAGE)

    def assert_electronic_page_open(self):
        self.assertions.assert_that_page_open(self.ELECTRONIC_PAGE)

    def assert_ikea_open(self):
        self.assertions.assert_that_element_contains_text(self.IKEA_TEXT, 'ИКЕА')

    def assert_food_page_open(self):
        self.assertions.assert_that_page_open(self.FOOD_PAGE)

    def assert_open_business_page(self):
        self.assertions.assert_that_page_open(self.BUSINESS_PAGE)

    def assert_sell_on_market_page_open(self):
        self.assertions.assert_that_page_open(self.SELL_PAGE)