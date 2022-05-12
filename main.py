import math
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/cats.html")
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    time.sleep(4)
    browser.quit()