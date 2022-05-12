from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет активной
    browser.get("http://suninjuly.github.io/wait2.html")
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    time.sleep(4)
    browser.quit()