from django.test import TestCase
from costumerapp.utils import get_driver

from django.test import TestCase
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from costumerapp.utils import get_driver


class CostumerTestCase(TestCase):
    def test_news(self):
        driver = get_driver()
        driver.get("http://localhost:8000/")
        sleep(1)
        btn_element = driver.find_element(By.ID, "drop-info")
        btn_news_element = driver.find_element(By.ID, "btn-news")

        btn_element.click()
        sleep(3)

        btn_news_element.click()
        sleep(3)

        title_element = driver.find_element(By.NAME, "new_title")
        article_element = driver.find_element(By.NAME, "new_article")
        btn_added_news = driver.find_element(By.ID, "btn-added-news")

        title_element.clear()
        title_element.send_keys("test")
        sleep(2)

        article_element.clear()
        article_element.send_keys("Тест")
        sleep(2)

        btn_added_news.click()
        sleep(2)

        assert "Вы успешно создали новость" in driver.page_source
        sleep(3)

        driver.close()