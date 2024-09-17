import time

from pages.base_page import BasePage
from locators.headers_locators import HeadersLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HeaderElement(BasePage, HeadersLocators):
    def basket_open(self):
        self.click(self.BASKET)


    def open_wish_list(self):
        self.click(self.WISH_LIST)


    def orders_open(self):
        self.click(self.ORDERS)


    def open_login(self):
        self.click(self.BUTTON_LOGIN)


    def open_catalog(self):
        self.click_mouse(self.CATALOG)
        time.sleep(5)


    def open_region(self):
        self.click(self.REGION)


    def open_delivery_for_click(self):
        self.click(self.CLICK_DELIVERY)


    def open_split(self):
        self.click(self.SPLIT)


    def open_favorite_category(self):
        self.click(self.FAVORITE_CATEGORY)


    def open_home_product(self):
        self.click(self.HOME_PRODUCT)

    def open_cloth(self):
        self.click(self.CLOTHE)


    def open_child(self):
        self.click(self.CHILD)


    def open_business(self):
        self.click(self.MARKET_FOR_BUSINESS)


    def open_sell_on_the_market(self):
        self.click(self.SELL_ON_THE_MARKET)