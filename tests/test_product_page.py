import pytest
from elements.headers_elements import HeaderElement
from pages.product_page import ProductPage


def test_product(driver):
    product_page = ProductPage(driver)
    product_page.open()

    product_page.assert_open_page()


def test_main_elements_visible(driver):
    product_page = ProductPage(driver)
    product_page.open()

    product_page.assert_main_elements_is_visible()


def test_simular(driver):
    product_page = ProductPage(driver)
    product_page.open()

    product_page.open_simular()
    product_page.assert_open_simular()


def test_compare(driver):
    product_page = ProductPage (driver)
    product_page.open ()

    product_page.compare()
    product_page.assert_product_add_compare()


def test_favorites(driver):
    product_page = ProductPage(driver)
    product_page.open()

    product_page.add_to_favorites()

    header_element = HeaderElement(driver)
    header_element.open_favorites()

    product_page.assert_product_in_favorites()


def test_filter(driver):
    product_page = ProductPage(driver)
    product_page.open()

    product_page.click_on_gold()
    product_page.assert_gold_is_selected()
    product_page.click_on_grey()
    product_page.assert_grey_is_selected()


def test_characteristics(driver):
    product_page = ProductPage (driver)
    product_page.open ()

    product_page.click_read_moor()
    product_page.assert_open_characteristics()


def test_add_to_basket(driver):
    product_page = ProductPage(driver)
    product_page.open()

    product_page.add_to_basket()

    header_element = HeaderElement(driver)
    header_element.basket_open()

    product_page.assert_product_in_basket()





