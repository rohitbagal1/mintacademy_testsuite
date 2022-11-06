import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object.mintpro_profile_page import MintProfilePage


class MintGrowPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.red_dot_path = "//span[@class='notify']"

    def click_on_profile(self):
        # click on profile for filling up details having red dot
        self.driver.find_element(By.XPATH, self.red_dot_path).click()
        time.sleep(1)
        profile = MintProfilePage(self.driver, self.wait)
        return profile