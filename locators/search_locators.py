from selenium.webdriver.common.by import By


class SearchLocators:
    PAGE_SEARCH = (By.XPATH, '//*[@id="SerpStatic"]')
    FILTERS = (By.ID, "searchFilters")

    ALL_FILTERS = (By.XPATH, '//*[@id="/content/page/fancyPage/allFiltersEntrypoint"]')
    ALL_FILTERS_PAGE = (By.CSS_SELECTOR, '[data-zone-name="all-filters-page"]')

    POPULAR = (By.CSS_SELECTOR, '[data-autotest-id="dpop"]')
    CHEAPER = (By.CSS_SELECTOR, '[data-autotest-id="aprice"]')
    EXPENSIVE = (By.CSS_SELECTOR, '[data-autotest-id="dprice"]')
    RAITING = (By.CSS_SELECTOR, '[data-autotest-id="rating"]')

    LIST =(By.CSS_SELECTOR, '[data-baobab-name="viewtypeList"]')
    GRID =(By.CSS_SELECTOR, '[data-baobab-name="viewtypeGrid"]')
