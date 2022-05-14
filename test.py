from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://www.google.ru/")
    input = browser.find_element(By.CLASS_NAME, "gLFyf.gsfi")
    input.send_keys("Кардашьяны")
    time.sleep(2)
    #button = browser.find_element(By.CLASS_NAME, "gNO89b")
    #button.click()
finally:
    time.sleep(4)
    browser.quit()