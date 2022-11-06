import pickle
import time
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# open sanity ninja website for verifying dp
driver.get("https://ninja.sanity.planturtle.com/login")
# click on google sign in link
time.sleep(10)
#pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(5)
driver.find_element(By.XPATH, "//img[@src='images/google-dark.svg']").click()
time.sleep(10)