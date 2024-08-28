import pytest
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage


@pytest.mark.hm_hm
def test_open_main_page_website(driver):
    page = MainPage(driver)
    page.open()
    page.assert_essential_element_visible()


@pytest.mark.hm
def test_open_basket_page(driver):
    page = MainPage(driver)
    page.open()

    basket = MainPage(driver)
    basket.assert_basket_element_click()


def test_open_favorites_page(driver):
    page = MainPage(driver)
    page.open()

    favorites = MainPage(driver)
    favorites.assert_favorites_element_click()


def test_open_orders_page(driver):
    page = MainPage(driver)
    page.open()

    orders = MainPage(driver)
    orders.assert_orders_element_click()



@pytest.mark.hm
def test_catalog_is_visible(driver):
    page = MainPage(driver)
    page.open()

    catalog = CatalogPage(driver)
    catalog.assert_open_catalog()


@pytest.mark.hm
def test_form_login(driver):
    page = MainPage(driver)
    page.open()

    login_form = LoginPage(driver)
    login_form.assert_form_visible()


@pytest.mark.hm
def test_input_login(driver):
    page = MainPage(driver)
    page.open()

    login = LoginPage(driver)
    login.assert_login_input()


@pytest.mark.hm
def test_search(driver):
    page = MainPage(driver)
    page.open()

    search = CatalogPage(driver)
    search.assert_search()



