from selenium.webdriver.common.by import By


class MainPageLocators:
    CATALOG_PAGE = (By.XPATH, '/html/body/div[9]')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-auto="search-input"]')
    PAGE_SEARCH = (By.XPATH, '//*[@id="SerpStatic"]')
    ELECTRONIC = (By.XPATH, '/html/body/div[9]/div/div/div/div/div/div/div[1]/div/ul/li[5]')
    NOTEBOOK = (By.XPATH, '//a[@href="/product--noutbuk-apple-macbook-air-13-late-2020/752262035?hid=90401&show-uid=17266778438583748837516001&nid=26895412&from=search&cpa=1&do-waremd5=byL5TQ7sgERWFm1ucql8zQ&cpc=3awCvv3yLc-ndFDDIPmAyX3zC0TDdGFgzQLqjNHF1W6iquvUGmKua9j0gdjk8zG6u0Mpc8_RHFpDlVkZS_4k9Dus6yGdSKrGPM-kGqnNTKq6staSevJ3JdF6v8qn4Gq0TC38MMbJOyUv5Op2XRewVibaYo0HTZTJejMHlQ93cgl_3gu6pdZIZo460_DsLzsjxlF-r5VFZzsb0px4e3bvHH00QsQaskiE&cc=CjIxNzI2Njc3ODQzNjE5L2QxZjYxNWRjY2NjOTk0ZDRjOGFkODI4MzY3MjIwNjAwLzEvMRDnAYB95u0G&uniqueId=99965120"]')
    USER_MENU = (By.ID, 'USER_MENU_ANCHOR')
