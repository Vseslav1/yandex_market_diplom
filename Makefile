PYTEST=pytest
ALLURE_DIR=allure-results/
ALL=allure_all
PYTEST=pytest
ALLURE_DIR=allure-results/
ALL=allure_all
API_PET=allure_api_pet
API_PET_STORE=allure_api_petstore
USER_API = allure_user_api
LOGIN=allure_login
MAIN=allure_main
PRODUCT=allure_product


API_PET_TESTS = tests/test_pet_api.py
API_PET_STORE_TESTS = tests/test_pet_store_api.py
API_USER_TESTS = tests/test_user_api.py
MAIN_TESTS = tests/test_main_page.py
LOGIN_TESTS = tests/test_login_page.py
PRODUCT_TESTS = tests/test_product.py

test-all:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(ALL)

test-all-chrome:
	$(PYTEST) --chrome --alluredir $(ALLURE_DIR)$(ALL)

test-login:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(LOGIN) $(LOGIN_TESTS)

test-main:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(MAIN) $(MAIN_TESTS)

test-product:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(PRODUCT) $(PRODUCT_TESTS)

test-api-pet:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(API_PET) $(API_PET_TESTS)

test-api-pet-store:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(API_PET_STORE) $(API_PET_STORE_TESTS)

test-api-user:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(USER_API) $(API_USER_TESTS)

test-api-pet-chrome:
	$(PYTEST) --chrome --alluredir $(ALLURE_DIR)$(API_PET) $(API_PET_TESTS)

test-api-pet-store-chrome:
	$(PYTEST) --chrome --alluredir $(ALLURE_DIR)$(API_PET_STORE) $(API_PET_STORE_TESTS)

test-api-user-chrome:
	$(PYTEST) --chrome --alluredir $(ALLURE_DIR)$(USER_API) $(API_USER_TESTS)

test-login-chrome:
	$(PYTEST) --chrome --alluredir $(ALLURE_DIR)$(LOGIN) $(LOGIN_TESTS)

test-main-chrome:
	$(PYTEST) --chrome --alluredir $(ALLURE_DIR)$(MAIN) $(MAIN_FILES)

test-product-chrome:
	$(PYTEST) --chrome --alluredir $(ALLURE_DIR)$(PRODUCT) $(PRODUCT_FILES)

report-all:
	allure serve $(ALLURE_DIR)$(ALL)

report-api-pet:
	allure serve $(ALLURE_DIR)$(API_PET)

report-api-pet-store:
	allure serve $(ALLURE_DIR)$(API_PET_STORE)

report-api-user:
	allure serve $(ALLURE_DIR)$(USER_API)

report-login:
	allure serve $(ALLURE_DIR)$(LOGIN)

report-main:
	allure serve $(ALLURE_DIR)$(MAIN)

report-product:
	allure serve $(ALLURE_DIR)$(PRODUCT)

clean-allure:
	powershell -Command "Remove-Item -Path '$(ALLURE_DIR)' -Recurse -Force"