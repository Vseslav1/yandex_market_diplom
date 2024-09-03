from selenium.webdriver.common.by import By


class MarketYandexLocators:

    LOGO = (By.XPATH,'//*[@id="MainHeader"]/div/header')

    LOGIN = (By.XPATH, '//*[@id="USER_MENU_ANCHOR"]/div')
    LOGO = (By.XPATH, '//*[@id="MainHeader"]/div/header/div[1]/div/noindex/div/div/a[2]')
    SEARCH = (By.XPATH, '//*[@id="header-search"]')
    FORM_LOGIN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]')
    INPUT_SEARCH = (By.XPATH, '//*[@id="header-search"]')
    BUTTON_SEARCH = (By.XPATH, '//*[@id="MainHeader"]/div/header/div[1]/div/div/div/div/div/div/form/div/button')
    RESULT1 = (By.XPATH, '//*[@id="pcxwhp33rn"]/div/div/div[2]/div[1]/div/a')
    PAGE_SEARCH = (By.XPATH, '//*[@id="/content/page/fancyPage/cms"]/div')
    BUTTON_CATALOG = (By.CSS_SELECTOR, '[class="_30-fz button-focus-ring Hkr1q _1pHod _2rdh3 _3rbM-"]')
    CATALOG = (By.XPATH, '/html/body/div[7]')
    BUTTON_LOGIN = (By.XPATH, '//*[@id="USER_MENU_ANCHOR"]/div/div/a')
    NAME = (By.XPATH, '//*[@id="passp-field-login"]')
    SING_IN = (By.XPATH, '//*[@id="passp:sign-in"]')
    NAME_ENTERED = (By.XPATH,
            '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[2]/div[1]/a/span[2]/span')
    BASKET = (By.XPATH, '//*[@id="MainHeader"]/div/header/div[1]/div/div/noindex[2]/nav/ul/li[4]/div/div')
    BASKET_PAGE = (By.XPATH, '//*[@id="cartItems"]/div[2]/div/div[2]/div[1]/div/div/div/ul/li/div/div')
    START_PAGE = (By.XPATH, '//*[@id="MainHeader"]/div/header/div[1]/div/noindex/div/div/a[2]')
    ORDERS = (By.XPATH, '//*[@id="MainHeader"]/div/header/div[1]/div/div/noindex[2]/nav/ul/li[3]/div')
    ORDERS_PAGE = (By.XPATH, '//*[@id="/content/page/fancyPage/layout/searchList/emptyState"]/div')
    FAVORITES = (By.XPATH, '//*[@id="MainHeader"]/div/header/div[1]/div/div/noindex[2]/nav/ul/li[3]/div')
    FAVORITES_PAGE = (By.XPATH, '//*[@id="/content/page/fancyPage/layout/searchList/emptyState"]/div/div')
    TEXT = (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/noindex/div/div/div/nav/div/ul[1]/li[2]/div/div/a/span')
    CONTAIN_MENU = (By.CSS_SELECTOR, '[class="_1grEj button-focus-ring _2c__A"]')
    USER_EMAIL = (By.XPATH, '//*[@id="userMenu"]/div[1]/div[1]/a/div/div[2]/div[2]')
