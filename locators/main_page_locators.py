from selenium.webdriver.common.by import By


class MainPageLocators:
    CATALOG_PAGE = (By.XPATH, '/html/body/div[9]')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-auto="search-input"]')
    PAGE_SEARCH = (By.XPATH, '//*[@id="SerpStatic"]')
    ELECTRONIC = (By.XPATH, '/html/body/div[9]/div/div/div/div/div/div/div[1]/div/ul/li[5]')
    NOTEBOOK = (By.XPATH, '//a[@href="https://market.yandex.ru/catalog--noutbuki/26895412/list?hid=91013&local-offers-first=0"]')
    USER_MENU = (By.ID, 'USER_MENU_ANCHOR')
