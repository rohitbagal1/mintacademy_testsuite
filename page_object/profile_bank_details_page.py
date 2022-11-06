import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object.profile_education_details_page import EducationDetailsPage


class BankDetailsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.check_book_image_locator = "//input[@id='bankPassbook']"
        self.bank_name_locator = "//input[@name='bankName']"
        self.account_holder_name_locator = "//input[@name='accHolderName']"
        self.bank_account_number_locator = "//input[@name='accNo']"
        self.ifsc_field_locator = "//input[@name='ifsccode']"

    def upload_bank_check_book_proof(self, proof):
        # after updating landing on bank details and uploading checkbook image
        self.driver.find_element(By.XPATH, self.check_book_image_locator).send_keys(proof)
        time.sleep(30)

    def enter_bank_name_of_dp(self, bank_name):
        # enter bank name
        self.driver.find_element(By.XPATH, self.bank_name_locator).send_keys(bank_name)
        time.sleep(4)

    def enter_account_holders_name(self, name):
        # enter account holder name
        self.driver.find_element(By.XPATH, self.account_holder_name_locator).clear()
        self.driver.find_element(By.XPATH, self.account_holder_name_locator).send_keys(name)
        time.sleep(4)

    def enter_bank_account_number(self, account_no):
        # enter account no
        self.driver.find_element(By.XPATH, self.bank_account_number_locator).clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.bank_account_number_locator).send_keys(account_no)

    def enter_ifsc_code_of_bank(self, code):
        # enter ifsc code
        self.driver.find_element(By.XPATH, self.ifsc_field_locator).send_keys(code)
        time.sleep(5)

    def click_update_to_upload_bank_details(self):
        # click on update button
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()

    def perform_bank_details_filing_up_activities(self):
        self.upload_bank_check_book_proof()
        self.enter_bank_name_of_dp()
        self.enter_account_holders_name()
        self.enter_bank_account_number()
        self.enter_ifsc_code_of_bank()
        self.click_update_to_upload_bank_details()
        education = EducationDetailsPage(self.driver, self.wait)
        return education