from helpers.assertion import Assertions


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

    def get_element(self, selector):
        return self.driver.find_element (*selector)

    def add_cookie(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.add_cookie (cookie)
