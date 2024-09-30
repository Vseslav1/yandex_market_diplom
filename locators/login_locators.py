from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '[class="passp-auth-content"]')

    LOGIN_BY_PHONE = (By.CSS_SELECTOR,
        '[data-type="phone"]')
    PHONE_INPUT = (By.XPATH, '//*[@id="passp-field-phone"]')
    SING_IN_BY_PHONE = (By.XPATH, '//*[@id="passp:sign-in"]')
    PHONE_PHORM = (By.CSS_SELECTOR, '[autocomplete="off"]')
    TEXT = (By.XPATH,
        ' //h1[@class="TitleWithDescription-title TitleWithDescription-title_hasDescription '
        'TitleWithDescription-title_align_center TitleWithDescription-title_size_m"]')

    BUTTON_CREATE_ID = (By.XPATH, '//*[@id="passp:exp-register"]')
    CREATE_ID = (By.XPATH,
'//button[@class="RegistrationButtonPopup-itemButton"]')
    FORM_FOR_ME = (By.CSS_SELECTOR, '[class="Phone Phone_0_layout_container"]')
    FORM_FOR_CHILD = (By.CSS_SELECTOR, '[class="passp-route-forward"]')
    BACK = (By.CSS_SELECTOR, '[data-t="backpane"]')

    LOGIN = (By.XPATH, '//*[@id="passp-field-login"]')
    BUTTON_LOGIN = (By.XPATH, '//*[@id="USER_MENU_ANCHOR"]/div/div/a')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="passp-field-passwd"]')
    BUTTON_PASSWORD = (By.CSS_SELECTOR, '[data-t="button:action:passp:sign-in"]')
    SING_IN = (By.CSS_SELECTOR, '[data-t="button:action:passp:sign-in"]')

    TEXT_CREATE = (By.CSS_SELECTOR, '[data-t="title"]')
    LOGIN_VK = (By.CSS_SELECTOR, '[data-t="provider:primary:vk"]')
    LOGIN_GMAIL = (By.CSS_SELECTOR, '[data-t="provider:primary:gg"]')
    LOGIN_QR = (By.CSS_SELECTOR, '[data-t="provider:primary:qr"]')
    LOGIN_FACEBOOK = (By.CSS_SELECTOR, '[data-t="provider:primary:fb"]')
    BUTTON_MORE = (By.CSS_SELECTOR, '[data-t="provider:more"]')
    LOGIN_MR = (By.CSS_SELECTOR, '[data-t="provider:primary:mr"]')
    LOGIN_OK = (By.CSS_SELECTOR, '[data-t="provider:primary:ok"]')
    LOGIN_X = (By.CSS_SELECTOR, '[data-t="provider:primary:tw"]')
    CONTAIN_MENU = (By.CSS_SELECTOR, '[class="_1grEj button-focus-ring _2c__A"]')

    TEXT_EROR_LOGIN= (By.XPATH, '//div[@id="field:input-login:hint"]')
    TEXT_EROR_PASSWORD = (By.XPATH, '//div[@id="field:input-passwd:hint"]')
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="field:link-passwd"]/a')