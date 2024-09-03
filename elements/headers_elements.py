from pages.base_page import BasePage
from locators.locators import MarketYandexLocators
from locators.headers_locators import HeadersLocators


class HeaderElement(BasePage, MarketYandexLocators, HeadersLocators):
    def basket_open(self):
        self.click(self.BASKET)


    def favorites_open(self):
        self.click(self.FAVORITES)



    def orders_open(self):
        self.click (self.ORDERS)



    def open_login(self):
        self.click(self.BUTTON_LOGIN)
