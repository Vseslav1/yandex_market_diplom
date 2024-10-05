
# YANDEX MARKET SITE AUTOMATION PROJECT


This project is designed to automate testing of the functionality of the Yandex.Market website using Selenium WebDriver and Python. The project includes a set of tests to test various operations on the site, such as searching for products, authorizing users, adding products to the cart
.

This project can be run on two browsers: Google Chrome and Mozilla Firefox

The project also contains API tests for https://petstore.swagger.io/.

Docker containerization has been completed. 

All tests are structured with an Page Object Model patern

## Tehnologies

- Python 3.12
- Selenium WebDriver
- pytest
- allure-pytest
- Docker

## Installation and configuration

1. **Clone repository**

git clone https://github.com/Vseslav1/yandex_market_diplom.git

- cd yandex_market_diplom



2 **Install dependencies**


   Make sure you have `pip` installed, then run:


- pip install  -r requirements.txt



2. ## Running tests

You can use the following commands to run tests:

1 **Run tests with pytest**

- pytest

2 **Run all tests with make and allure**

- make test-all - to run on Firefox
- make test-all-chrome - to run on Chrome

3 **To view test results**

- report-all


