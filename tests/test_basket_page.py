import pytest
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from elements.headers_elements import HeaderElement


def test_add_to_basket(driver):
    product_page = ProductPage(driver)
    product_page.open()

    product_page.add_to_basket()

    header_element = HeaderElement(driver)
    header_element.basket_open()

    basket_page = BasketPage(driver)
    basket_page.assert_product_add_to_basket()

