from selenium.webdriver.common.by import By


class ProductLocator:
    PRODUCT_NAME = (By.CSS_SELECTOR, '[data-auto="productCardTitle"]')
    PRODUCT_PAGE = (By.CSS_SELECTOR, '[data-zone-name="product-page"]')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '[data-zone-name="cartButton"]')
    PRODUCT_IN_BASKET = (By.XPATH, '//*[@id="cartItems"]/div[2]/div/div/div[2]/div/div/div/ul/li/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div')
    GRADE = (By.CSS_SELECTOR, '[class="_1nuzB _1MOwX _1bCJz _1aCUG iLygt"]')
    FILTERS = (By.CSS_SELECTOR, '[data-baobab-name="filters"]')
    SIMILAR = (By.CSS_SELECTOR, '[data-auto="search-by-photo-button"]')
    RECOMMENDATION = (By.CSS_SELECTOR, '[data-zone-name="RecommendationRoll"]')
    COMPARE = (By.CSS_SELECTOR, '[data-autotest-id="comparison"]')
    ADD_COMPARE = (By.CSS_SELECTOR, '[class="_3bihM _2SUA6 _3kbFf IFARr _1A5yJ"]')
    FAVORITES = (By.CSS_SELECTOR, '[data-autotest-id="wishlist"]')
    PRODUCT_IN_FAVORITES = (By.ID, '/content/page/fancyPage/layout/searchList')
    SHARE = (By.CSS_SELECTOR, '[data-zone-name="shortUrl"]')
    BUY_NOW = (By.CSS_SELECTOR, '[data-auto="default-offer-buy-now-button"]')
    MORE_PRICES = (By.CSS_SELECTOR, '[data-zone-name="morePricesLink"]')
    PHOTO = (By.CSS_SELECTOR, '[data-auto="image-gallery-nav-item"]')
    SPECS_LIST_MINIMAL = (By.CSS_SELECTOR, '[data-auto="specs-list-minimal"]')
    CPA_OFFER = (By.CSS_SELECTOR, '[data-zone-name="cpa-offer"]')
    CREDIT = (By.CSS_SELECTOR, '[data-auto="main"]')
    ORDR_SPLIT = (By.CSS_SELECTOR, '[data-zone-name="checkout-button"]')
    ALL_CHARACTERISTICS = (By.CSS_SELECTOR, '[class="_1_47u _2SUA6 _33utW IFARr _1A5yJ"]')
    ABOUT_PRODUCT = (By.CSS_SELECTOR, '[class="_1NdPg _1MOwX _2eMnU _3DZsR _1O1a7"]')
    PAGE_SIMULAR = (By.XPATH, '//*[@id="searchByPhotoModal"]/div')
    COLOR = (By.XPATH, "//div[@id='cardContent']//h3//span[2]")
    GOLD = (By.XPATH, '//*[@id="15266392"]/label')
    GREY = (By.XPATH, '//*[@id="15277521"]')


