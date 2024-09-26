import pytest
from pages.search_page import SearchPage
from pages.main_page import MainPage
from elements.headers_elements import HeaderElement
from pages.product_page import ProductPage


def test_search(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.search()

    page_search = SearchPage(driver)

    page_search.assert_search()
    page_search.assert_filters_visible()



def test_all_filters(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.search()

    page_search = SearchPage(driver)

    page_search.click_all_filters()
    page_search.assert_all_filters_page_open()


def test_header_search(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.search()

    page_search = SearchPage(driver)
    page_search.assert_headers_search_visible()
    page_search.assert_headers_search_clickable()
