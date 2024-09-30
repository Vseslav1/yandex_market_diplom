from elements.headers_elements import HeaderElement
from pages.product_page import ProductPage
from pages.main_page import MainPage


def test_open_product_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    product_page = ProductPage(driver)
    product_page.open_product_page()
    product_page.assert_product_open()


def test_header_elements_on_product_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    product_page = ProductPage(driver)
    product_page.open_product_page()

    main_page.assert_header_element_visible()
    main_page.assert_header_element_click()


def test_main_elements_visible(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    product_page = ProductPage(driver)
    product_page.open_product_page()

    product_page.assert_main_elements_is_visible()


def test_simular(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    product_page = ProductPage(driver)
    product_page.open_product_page()

    product_page.open_simular()
    product_page.assert_open_simular()


def test_compare(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    product_page = ProductPage(driver)
    product_page.open_product_page()

    product_page.compare()
    product_page.assert_product_add_compare()


def test_favorites(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    product_page = ProductPage(driver)
    product_page.open_product_page()

    product_page.add_to_favorites()

    header_element = HeaderElement(driver)
    header_element.open_favorites()

    product_page.assert_product_in_favorites()


def test_add_to_basket(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    product_page = ProductPage(driver)
    product_page.open_product_page()
    product_page.add_to_basket()

    header_element = HeaderElement(driver)
    header_element.basket_open()

    product_page.assert_product_in_basket()


def test_other_button(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    product_page = ProductPage(driver)
    product_page.open_product_page()

    product_page.other_button_clickable()