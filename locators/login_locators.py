from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '[class="passp-auth-content"]')
    LOGIN_BY_PHONE_NUMBER = (By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[2]/button')
    PHONE_INPUT = (By.XPATH, '//*[@id="passp-field-phone"]')
    SING_IN_BY_PHONE = (By.XPATH, '//*[@id="passp:sign-in"]')
    TEXT = (By.XPATH, '//*[@id="UserEntryFlow"]/form/div/div[1]/div/h1')
    BUTTON_CREATE_ID = (By.XPATH, '//*[@id="passp:exp-register"]')
    BUTTON_LOGIN = (By.XPATH, '//*[@id="USER_MENU_ANCHOR"]/div/div/a')
    SING_IN = (By.CSS_SELECTOR, '[data-t="button:action:passp:sign-in"]')
    FOR_ME = (By.XPATH,
'//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[4]/div/ul/li[1]/button')
    CREATION_ID_FOR_ME = (By.XPATH, '//*[@id="UserEntryFlow"]/form/div/div[1]/h1')
    CREATION_ID_FOR_CHILD = (By.XPATH,
'//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[4]/div/ul/li[2]/button')
    NAME_ENTERED = (
    By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[2]/div[1]/a/span[2]/span')
    NAME = (By.XPATH, '//*[@id="passp-field-login"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="passp-field-passwd"]')
    BUTTON_PASSWORD = (By.CSS_SELECTOR, '[data-t="button:action:passp:sign-in"]')
    PROFILE = (By.CSS_SELECTOR, '[data-zone-name="profile"]')
    BACK = (By.CSS_SELECTOR, '[data-t="backpane"]')
    TEXT_CREATE = (By.CSS_SELECTOR, '[data-t="title"]')
    LOGIN_VK = (By.CSS_SELECTOR, '[data-t="provider:primary:vk"]')
    LOGIN_GMAIL = (By.CSS_SELECTOR, '[data-t="provider:primary:gg"]')
    LOGIN_QR = (By.CSS_SELECTOR, '[data-t="provider:primary:qr"]')
    LOGIN_FACEBOOK = (By.CSS_SELECTOR, '[data-t="provider:primary:fb"]')
    BUTTON_MORE = (By.CSS_SELECTOR, '[data-t="provider:more"]')
    LOGIN_MR = (By.CSS_SELECTOR, '[data-t="provider:primary:mr"]')
    LOGIN_OK = (By.CSS_SELECTOR, '[data-t="provider:primary:ok"]')
    LOGIN_X = (By.CSS_SELECTOR, '[data-t="provider:primary:tw"]')
    CONTAIN_MENU = (By.CSS_SELECTOR,'[class="_1grEj button-focus-ring _2c__A"]')
    USER_EMAIL = (By.XPATH, '//*[@id="userMenu"]/div[1]/div[1]/a/div/div[2]/div[2]')
    TEXT_BY_INCORRECT_LOGIN = (By.XPATH, '//*[@id="field:input-login:hint"]')
    TEXT_BY_INCORRECT_PASSWORD = (By.XPATH, '//*[@id="field:input-passwd:hint"]')
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="field:link-passwd"]/a')