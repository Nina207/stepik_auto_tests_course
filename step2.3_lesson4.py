import math
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("http://suninjuly.github.io/alert_accept.html")
    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    num = browser.find_element(By.ID, "input_value")
    num1 = num.text
    number = calc(num1)
    input = browser.find_element(By.CLASS_NAME, "form-control")
    input.send_keys(number)
    submit2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
finally:
    time.sleep(4)
    browser.quit()