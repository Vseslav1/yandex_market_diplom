import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from elements.headers_elements import HeaderElement


@allure.title('Login form visible')
def test_login_form_visible(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.assert_open_form_login()


@allure.title('Form login by phone visible')
def test_login_by_phone(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_by_phone()
    login_page.assert_form_phone_login()


@allure.title('Test open form create id')
def test_open__form_create_id(driver):
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


@allure.title('Test Authorization')
def test_authorization(driver):
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


@allure.title('Test using other services by login')
def test_using_other_services_by_login(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.assert_login_using_other_service()
    login_page.button_more()
    login_page.assert_login_using_other_elements_visible_and_clickable()


@allure.title('Test incorrect login')
def test_entered_incorrect_login(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_input('Egaedszgaezh')
    login_page.click_login()
    login_page.assert_login_entered_incorrect()


@allure.title('Test login not entered')
def test_login_not_entered(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.assert_login_not_entered()


@allure.title('Test incorrect password')
def test_entered_incorrect_password(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_input('vselslav-test.1')
    login_page.click_login()
    login_page.password_input('111111')
    login_page.click_password()
    login_page.assert_entered_incorrect_password()


@allure.title('Test forgot password')
def test_forgot_password(driver):
    main_page = MainPage(driver)
    main_page.open()

    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.login_input('vselslav-test.1')
    login_page.click_login()
    login_page.assert_forgot_password()


@allure.title('Test password not entered')
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
