from selenium.webdriver.common.by import By


class ProductLocator:
    PRODUCT_NAME = (By.CSS_SELECTOR, '[data-auto="productCardTitle"]')
    PRODUCT_PAGE = (By.CSS_SELECTOR, '[data-zone-name="product-page"]')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '[data-zone-name="cartButton"]')
    SIMILAR = (By.CSS_SELECTOR, '[data-auto="search-by-photo-button"]')
    RECOMMENDATION = (By.CSS_SELECTOR, '[data-zone-name="RecommendationRoll"]')
    COMPARISON = (By.CSS_SELECTOR, '[data-autotest-id="comparison"]')
    GO_TO_WHISHLIST = (By.CSS_SELECTOR, '[data-auto="wishlist"]')
    SHARE = (By.CSS_SELECTOR, '[data-zone-name="shortUrl"]')
    BUY_NOW = (By.CSS_SELECTOR, '[data-auto="default-offer-buy-now-button"]')
    SPLIT = (By.CSS_SELECTOR, '[class="_3CCE- _1EcOS _2jQ3e"]')
    MONTH = (By.CSS_SELECTOR, '[class="_3RJHd m1URf"]')
    MORE_PRICES = (By.CSS_SELECTOR, '[data-zone-name="morePricesLink"]')
    PHOTO = (By.CSS_SELECTOR, '[data-auto="image-gallery-nav-item"]')
    SPECS_LIST_MINIMAL = (By.CSS_SELECTOR, '[data-auto="specs-list-minimal"]')
    CPA_OFFER = (By.CSS_SELECTOR, '[data-zone-name="cpa-offer"]')
    CREDIT = (By.CSS_SELECTOR, '[data-auto="main"]')
    ORDR_SPLIT = (By.CSS_SELECTOR, '[data-zone-name="checkout-button"]')


