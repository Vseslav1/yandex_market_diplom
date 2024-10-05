import allure

from pages.base_page import BasePage
from helpers.url import URL
from locators.headers_locators import HeadersLocators
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage, HeadersLocators, MainPageLocators, URL):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Open main page')
    def open(self):
        self.driver.get(self.BASE_URL)

    @allure.step('Assert open Base Page')
    def assert_open_main_page(self):
        self.assertions.assert_that_page_open(self.BASE_URL)

    @allure.step('Go to home page logo visible')
    def assert_go_to_main_page(self):
        self.assertions.assert_that_element_is_visible(self.LOGO)

    @allure.step('Assert header element visible')
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

    @allure.step('Assert open catalog widget')
    def assert_open_catalog_widget(self):
        self.assertions.assert_that_element_is_visible(self.CATALOG_WIDGET)

    @allure.step('Assert click logo go to main page')
    def assert_click_logo_go_to_main_page(self):
        self.assertions.assert_that_page_open(self.BASE_URL)

    @allure.step('Assert search page open')
    def assert_page_search_open(self):
        self.assertions.assert_that_element_is_visible(self.PAGE_SEARCH)

    @allure.step('Assert filters on search page visible')
    def assert_search_filters_visible(self):
        self.assertions.assert_that_element_is_visible(self.FILTERS)

    @allure.step('Assert header search visible')
    def assert_headers_search_visible(self):
        self.assertions.assert_that_element_is_visible(self.POPULAR)
        self.assertions.assert_that_element_is_visible(self.CHEAPER)
        self.assertions.assert_that_element_is_visible(self.EXPENSIVE)
        self.assertions.assert_that_element_is_visible(self.RAITING)
        self.assertions.assert_that_element_is_visible(self.LIST)
        self.assertions.assert_that_element_is_visible(self.GRID)

    @allure.step('Assert header search clickable')
    def assert_headers_search_clickable(self):
        self.assertions.assert_that_element_is_clickable(self.CHEAPER)
        self.assertions.assert_that_element_is_clickable(self.EXPENSIVE)
        self.assertions.assert_that_element_is_clickable(self.RAITING)
        self.assertions.assert_that_element_is_clickable(self.LIST)
        self.assertions.assert_that_element_is_clickable(self.GRID)

    @allure.step('Assert plus page open')
    def assert_plus_page_open(self):
        self.switch_window(1)
        self.assertions.assert_that_page_open(self.YANDEX_PLUS_PAGE)

    @allure.step('Assert order page open')
    def assert_open_order_page(self):
        self.assertions.assert_that_page_open(self.ORDER_PAGE)

    @allure.step('Assert favorite page open')
    def assert_open_favorite_page(self):
        self.assertions.assert_that_page_open(self.FAVORITE_PAGE)

    @allure.step('Assert basket page open')
    def assert_open_basket_page(self):
        self.assertions.assert_that_page_open(self.BASKET_URL)

    @allure.step('Assert login page open')
    def assert_login_page_open(self):
        self.assertions.assert_that_page_open(self.LOGIN_PAGE)

    @allure.step('Assert split page open')
    def assert_split_page_open(self):
        self.assertions.assert_that_page_open(self.SPLIT_PAGE)

    @allure.step('Assert cloth page open')
    def assert_cloth_page_open(self):
        self.assertions.assert_that_page_open(self.CLOTH_PAGE)

    @allure.step('Assert product for home open')
    def assert_product_home_page_open(self):
        self.assertions.assert_that_page_open(self.PRODUCT_FOR_HOME_PAGE)

    @allure.step('Assert product for child open')
    def assert_product_child_page_open(self):
        self.assertions.assert_that_page_open(self.CHILD_PAGE)

    @allure.step('Assert beauty page open')
    def assert_beauty_page_open(self):
        self.assertions.assert_that_page_open(self.BEAUTY_PRODUCT_PAGE)

    @allure.step('Assert electronic page open')
    def assert_electronic_page_open(self):
        self.assertions.assert_that_page_open(self.ELECTRONIC_PAGE)

    @allure.step('Assert ikea page open')
    def assert_ikea_open(self):
        self.assertions.assert_that_element_contains_text(self.IKEA_TEXT, 'ИКЕА')

    @allure.step('Assert food page open')
    def assert_food_page_open(self):
        self.assertions.assert_that_page_open(self.FOOD_PAGE)

    @allure.step('Assert business page open')
    def assert_open_business_page(self):
        self.assertions.assert_that_page_open(self.BUSINESS_PAGE)

    @allure.step('Assert sell on the market page open')
    def assert_sell_on_market_page_open(self):
        self.assertions.assert_that_page_open(self.SELL_PAGE)
