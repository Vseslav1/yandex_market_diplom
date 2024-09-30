from selenium.webdriver.common.by import By



class HeadersLocators:
    LOGO = (By.CSS_SELECTOR, '[data-auto="logoMarketLink"]')

    CATALOG = (By.XPATH, '//div[@class="cia-vs cia-cs"]')

    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-auto="search-button"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-auto="search-input"]')

    PLUS = (By.CSS_SELECTOR, '[data-zone-name="yaPlusBadge"]')

    ORDERS = (By.XPATH, '//div[@data-baobab-name="orders"]')

    FAVORITES = (By.CSS_SELECTOR, '[class="_11Nqc _3dlQc _2q1BP"]')

    BUTTON_LOGIN = (By.CSS_SELECTOR, '[data-zone-name="headerLoginButton"]')

    BASKET = (By.CSS_SELECTOR, '[data-auto="header-cart"]')

    DELIVERY = (By.XPATH, '//span[@class="_1_C0_ _1n-yE _33-CL _2BojB _22iQ6"]')

    TOP_MENY = (By.XPATH, '//li[@role="tab"]')

    MARKET_FOR_BUSINESS = (By.CSS_SELECTOR, '[data-zone-name="market-for-business"]')

    PRODUCT_ONE = (By.XPATH, '//div[@data-apiary-widget-name="@marketfront/SerpEntity"]')