import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    num = browser.find_element(By.ID, "input_value")
    num1 = num.text
    number = calc(num1)
    input = browser.find_element(By.CLASS_NAME, "form-control")
    input.send_keys(number)
    submit2 = browser.find_element(By.ID, "solve")
    submit2.click()
finally:
    time.sleep(4)
    browser.quit()