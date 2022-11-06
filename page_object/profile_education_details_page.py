import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class EducationDetailsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.education_qualification_drop_down_locator = "educationQualification"
        self.education_proof_upload_locator = "//input[@id='educationQualificationFile']"

    def select_dp_education_type_from_drop_down(self, eduction_stream):
        # landing on education details page and selecting educational qualification from drop down
        # provide variable to dropdown web element
        edu = self.driver.find_element(By.NAME, self.education_qualification_drop_down_locator)
        # use select class and create variable
        eduselect = Select(edu)
        # create list of web elements that is edulist
        edulist = eduselect.options
        # print all education qualification options along with name
        print("TOTAL EDUCATION QUALIFICATION OPTIONS ARE", len(edulist) - 1)
        # use for loop to select user submitted option like SSC, HSC etc.
        for i in edulist:
            print(i.text)
            if i.text == eduction_stream:
                i.click()
                break

    def upload_dp_eduction_proof(self, proof):
        # upload education proof
        self.driver.find_element(By.XPATH, self.education_proof_upload_locator).send_keys(proof)
        time.sleep(8)

    def click_to_update_education_details(self):
        # click on update button
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()

    def perform_filing_upeducation_