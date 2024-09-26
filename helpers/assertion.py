from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Assertions:


    def __init__(self, driver):
        self.driver = driver


    def assert_that_text_is_visible(self, selector, text):
        el = self.driver.find_element(*selector)
        assert el.text == text


    def assert_that_element_is_visible(self, selector):
        try:
            WebDriverWait (self.driver, 10).until (EC.visibility_of_element_located(selector))
            assert self.driver.find_element (*selector)
        except AssertionError:
            raise AssertionError(f"Element with selector {selector} is not visible within 10 seconds")


    def assert_that_element_contains_text(self, selector, value):
        element = self.driver.find_element(*selector)
        assert element.text == value, 'Text from element does not match value'


    def assert_that_element_is_clickable(self, selector):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(selector))
            assert element is not None, f"Element with selector {selector} is not found."
        except TimeoutException:
            raise AssertionError(f"Element with selector {selector} is not clickable after 10 seconds.")
