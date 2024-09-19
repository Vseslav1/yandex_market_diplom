import pytest
from elements.headers_elements import HeaderElement
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


def test_product(driver):
    product_page = ProductPage(driver)
    product_page.open()

    product_page.assert_open_page()


def test_main_elements_clickable(driver):
    product_page = ProductPage(driver)
    product_page.open()

    product_page.main_elements_are_clickable()


def test_main_elements_visible(driver):
    product_page = ProductPage(driver)
    product_page.open()

    product_page.main_elements_is_visible()



