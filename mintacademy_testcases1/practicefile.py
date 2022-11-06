from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="C:\\browser files\\chromedriver.exe", chrome_options=opt)
driver.get("https://www.mintpro.in")
driver.maximize_window()
print(driver.title)
driver.find_element(By.XPATH, "//*[@id='menu-item-44']/a").click()
driver.find_element(By.CLASS_NAME, "jss109").click()
driver.find_element(By.NAME, "mobileNumber").send_keys("6999912345")
