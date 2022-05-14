import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestAbs(unittest.TestCase):
    def test_1(self):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get("http://suninjuly.github.io/registration1.html")
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//div[1]//div[1]//div[1]/input")
        input1.send_keys("Nina")
        input2 = browser.find_element(By.XPATH, "//div[1]//div[1]//div[2]/input")
        input2.send_keys("Nina")
        input3 = browser.find_element(By.XPATH, "//div[1]//div[1]//div[3]/input")
        input3.send_keys("Nina")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Should be absolute value of a number")
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_2(self):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get("http://suninjuly.github.io/registration2.html")
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//div[1]//div[1]//div[1]/input")
        input1.send_keys("Nina")
        input2 = browser.find_element(By.XPATH, "//div[1]//div[1]//div[2]/input")
        input2.send_keys("Nina")
        input3 = browser.find_element(By.XPATH, "//div[1]//div[1]//div[3]/input")
        input3.send_keys("Nina")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
