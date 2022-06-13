import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    yield browser
    print("\nquit browser...")
    browser.quit()