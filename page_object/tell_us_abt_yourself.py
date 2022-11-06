import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object.name_email_page import EnterNameEmailPage


class AboutYourSelfPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.image_never_sold_locator = "//div[contains(text(),'We help you to learn more, earn more!')]"
        self.continue_button_locator = "//div[@class='loginPageBtn']"

    def click_first_image_never_sold(self):
        # clicking on first image that if dp is new
        self.driver.find_element(By.XPATH, self.image_never_sold_locator).click()
        time.sleep(2)

    def click_continue_button(self):
        # click on continue button
        self.driver.find_element(By.XPATH, self.continue_button_locator).click()
        time.sleep(2)

    def perform_about_page_related_activities(self):
        self.click_first_image_never_sold()
        self.click_continue_button()
        name_email = EnterNameEmailPage(self.driver, self.wait)
        return name_email