import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object.grow_page import MintGrowPage


class EnterNameEmailPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.name_field_locator = "//input[@placeholder='Enter your full name']"
        self.email_field_locator = "//input[@placeholder='Enter your email address']"
        self.create_account_locator = "//div[@class='formActionWrapper _turtlemint_action_button']"

    def enter_dp_name(self, name):
        # enter name
        self.driver.find_element(By.XPATH, self.name_field_locator).send_keys(name)
        time.sleep(1)

    def enter_dp_email(self, email):
        # enter mail id
        self.driver.find_element(By.XPATH, self.email_field_locator).send_keys(email)
        time.sleep(1)

    def click_create_account_button(self):
        # click on create account button
        self.driver.find_element(By.XPATH, self.create_account_locator).click()
        time.sleep(10)

    def perform_email_name_entering_activities(self):
        self.enter_dp_name()
        self.enter_dp_email()
        self.click_create_account_button()
        grow = MintGrowPage(self.driver, self.wait)
        return grow
