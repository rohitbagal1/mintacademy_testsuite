import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
s = Service("C:\\browser files\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.google.com")
driver.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin', 'tab2');")
windowlist = driver.window_handles
# switching to mint academy

driver.switch_to.window(windowlist[0])

# below all code is related to gmail opening upto verification code sending on mobile
driver.find_element(By.ID, "identifierId").send_keys("rohit.bagal@turtlemint.com")
driver.find_element(By.XPATH, "//button[@type='button']").click()
time.sleep(2)
driver.find_element(By.ID, "recoveryIdentifierId").click()
time.sleep(2)
driver.find_element(By.ID, "recoveryIdentifierId").send_keys("8329142239")
driver.find_element(By.XPATH, "//button[@type='button']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Rohit")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Bagal")
driver.find_element(By.XPATH, "//button[@type='button']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@type='button']").click()
driver.get_screenshot_as_file("screenshot1.png")
#(driver.get_screenshot_as_file("upload.png"))
driver.find_element(By.XPATH, "//ul[2]/li[i]").get_attribute("class")

