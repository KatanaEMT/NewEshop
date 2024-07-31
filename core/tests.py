from django.test import TestCase
from costumerapp.utils import get_driver

from django.test import TestCase
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from costumerapp.utils import get_driver


class CostumerTestCase(TestCase):
    def test_product(self):
        driver = get_driver()
        driver.get("http://localhost:8000/")
        sleep(1)
        btn_element = driver.find_element(By.ID, "drop-info")
        btn_product_element = driver.find_element(By.ID, "btn-product")

        btn_element.click()
        sleep(3)

        btn_product_element.click()
        sleep(3)

        name_element = driver.find_element(By.NAME, "name")
        description_element = driver.find_element(By.NAME, "description")
        price_element = driver.find_element(By.NAME, "price")
        qty_element = driver.find_element(By.NAME, "qty")
        btn_added_product = driver.find_element(By.ID, "btn-added-product")

        name_element.clear()
        name_element.send_keys("Тест")
        sleep(2)

        description_element.clear()
        description_element.send_keys("Тест")
        sleep(2)

        price_element.clear()
        price_element.send_keys("50")
        sleep(2)

        qty_element.clear()
        qty_element.send_keys("10")
        sleep(2)

        btn_added_product.click()
        sleep(2)

        assert "Вы успешно создали товар" in driver.page_source
        sleep(3)

        driver.close()
