from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-auto="search-input"]')
    PAGE_SEARCH = (By.XPATH, '//*[@id="SerpStatic"]')


