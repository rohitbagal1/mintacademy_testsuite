import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class PersonnelDetailsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.profile_picture_upload_locator = "//input[@id='profilePicture']"
        self.status_text_locator = "//div[@class='leftTabWrapper']/ul[2]/h3"
        self.status_of_six_details_locator = "//ul[2]/li[i]"
        self.profile_section_locator = "//span[contains(text(),'Profile')]"

    def upload_dp_profile_picture(self, image):
        # landing personnel details page and uploading profile picture
        self.driver.find_element(By.XPATH, self.profile_picture_upload_locator).send_keys(image)
        time.sleep(8)

    def click_update_to_upload_personnel_details(self):
        # click on update button
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        time.sleep(3)

    def get_status_of_dp_after_uploading_all_details(self):
        # get under review status of dp as he has uploaded all documents
        dp_status = self.driver.find_element(By.XPATH, self.status_text_locator).text
        assert dp_status == "Completed - Under Review", \
            "assertion error because dp status should be Completed - Under Review"

    def getting_status_of_all_six_details(self):
        for i in range(1, 7):
            status = self.driver.find_element(By.XPATH, self.status_of_six_details_locator).get_attribute("class")
        assert status == "completed", "assertion error, Some details are not completed"

    def landing_back_to_profile_page(self):
        self.driver.find_element(By.XPATH, self.profile_section_locator).click()