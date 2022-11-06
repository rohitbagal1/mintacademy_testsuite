import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object.profile_bank_details_page import BankDetailsPage


class ADhaRCardDetailsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.aadhar_image_upload_locator = "//input[@class='typeFile']"
        self.pin_code_locator = "//input[@name='pincode']"
        self.address_test_field_locator = "//input[@name='displayAddress']"
        self.male_radio_button_locator = "//span[@class='designRadio']"
        self.aadhar_number_field_locator = "documentNumber"

    def upload_front_aadhaar_card_proof(self, address):
        # front image upload
        self.driver.find_element(By.XPATH, self.aadhar_image_upload_locator).send_keys(address)
        time.sleep(5)

    def upload_back_aadhaar_proof(self, address):
        # back image upload
        self.driver.find_element(By.XPATH, self.aadhar_image_upload_locator).send_keys(address)
        time.sleep(7)

    def enter_pin_code_of_dp(self,pin_code_number):
        # enter pincode
        self.driver.find_element(By.XPATH, self.pin_code_locator).send_keys(pin_code_number)
        time.sleep(3)

    def enter_address_of_dp(self, location):
        # enter address
        self.driver.find_element(By.XPATH, self.address_test_field_locator).send_keys(location)
        time.sleep(3)

    def select_radio_button_as_male(self):
        # select radio button for male
        self.driver.find_element(By.XPATH, self.male_radio_button_locator).click()
        time.sleep(3)

    def enter_aadhaar_number_of_dp(self, aadhaar_number):
        # enter Aadhaar no
        self.driver.find_element(By.NAME, self.aadhar_number_field_locator).send_keys(aadhaar_number)
        time.sleep(3)

    def click_to_update_aadhaar_details(self):
        # click on update button
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        time.sleep(5)

    def perform_aadhar_card_activities(self):
        self.upload_front_aadhaar_card_proof()
        self.upload_back_aadhaar_proof()
        self.enter_pin_code_of_dp()
        self.enter_address_of_dp()
        self.select_radio_button_as_male()
        self.enter_aadhaar_number_of_dp()
        self.click_to_update_aadhaar_details()
        bank = BankDetailsPage(self.driver, self.wait)
        return bank