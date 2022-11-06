import time
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="C:\\browser files\\chromedriver.exe", chrome_options=opt)
# maximize window
driver.maximize_window()
# adding implicit wait of 20 sec because of slow loading
driver.implicitly_wait(60)
# opening url
driver.get("https://app.sanity.stage.mintpro.in/grow")
# click on login
driver.find_element(By.XPATH, "//span[@class='jss214']").click()

# print(driver.find_element(By.XPATH, "//div[@class='loginPageBtn']").is_enabled())
# enter admin mobile no
driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("6868686863")
# click on continue button after entering mobile no of admin

driver.find_element(By.XPATH, "//button[@type='button']").click()

# sleep

time.sleep(30)

# enter otp manually
# click on verify otp button after sleep done automatically

driver.find_element(By.XPATH, "//button[@type='button']").click()
time.sleep(45)

# click on notify button of profile that is red dot to open profile

driver.find_element(By.XPATH, "//span[@class='notify']").click()

# click on get free certification or training link to proceed

#driver.find_element(By.XPATH,"//*[text()='Get free certifications here']").click()

# click on go to turtle mint academy link

#driver.find_element(By.XPATH, "//a[@class='gotomint']").click()
# click to profile update with red color to upload document
driver.find_element(By.XPATH, "//span[@class='section_status']").click()
# click on upload pan card or upload image address of image is given to variable
adr = "C:\\Users\\user\\Pictures\\Screenshots\\xyz.png"
driver.find_element(By.XPATH, "//input[@id='panCardNumberFile']").send_keys(adr)
time.sleep(5)

# enter pan card no
driver.find_element(By.NAME, "documentNumber").send_keys("BHEPB9994A")
# enter the birth date
driver.find_element(By.NAME, "dateOfBirth").send_keys("19111988")
# click on update button
time.sleep(3)
driver.find_element(By.XPATH, "//button[@type='button']").click()
# upload adhar card front and back image use same image, used for pan
# front image upload
driver.find_element(By.XPATH, "//input[@class='typeFile']").send_keys(adr)
time.sleep(5)
# back image upload
driver.find_element(By.XPATH, "//input[@class='typeFile']").send_keys(adr)
time.sleep(7)

# enter pincode
driver.find_element(By.XPATH, "//input[@name='pincode']").send_keys("413229")
time.sleep(3)
# enter address
driver.find_element(By.XPATH, "//input[@name='displayAddress']").send_keys("times square")
time.sleep(3)
# select radio button for male
driver.find_element(By.XPATH, "//span[@class='designRadio']").click()
time.sleep(3)
# enter adhar no
driver.find_element(By.NAME, "documentNumber").send_keys("111111111117")
time.sleep(3)
# click on update button
driver.find_element(By.XPATH, "//button[@type='button']").click()
time.sleep(5)
# after updating landing on bank details and uploading checkbook image
driver.find_element(By.XPATH, "//input[@id='bankPassbook']").send_keys(adr)
time.sleep(30)
# enter bank name
driver.find_element(By.XPATH, "//input[@name='bankName']").send_keys("ICICI")
time.sleep(4)
# enter account holder name
driver.find_element(By.XPATH, "//input[@name='accHolderName']").send_keys("rohit bagal")
time.sleep(4)
# enter account no
driver.find_element(By.XPATH, "//input[@name='accNo']").clear()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='accNo']").send_keys("52478614778524")
# enter ifci code
driver.find_element(By.XPATH, "//input[@name='ifsccode']").send_keys("ICIC0000123")
time.sleep(5)
# click on update button
driver.find_element(By.XPATH, "//button[@type='button']").click()
# landing on education details page and selecting educational qualification from drop down
# provide variable to dropdown web element
edu = driver.find_element(By.NAME, "educationQualification")
# use select class and create variable
eduselect = Select(edu)
# create list of web elements that is edulist
edulist = eduselect.options
# print all education qualification options along with name
print("TOTAL EDUCATION QUALIFICATION OPTIONS ARE", len(edulist)-1)
# use for loop to select user submitted option like SSC, HSC etc.
for i in edulist:
    print(i.text)
    if i.text == "Post Graduation":
        i.click()
        break
# upload education proof
driver.find_element(By.XPATH, "//input[@id='educationQualificationFile']").send_keys(adr)
time.sleep(8)
# click on update button
driver.find_element(By.XPATH, "//button[@type='button']").click()
# landing on business information page and selecting primary source of income.
# attaching variable to income drop down web element
income = driver.find_element(By.NAME, "primarySourceOfIncome")
# using select class
incomeselect = Select(income)
# create income source list
incomesourcelist = incomeselect.options
# printing all income source option with names and no
print("ALL INCOME SOURCES OPTIONS ARE", len(incomesourcelist)-1)
# for loop to select particular option from drop down
for i in incomesourcelist:
    print(i.text)
    if i.text == "Other":
        i.click()
# selecting from experience drop down, giving variable to exp drop down web element
exp = driver.find_element(By.NAME, "insuranceExperienceInYears")
# using select class for exp web element
expselect = Select(exp)
# creating exp list
explist = expselect.options
# printing all no of experience option present in drop down
print("ALL EXPERINCE DROP DOWN OPTION NO", len(explist)-1)
# for loop for selecting particular option
for i in explist:
    print(i.text)
    if i.text == "Fresher":
        i.click()
# click on update button
time.sleep(3)
driver.find_element(By.XPATH, "//button[@type='button']").click()
# landing personnel details page and uploading profile picture
driver.find_element(By.XPATH, "//input[@id='profilePicture']").send_keys(adr)
# click on update button
time.sleep(8)
driver.find_element(By.XPATH, "//button[@type='button']").click()







