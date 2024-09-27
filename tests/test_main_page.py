from pages.main_page import MainPage
from elements.headers_elements import HeaderElement


def test_headers_element_visible(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.assert_header_element_visible()


def test_headers_element_clickable(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.assert_header_element_click()


def test_catalog(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_catalog()

    main_page.assert_open_catalog()



def test_logo(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.basket_open()
    header_element.click_logo()

    main_page.assert_click_logo_go_to_main_page()


def test_search(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    page_search = MainPage(driver)

    page_search.assert_search_element_visible()


def test_header_search_visible(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    page_search = MainPage(driver)

    page_search.assert_headers_search_visible()


def test_header_search_clickable(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.search_input('макбук эйр м1')
    header_element.button_search()

    page_search = MainPage(driver)

    page_search.assert_headers_search_clickable()


def test_page_plus_open(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_plus()

    main_page.assert_plus_page_open()


def test_order_page_open(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.orders_open()

    main_page.assert_open_order_page()


def test_open_favorite_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_favorites()

    main_page.assert_open_favorite_page()


def test_open_basket_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.basket_open()

    main_page.assert_open_basket_page()


def test_open_login_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    main_page.assert_login_page_open()


def test_open_split_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_split()

    main_page.assert_split_page_open()


def test_open_cloth_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_cloth()

    main_page.assert_cloth_page_open()


def test_open_product_for_home(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_home_product()

    main_page.assert_product_home_page_open()


def test_open_product_for_child(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_child()

    main_page.assert_product_child_page_open()


def test_open_beauty_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_beauty()

    main_page.assert_beauty_page_open()


def test_open_electronic_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_electronic()

    main_page.assert_electronic_page_open()


def test_open_ikea_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_ikea()

    main_page.assert_ikea_page_open()


def test_open_food_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_food_product()

    main_page.assert_food_page_open()


def test_open_business_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_business()

    main_page.assert_open_business_page()


def test_open_sell_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_sell_on_the_market()

    main_page.assert_sell_on_market_page_open()