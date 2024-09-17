from helpers.assertion import Assertions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(Assertions):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.assertions = Assertions(driver)

    def click(self, selector):
        element = self.driver.find_element(*selector)
        element.click()

    def click_js(self,selector):
        element = self.driver.find_element (*selector)
        element.click()
        self.driver.execute_script ("arguments[0].click();", element)
        WebDriverWait (self.driver, 10).until (EC.visibility_of_element_located (selector))


    def click_element(self, selector):
        element = self.driver.find_element(*selector)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector))
        self.driver.execute_script("arguments[0].setAttribute('aria-expanded', 'true');", element)


    def click_mouse(self, selector):
        element = self.get_element(selector)
        actions = ActionChains(self.driver)
        actions.click(element).perform()


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


    def get_element(self, selector):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(selector))
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