import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from elements.headers_elements import HeaderElement




def test_headers_element_visible(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.assert_header_element_visible()


def test_headers_element_click(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.assert_header_element_click()


def test_catalog(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_catalog()


    main_page.assert_open_catalog()


def test_search(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.search()
    main_page.assert_search()







