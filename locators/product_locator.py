from selenium.webdriver.common.by import By


class ProductLocator:
    PRODUCT_PAGE = (By.XPATH, '//div[@id="cardContent"]')
    PRODUCT_ON_SEARCH = (By.XPATH, '//div[@data-apiary-widget-name="@marketfront/SerpEntity"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[data-auto="productCardTitle"]')
    PHOTO = (By.CSS_SELECTOR, '[data-auto="image-gallery-nav-item"]')
    DESCRIPTION = (By.CSS_SELECTOR, '[data-auto="specs-list-minimal"]')
    PRICE = (By.CSS_SELECTOR, '[data-apiary-widget-id="/content/page/fancyPage/mainDO"]')


    ADD_TO_BASKET = (By.CSS_SELECTOR, '[data-zone-name="cartButton"]')
    PRODUCT_IN_BASKET = (By.XPATH, '//div[@class="HLUwt _2ixvm _2SUA6 _33utW IFARr _1A5yJ"]')

    SIMILAR = (By.CSS_SELECTOR, '[data-auto="search-by-photo-button"]')
    RECOMMENDATION = (By.CSS_SELECTOR, '[data-zone-name="RecommendationRoll"]')

    COMPARE = (By.CSS_SELECTOR, '[data-autotest-id="comparison"]')
    ADD_COMPARE = (By.CSS_SELECTOR, '[class="_3bihM _2SUA6 _3kbFf IFARr _1A5yJ"]')

    FAVORITES = (By.CSS_SELECTOR, '[data-autotest-id="wishlist"]')
    PRODUCT_IN_FAVORITES = (By.ID, '/content/page/fancyPage/layout/searchList')

    SHARE = (By.CSS_SELECTOR, '[data-zone-name="shortUrl"]')

    BUY_NOW = (By.CSS_SELECTOR, '[data-auto="default-offer-buy-now-button"]')

    MORE_PRICES = (By.CSS_SELECTOR, '[data-zone-name="morePricesLink"]')


    CHARACTERISTICS = (By.CSS_SELECTOR, '[class="_1_47u _2SUA6 _33utW IFARr _1A5yJ"]')
    ALL_CHARACTERISTICS = (By.CSS_SELECTOR, '[class="_1NdPg _1MOwX _2eMnU _3DZsR _1O1a7"]')

    PAGE_SIMULAR = (By.XPATH, '//*[@id="searchByPhotoModal"]/div')

    QUANTITY = (By.CSS_SELECTOR, '[data-auto="counter-cart-button"]')