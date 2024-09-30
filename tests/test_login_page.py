
from pages.login_page import LoginPage
from pages.main_page import MainPage
from elements.headers_elements import HeaderElement


def test_login_form_visible(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.assert_open_form_login()


def test_sing_in_by_phone(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_by_phone()
    login_page.assert_form_phone_login()


def test_create_id(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.create_id()
    login_page.create_id_for_me()
    login_page.assert_open_form_for_me()
    login_page.back_button()
    login_page.create_id()
    login_page.create_id_for_child()
    login_page.assert_open_form_for_child()


def test_input_login_form(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_input('vselslav-test.1')
    login_page.click_login()
    login_page.password_input('qap18test')
    login_page.click_password()
    main_page.assert_go_to_main_page()



def test_login_through_services(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.assert_login_through_services()
    login_page.button_more()
    login_page.assert_login_through_element()


def test_input_incorrect_login(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_input('Egaedszgaezh')
    login_page.click_login()
    login_page.assert_login_incorrect()


def test_login_not_entered(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.assert_login_not_entered()


def test_input_incorrect_password(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_input('vselslav-test.1')
    login_page.click_login()
    login_page.password_input('111111')
    login_page.click_password()
    login_page.assert_input_incorrect_password()



def test_forgot_password(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_input('vselslav-test.1')
    login_page.click_login()
    login_page.assert_forgot_password()


def test_password_not_entered(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_input('vselslav-test.1')
    login_page.click_login()
    login_page.click_password()
    login_page.assert_password_not_entered()