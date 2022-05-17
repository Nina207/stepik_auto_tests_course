import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

answer = math.log(int(time.time()))
answer1 = str(answer)


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser...")


@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, links):
    links = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(links)
    input2 = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view")
    input2.send_keys(answer1)
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    assert message == "Correct!"
