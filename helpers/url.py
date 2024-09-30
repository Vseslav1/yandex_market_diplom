class URL:
    BASE_URL = 'https://market.yandex.ru/'
    LOGIN_PAGE = ('https://passport.yandex.ru/auth?retpath=http%3A%2F%2Fmarket.yandex.ru%2F%3Floggedin%3D1&backpath='
                  'http%3A%2F%2Fmarket.yandex.ru%2F&origin=market_index_header_nav')
    BASKET_URL = (BASE_URL + 'my/cart')
    YANDEX_PLUS_PAGE = (
        'https://plus.yandex.ru/?utm_source=market&utm_medium='
        'banner&utm_campaign=MSCAMP-77&utm_term=src_market&utm_content='
        'onboarding&message=market')

    ORDER_PAGE = (BASE_URL + 'my/orders?track=menu')
    FAVORITE_PAGE = (BASE_URL + 'my/wishlist?track=head')
    SPLIT_PAGE = (BASE_URL + 'special/split')
    CLOTH_PAGE = (BASE_URL + 'special/fashion_dep')
    PRODUCT_FOR_HOME_PAGE = (BASE_URL + 'catalog--tovary-dlia-doma/54422')
    CHILD_PAGE = (BASE_URL + 'special/kids_dep')
    BEAUTY_PRODUCT_PAGE = (BASE_URL + 'catalog--tovary-dlia-krasoty/54438')
    ELECTRONIC_PAGE = (BASE_URL + 'catalog--elektronika/54440')
    IKEA_PAGE = (BASE_URL + 'https://market.yandex.ru/catalog--tovary-ikea/38679690/list?supplierId=465852&rs='
                            'eJwzsghg_MRozMEosPAQqwSDxr7jrBq3jrBq7Jz0k0njCpBxBIhXg_BRVo2nB24xa_'
                            'wBye5sZ3VqYuSS5uIA6lSQ4FVgEWCT4kxJTUsszSmJN1Jg0GDgUoRKCiqwAiX5YZKG8QWJ6amoSmQVOJCVGCEpgV'
                            'nBqMCIbIUhSFKAyYvDwiLJONUgNTXIyNDcyNzExNzY2MzIwlQ_MTE10dTM0swsBUgZmBuamKSZpFgkJhsmGhkbmBk'
                            'Y6BvqGwIAmGU-PA%2C%2C&searchContext=ikea_ctx')
    FOOD_PAGE = (BASE_URL + 'catalog--produkty-napitki/54434')
    BUSINESS_PAGE = 'https://business.market.yandex.ru/?_redirectCount=1'
    SELL_PAGE = ('https://partner.market.yandex.ru/welcome/?utm_source=yandex_services&utm_medium='
                 'b2c_market&utm_campaign=frontb2c&utm_content=text&utm_term=portalb2b')
    PRODUCT_PAGE = (BASE_URL +
'product--macbook-air-13-2020/1753176222?sku=101832531745&uniqueId='
'67725588&do-waremd5=CXJj9CCrNEVRh8dK2DVovw&nid=26895412')