import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object.tell_us_abt_yourself import AboutYourSelfPage


class MobilePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.continue_button_locator = "//button[@type='button']"
        self.mobile_number_field_locator = "//input[@placeholder='Enter Your Mobile Number']"

    def check_disabled_cont_button(self):
        # check button is disabled or not
        value = self.driver.find_element(By.XPATH, self.continue_button_locator).get_attribute("class")
        print(value)

    def enter_mobile_no(self, mobile_no):
        # enter mobile number
        self.driver.find_element(By.XPATH, self.mobile_number_field_locator).send_keys(mobile_no)
        time.sleep(3)

    def click_on_cont_button(self):
        # click on continue button
        self.driver.find_element(By.XPATH, self.continue_button_locator).click()
        # entering otp
        time.sleep(60)

    def perform_mobile_no_entering_activities(self):
        self.check_disabled_cont_button()
        self.enter_mobile_no()
        self.click_on_cont_button()
        about = AboutYourSelfPage(self.driver, self.wait)
        return about
