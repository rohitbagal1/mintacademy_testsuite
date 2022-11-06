import time
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
# opt = Options()
# opt.add_experimental_option("debuggerAddress", "localhost:8989")
# driver = webdriver.Chrome(executable_path="C:\\browser files\\chromedriver.exe", chrome_options=opt)
driver = webdriver.Chrome(ChromeDriverManager().install())
# max window
driver.maximize_window()
# wait implicit
driver.implicitly_wait(60)
# open ninja sanity website
driver.get("https://ninja.sanity.planturtle.com/")
# click on sign in link
#driver.find_element(By.XPATH, "//a[@id='google-signin-button']").click()
time.sleep(60)
# enter turtle mint mail id flow but afterwords
#driver.find_element(By.XPATH, "//input[@type='email']").send_keys("rohit.bagal@turtlemint.com")
# click on partner management
driver.find_element(By.XPATH, "//a[contains(text(),'Partner Management')]").click()
# enter mobile no in search field
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("6565656536")
# use action chain class to hit enter
act = ActionChains(driver)
act.send_keys(Keys.ENTER).perform()
# click on obtained result to verify account
driver.find_element(By.XPATH, "//td[@class='md-cell ng-binding']").click()
# add name of reporting manager
driver.find_element(By.XPATH, "//input[@name='reportingTo']").send_keys("kun")
# time delay to get suggestion on screen
time.sleep(4)
# after entering name getting list of web element
listofmanager= driver.find_elements(By.XPATH, "//li[@class='uib-typeahead-match ng-scope']")

# for loop for clicking on name
for i in listofmanager:
    print(i.text)
    if i.text == "kunal somani ( SalesManager ) ( 167277 )":
        i.click()
        break
# selecting business channel
driver.find_element(By.XPATH, "//md-select[@ng-model='ViewModel.businessChannelModel']").click()
time.sleep(3)
# select field sales option
driver.find_element(By.XPATH, "//md-option[@id='select_option_58']").click()
# filling up bank details, clicking relationship with partner
driver.find_element(By.XPATH, "//md-select[@name='relationship']").click()
time.sleep(5)
# clicking on self in relationship with partner
driver.find_element(By.XPATH, "//md-option[@id='select_option_10']").click()
# entering bank branch name
driver.find_element(By.XPATH, "//input[@name='branch']").send_keys("Solapur")
# clicking on validate bank details button
driver.find_element(By.XPATH, "//button[@class='md-raised add_posp_code md-button md-ink-ripple']").click()
time.sleep(10)
# clicking on manually verified bank details button
driver.find_element(By.XPATH, "//*[text()='Manual Verify']").click()
# clicking at broker in IRDI data base
driver.find_element(By.XPATH, "//md-select-value[@id='select_value_label_271']").click()
time.sleep(5)
# clicking on not associated at IRDI DATABASE
driver.find_element(By.XPATH, "//md-option[@id='select_option_274']").click()
# clicking at POSP status drop down
driver.find_element(By.XPATH, "//md-select[@name='eligibleForLMS']").click()
time.sleep(5)
# clicking on eligible option
driver.find_element(By.XPATH, "//md-option[@id='select_option_23']").click()
time.sleep(5)
# clicking on save changes button
driver.find_element(By.XPATH, "//*[text()='Save Changes']").click()
time.sleep(5)
# clicking on final pop window having button save changes to verify user or dp
driver.find_element(By.XPATH, "//*[@ng-click='saveChangesPartner()']").click()
time.sleep(300)