import time
import math
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    print("\nquit browser...")


class TestMainPage1:

    message_pyst = ""
    massive = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]

    @pytest.mark.parametrize('link', massive)
    def test_guest_should_see_login_link(self, browser, link):
        links = f"https://stepik.org/lesson/{link}/step/1"
        browser.get(links)
        browser.implicitly_wait(10)
        input2 = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
        input2.send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()
        message = WebDriverWait(browser, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
        assert message.text == "Correct!", f"Message c ошибкой: {message.text}"
        if __name__ == "__main__":
            unittest.main()
