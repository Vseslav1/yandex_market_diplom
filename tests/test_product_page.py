import allure
import pytest
from elements.headers_elements import HeaderElement
from pages.product_page import ProductPage
from pages.main_page import MainPage


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page


@pytest.fixture
def header_element(driver, main_page):
    header = HeaderElement(driver)
    header.execute_search_input('макбук эйр м1')
    header.button_search()
    return header


@pytest.fixture
def product_page(driver, header_element):
    page = ProductPage(driver)
    page.open_product_page()
    return page


@allure.title('Test open product page')
def test_open_product_page(main_page, header_element, product_page):

    product_page.assert_product_open()


@allure.title('Test header elements')
def test_header_elements_on_product_page(main_page, header_element, product_page):

    main_page.assert_header_element_visible()


@allure.title('Test main elements visible')
def test_main_elements_visible(main_page, header_element, product_page):

    product_page.assert_main_elements_is_visible()


@allure.title('Test simular')
def test_simular(main_page, header_element, product_page):

    product_page.open_simular()
    product_page.assert_open_simular()


@allure.title('Test add compare')
def test_add_compare(main_page, header_element, product_page):

    product_page.add_compare()
    product_page.assert_product_add_compare()


@allure.title('Test add to favorites')
def test_add_to_favorites(main_page, header_element, product_page):

    product_page.add_to_favorites()

    header_element.open_favorites()

    product_page.assert_product_in_favorites()


@allure.title('Test add to basket')
def test_add_to_basket(main_page, header_element, product_page):

    product_page.add_to_basket()

    header_element.basket_open()

    product_page.assert_product_in_basket()


@allure.title('Test other button')
def test_other_button(main_page, header_element, product_page):

    product_page.other_button_clickable()
