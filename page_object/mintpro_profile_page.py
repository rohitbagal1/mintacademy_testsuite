import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object.profile_pancard_page import PanCardDetailsPage


class MintProfilePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.verification_status_locator = "//span[normalize-space()='Verification pending']"

    def get_current_verification_status(self):
        # get verification pending text
        verification_status = self.driver.find_element(By.XPATH, self.verification_status_locator).text
        print(verification_status)
        time.sleep(3)

    def click_on_update(self):
        # clicking on red coloured update for filling up details.
        self.driver.find_element(By.XPATH, "//span[@class='section_status']").click()
        time.sleep(3)

    def perform_profile_page_activities(self):
        self.get_current_verification_status()
        self.click_on_update()
        pan = PanCardDetailsPage(self.driver, self.wait)
        return pan