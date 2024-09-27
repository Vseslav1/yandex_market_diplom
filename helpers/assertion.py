from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait



class Assertions:

    def __init__(self, driver):
        self.driver = driver


    def assert_that_text_is_visible(self, selector, text):
        el = self.driver.find_element(*selector)
        assert el.text == text


    def assert_that_page_open(self, expected_url, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.current_url == expected_url)
        except TimeoutException:
            raise AssertionError(
                f"Timed out waiting for URL to be {expected_url}. Current URL: {self.driver.current_url}")
        assert self.driver.current_url


    def assert_that_element_is_visible(self, selector):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector))
            assert self.driver.find_element(*selector)
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


    def assert_that_elements_are_clickable(self, selector, elements_cont):
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(selector))
            assert len(elements) == elements_cont
            for index, element in enumerate(elements):
                elements_clickable = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
                assert elements_clickable
            return True
        except Exception as e:
            print(f"Произошла ошибка: {e}")