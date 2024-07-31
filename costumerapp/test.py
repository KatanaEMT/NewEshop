from django.test import TestCase

from django.test import TestCase
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .utils import get_driver


class CostumerTestCase(TestCase):
    def test_profile(self):
        driver = get_driver()
        driver.get("http://localhost:8000/")
        sleep(1)
        btn_element = driver.find_element(By.ID, "drop-info")
        btn_profile_element = driver.find_element(By.ID, "btn-profile")

        btn_element.click()
        sleep(3)

        btn_profile_element.click()
        sleep(3)

        bio_element = driver.find_element(By.NAME, "bio")
        social_link_element = driver.find_element(By.NAME, "social_link")
        phone_number_element = driver.find_element(By.NAME, "phone_number")
        btn_added_profile = driver.find_element(By.ID, "btn-added-profile")

        bio_element.clear()
        bio_element.send_keys("test")
        sleep(2)

        social_link_element.clear()
        social_link_element.send_keys("test")
        sleep(2)

        phone_number_element.clear()
        phone_number_element.send_keys("999")
        sleep(2)

        btn_added_profile.click()
        sleep(2)

        assert "Вы успешно создали профиль" in driver.page_source
        sleep(3)

        driver.close()