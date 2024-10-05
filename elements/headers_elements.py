import allure
from pages.base_page import BasePage
from locators.headers_locators import HeadersLocators


class HeaderElement(BasePage, HeadersLocators):

    @allure.step('Clicklogo')
    def click_logo(self):
        self.click(self.LOGO)

    def open_catalog(self):
        self.click_mouse(self.CATALOG)

    def search_input(self, text):
        self.fill(self.SEARCH_INPUT, text)

    def button_search(self):
        self.click(self.SEARCH_BUTTON)

    def open_plus(self):
        self.click(self.PLUS)

    def orders_open(self):
        self.click(self.ORDERS)

    def open_favorites(self):
        self.click(self.FAVORITES)

    def basket_open(self):
        self.click(self.BASKET)

    def open_login(self):
        self.click(self.BUTTON_LOGIN)

    def open_delivery(self):
        self.click_mouse(self.DELIVERY)

    def open_thematic(self):
        self.click_for_index(self.TOP_MENY, 0)

    def open_split(self):
        self.click_for_index(self.TOP_MENY, 1)

    def open_favorite_category(self):
        self.click_for_index(self.TOP_MENY, 2)

    def open_cloth(self):
        self.click_for_index(self.TOP_MENY, 3)

    def open_home_product(self):
        self.click_for_index(self.TOP_MENY, 4)

    def open_child(self):
        self.click_for_index(self.TOP_MENY, 5)

    def open_beauty(self):
        self.click_for_index(self.TOP_MENY, 6)

    def open_electronic(self):
        self.click_for_index(self.TOP_MENY, 7)

    def open_ikea(self):
        self.click_for_index(self.TOP_MENY, 8)

    def open_food_product(self):
        self.click_for_index(self.TOP_MENY, 9)

    def open_business(self):
        self.click(self.MARKET_FOR_BUSINESS)

    def open_sell_on_the_market(self):
        self.click_for_index(self.TOP_MENY, 26)