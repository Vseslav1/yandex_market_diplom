from selenium.webdriver.common.by import By


class MainPageLocators:

    PAGE_SEARCH = (By.CSS_SELECTOR, '[data-auto="SerpList"]')

    ALL_FILTERS = (By.XPATH, '//button[@class="_3CCE- _1Mcpo _2jQ3e _3ozc8"]')
    ALL_FILTERS_PAGE = (By.CSS_SELECTOR, '[data-zone-name="all-filters-page"]')

    POPULAR = (By.CSS_SELECTOR, '[data-autotest-id="dpop"]')
    CHEAPER = (By.CSS_SELECTOR, '[data-autotest-id="aprice"]')
    EXPENSIVE = (By.CSS_SELECTOR, '[data-autotest-id="dprice"]')
    RAITING = (By.CSS_SELECTOR, '[data-autotest-id="rating"]')

    LIST = (By.CSS_SELECTOR, '[data-baobab-name="viewtypeList"]')
    GRID = (By.CSS_SELECTOR, '[data-baobab-name="viewtypeGrid"]')

    CATALOG_WIDGET = (By.CSS_SELECTOR, '[class="_12ret _1Fik6"]')
