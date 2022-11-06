import time
import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object.verify_mob_page import MobilePage


class SignupPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.login_button_xpath = "//div[@class='slick-slide slick-active slick-current']//div//div[@class='sliderWrapper']//div//button[@type='button']"

    def page_title(self):
        # get title of page
        print(self.driver.title)

    def click_on_login(self):
        # click on login
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def perform_signup_activities(self):
        self.page_title()
        self.click_on_login()
        mobile = MobilePage(self.driver, self.wait)
        return mobile


