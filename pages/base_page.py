from helpers.assertion import Assertions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage(Assertions):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.assertions = Assertions(driver)

    def click(self, selector):
        element = self.driver.find_element(*selector)
        element.click()


    def fill(self, selector, text):
        element = self.driver.find_element(*selector)
        element.send_keys(text)


    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def open_page(self, url):
        self.driver.get(url)


    def add_cookie(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.add_cookie (cookie)


    def get_text(self, selector):
        element = self.driver.find_element(*selector)
        return element.text


    def get_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        return element


    def select_by_index(self, selector, index):
        select = Select(self.get_element(selector))
        select.select_by_index(index)


    def select_by_visible_text(self, selector, text):
        select = Select(self.get_element(selector))
        select.select_by_visible_text(text)


    def select_by_value(self, selector, value):
        select = Select(self.get_element(selector))
        select.select_by_value(value)