import allure
from pages.base_page import BasePage
from locators.headers_locators import HeadersLocators


class HeaderElement(BasePage, HeadersLocators):

    @allure.step('Click logo')
    def click_logo(self):
        self.click(self.LOGO)

    @allure.step('Open catalog')
    def open_catalog(self):
        self.click_mouse(self.CATALOG)

    @allure.step('Execute search input')
    def execute_search_input(self, text):
        self.fill(self.SEARCH_INPUT, text)

    @allure.step('Button search')
    def button_search(self):
        self.click(self.SEARCH_BUTTON)

    @allure.step('Open plus')
    def open_plus(self):
        self.click(self.PLUS)

    @allure.step('Open orders')
    def orders_open(self):
        self.click(self.ORDERS)

    @allure.step('Open favorites')
    def open_favorites(self):
        self.click(self.FAVORITES)

    @allure.step('Open basket')
    def basket_open(self):
        self.click(self.BASKET)

    @allure.step('Open login')
    def open_login(self):
        self.click(self.BUTTON_LOGIN)

    @allure.step('Open delivery')
    def open_delivery(self):
        self.click_mouse(self.DELIVERY)

    @allure.step('Open thematic')
    def open_thematic(self):
        self.click_for_index(self.TOP_MENY, 0)

    @allure.step('Open split')
    def open_split(self):
        self.click_for_index(self.TOP_MENY, 1)

    @allure.step('Favorite category')
    def open_favorite_category(self):
        self.click_for_index(self.TOP_MENY, 2)

    @allure.step('Open cloth')
    def open_cloth(self):
        self.click_for_index(self.TOP_MENY, 3)

    @allure.step('Open home product')
    def open_home_product(self):
        self.click_for_index(self.TOP_MENY, 4)

    @allure.step('Open child')
    def open_child(self):
        self.click_for_index(self.TOP_MENY, 5)

    @allure.step('Open beauty')
    def open_beauty(self):
        self.click_for_index(self.TOP_MENY, 6)

    @allure.step('Open electronic')
    def open_electronic(self):
        self.click_for_index(self.TOP_MENY, 7)

    @allure.step('Open ikea')
    def open_ikea(self):
        self.click_for_index(self.TOP_MENY, 8)

    @allure.step('Open food product')
    def open_food_product(self):
        self.click_for_index(self.TOP_MENY, 9)

    @allure.step('Open business')
    def open_business(self):
        self.click(self.MARKET_FOR_BUSINESS)

    @allure.step('Open sell on market')
    def open_sell_on_the_market(self):
        self.click_for_index(self.TOP_MENY, 26)