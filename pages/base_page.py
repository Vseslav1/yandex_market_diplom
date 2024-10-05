import allure
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

    @allure.step('Open page')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Click')
    def click(self, selector, force=False):
        element = self.driver.find_element(*selector)
        if force:
            self.driver.execute_script("arguments[0].click();", element)
        element.click()

    @allure.step('Click mouse')
    def click_mouse(self, selector):
        element = self.get_element(selector)
        actions = ActionChains(self.driver)
        actions.click(element).perform()

    @allure.step('Fill text')
    def fill(self, selector, text):
        element = self.driver.find_element(*selector)
        element.send_keys(text)

    @allure.step('Save screenshot')
    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    @allure.step('Get element')
    def get_element(self, selector):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(selector))
        return element

    @allure.step('Scroll to element')
    def scroll(self, selector):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(selector))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.driver.execute_script("window.scrollBy(0, -100);")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    @allure.step('Clik for index')
    def click_for_index(self, selector, index):
        tabs = self.driver.find_elements(*selector)
        if 0 <= index < len(tabs):
            try:
                tabs[index].click()
            except Exception as e:
                print(f"Could not click on tab {index + 1}: {str(e)}")
        else:
            print(f"Index {index + 1} is out of range. There are {len(tabs)} tabs.")

    @allure.step('Switch to window')
    def switch_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])
