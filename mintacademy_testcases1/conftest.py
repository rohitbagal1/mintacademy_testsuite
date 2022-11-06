import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    # max window
    driver.maximize_window()
    # enter url
    driver.get("https://app.sanity.stage.mintpro.in/signup")
    # requesting driver object and wait object in other test class files because we have defined everything over fixture only
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()

