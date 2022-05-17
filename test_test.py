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

try:
    links = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(links)
    input2 = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view")
    input2.send_keys(answer1)
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    assert message == "Correct!"
finally:
    time.sleep(3)
    browser.quit()