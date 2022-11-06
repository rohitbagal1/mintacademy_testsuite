import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object.profile_adhar_page import ADhaRCardDetailsPage


class PanCardDetailsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.pan_card_proof_upload_locator = "//input[@id='panCardNumberFile']"
        self.pan_number_field_locator = "documentNumber"
        self.dob_filed_locator = "dateOfBirth"

    def upload_pan_card_proof(self, address):
        # Upload image of pan card
        self.driver.find_element(By.XPATH, self.pan_card_proof_upload_locator).send_keys(address)
        time.sleep(5)

    def enter_pan_card_no(self, pan_number):
        # enter pan card no
        self.driver.find_element(By.NAME, self.pan_number_field_locator).send_keys(pan_number)

    def enter_birth_date(self, date):
        # enter the birth date
        self.driver.find_element(By.NAME, self.dob_filed_locator).send_keys(date)

    def click_to_upload_pan_details(self):
        # click on update button
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()

    def perform_pan_card_related_activities(self):
        self.upload_pan_card_proof()
        self.enter_pan_card_no()
        self.enter_birth_date()
        self.click_to_upload_pan_details()
        aadhar = ADhaRCardDetailsPage(self.driver, self.wait)
        return aadhar
