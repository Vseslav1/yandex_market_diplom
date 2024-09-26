import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from elements.headers_elements import HeaderElement
from pages.search_page import SearchPage




def test_headers_element_visible(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.assert_header_element_visible()


def test_headers_element_click(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.assert_header_element_click()











