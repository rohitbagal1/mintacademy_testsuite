import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class BusinessDetailsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.income_drop_down_locator = "primarySourceOfIncome"
        self.experience_drop_down_locator = "insuranceExperienceInYears"

    def select_dp_source_of_income_from_drop_down(self, income_source):
        # landing on business information page and selecting primary source of income
        # attaching variable to income drop down web element
        income = self.driver.find_element(By.NAME, self.income_drop_down_locator)
        # using select class
        income_select = Select(income)
        # create income source list
        income_source_list = income_select.options
        # printing all income source option with names and no
        print("ALL INCOME SOURCES OPTIONS ARE", len(income_source_list) - 1)
        # for loop to select particular option from drop down
        for i in income_source_list:
            print(i.text)
            if i.text == income_source:
                i.click()

    def select_years_of_exp_from_drop_down(self, years):
        # selecting from experience drop down, giving variable to exp drop down web element
        exp = self.driver.find_element(By.NAME, self.experience_drop_down_locator)
        # using select class for exp web element
        expselect = Select(exp)
        # creating exp list
        explist = expselect.options
        # printing all no of experience option present in drop down
        print("ALL EXPERIENCE DROP DOWN OPTION NO", len(explist) - 1)
        # for loop for selecting particular option
        for i in explist:
            print(i.text)
            if i.text == years:
                i.click()
        time.sleep(3)

    def click_on_update_dp_education_details(self):
        # click on update button
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()