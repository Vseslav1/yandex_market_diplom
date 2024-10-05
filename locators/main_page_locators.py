from selenium.webdriver.common.by import By


class MainPageLocators:

    PAGE_SEARCH = (By.CSS_SELECTOR, '[data-zone-name="searchPage"]')

    FILTERS = (By.XPATH, '//div[@data-zone-name="SearchFilters"]')

    POPULAR = (By.CSS_SELECTOR, '[data-autotest-id="dpop"]')
    CHEAPER = (By.CSS_SELECTOR, '[data-autotest-id="aprice"]')
    EXPENSIVE = (By.CSS_SELECTOR, '[data-autotest-id="dprice"]')
    RAITING = (By.CSS_SELECTOR, '[data-autotest-id="rating"]')

    LIST = (By.CSS_SELECTOR, '[data-baobab-name="viewtypeList"]')
    GRID = (By.CSS_SELECTOR, '[data-baobab-name="viewtypeGrid"]')

    CATALOG_WIDGET = (By.CSS_SELECTOR, '[class="_12ret _1Fik6"]')

    IKEA_TEXT = (By.XPATH, '//span[@data-auto="chip-name"]')
