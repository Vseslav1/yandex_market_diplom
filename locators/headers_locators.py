from selenium.webdriver.common.by import By


class HeadersLocators:
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[data-zone-name="headerLoginButton"]')
    LOGO = (By.CSS_SELECTOR, '[data-auto="logoMarketLink"]')
    CATALOG = (By.CSS_SELECTOR, '[data-zone-name="catalog"]')
    SEARCH = (By.CSS_SELECTOR, '[data-zone-name="search_block"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-auto="search-button"]')
    PLUS = (By.CSS_SELECTOR, '[data-zone-name="yaPlusBadge"]')
    ORDERS = (By.CSS_SELECTOR, '[data-apiary-widget-id="/content/header/header/ordersButton"]')
    WISH_LIST = (By.CSS_SELECTOR, '[data-apiary-widget-id="/content/header/header/wishlistButton"]')
    BASKET = (By.CSS_SELECTOR, '[data-auto="header-cart"]')
    REGION = (By.CSS_SELECTOR, '[data-zone-name="region-select"]')
    CLICK_DELIVERY = (By.CSS_SELECTOR, '[data-zone-name="thematic-entrypoint"]')
    SPLIT = (By.CSS_SELECTOR, '[data-zone-name="category-link"]')
    FAVORITE_CATEGORY = (By.CSS_SELECTOR, '[data-zone-name="tab-with-action"]')
    CLOTHE = (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/noindex/div/div/div/nav/div/ul[1]/li[4]')
    HOME = (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/noindex/div/div/div/nav/div/ul[1]/li[5]')
    CHILD = (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/noindex/div/div/div/nav/div/ul[1]/li[6]')
    MARKET_FOR_BISINESS = (By.CSS_SELECTOR, '[data-zone-name="market-for-business"]')
    SELL_ON_THE_MARKET = (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/noindex/div/div/div/nav/div/ul[2]/li[2]/div')
