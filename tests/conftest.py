from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--chrome", action="store_true", default=False, help="Run tests in Chrome"
    )


@pytest.fixture
def driver(request):
    if request.config.getoption("--chrome"):
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        options = FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    driver.maximize_window()
    yield driver
    driver.quit()
