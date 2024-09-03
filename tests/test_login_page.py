import time

import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from elements.headers_elements import HeaderElement


def test_open_login_form(driver):
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
    login_page.assert_login_by_phone()


def test_create_id(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page =LoginPage(driver)
    login_page.create_id()
    login_page.create_id_for_me()
    login_page.assert_create_id_for_me()
    login_page.back_button()
    login_page.create_id()
    login_page.create_id_for_child()
    login_page.assert_create_id_for_child()


def test_input_login_form(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page =LoginPage(driver)
    login_page.login_input()
    login_page.password_input()
    main_page.assert_go_tomain_page()



def test_login_through_services(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.assert_login_through_services()
    login_page.button_more()
    login_page.assert_more_login_element()


def test_input_incorrect_login(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.input_incorrect_login()


def test_input_incorrect_password(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_input()
    login_page.input_incorrect_password()



def test_forgot_password(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_input()
    login_page.assert_forgot_pasword()









