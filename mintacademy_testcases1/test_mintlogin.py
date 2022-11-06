import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# s = Service("C:\\browser files\\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
from page_object.mintpro_signup_page import SignupPage
from page_object.verify_mob_page import MobilePage
from page_object.tell_us_abt_yourself import AboutYourSelfPage
from page_object.name_email_page import EnterNameEmailPage
from page_object.grow_page import MintGrowPage
from page_object.mintpro_profile_page import MintProfilePage
from page_object.profile_pancard_page import PanCardDetailsPage
from page_object.profile_adhar_page import ADhaRCardDetailsPage
from page_object.profile_bank_details_page import BankDetailsPage
from page_object.profile_education_details_page import EducationDetailsPage
from page_object.bussines_information_page import BusinessDetailsPage
from page_object.profile_personel_details_page import PersonnelDetailsPage


@pytest.mark.usefixtures("setup")
class TestMintLogin:
    def test_mint_login(self):
        signup = SignupPage(self.driver, self.wait)
        # mobile = MobilePage(self.driver, self.wait)
        # about = AboutYourSelfPage(self.driver, self.wait)
        # name_email = EnterNameEmailPage(self.driver, self.wait)
        # grow = MintGrowPage(self.driver, self.wait)
        # profile = MintProfilePage(self.driver, self.wait)
        # pan = PanCardDetailsPage(self.driver, self.wait)
        # aadhar = ADhaRCardDetailsPage(self.driver, self.wait)
        # bank = BankDetailsPage(self.driver, self.wait)
        # education = EducationDetailsPage(self.driver, self.wait)
        business = BusinessDetailsPage(self.driver, self.wait)
        personnel = PersonnelDetailsPage(self.driver, self.wait)
        # signup.page_title()
        # signup.click_on_login()
        mobile = signup.perform_signup_activities()
        about = mobile.perform_mobile_no_entering_activities()
        name_email = about.perform_about_page_related_activities()
        grow = name_email.perform_email_name_entering_activities()
        # mobile.check_disabled_cont_button()
        # mobile.enter_mobile_no("6565656538")
        # mobile.click_on_cont_button()
        # about.click_first_image_never_sold()
        # about.click_continue_button()
        # name_email.enter_dp_name("test nine")
        # name_email.enter_dp_email("test.nine@gmail.com")
        # name_email.click_create_account_button()
        profile = grow.click_on_profile()
        pan = profile.perform_profile_page_activities()
        aadhar = pan.perform_pan_card_related_activities()
        # profile.get_current_verification_status()
        # profile.click_on_update()
        # file address for uploading image at different section.
        self.adr = "C:\\Users\\user\\PycharmProjects\\Mint_academy_testsuits\\testdata\\broken.png"
        # pan.upload_pan_card_proof(self.adr)
        # pan.enter_pan_card_no("BHEPB9998A")
        # pan.enter_birth_date("19111988")
        # pan.click_to_upload_pan_details()
        bank = aadhar.perform_aadhar_card_activities()
        education = bank.perform_bank_details_filing_up_activities()
        # aadhar.upload_front_aadhaar_card_proof(self.adr)
        # aadhar.upload_back_aadhaar_proof(self.adr)
        # aadhar.enter_pin_code_of_dp("413229")
        # aadhar.enter_address_of_dp("times square")
        # aadhar.select_radio_button_as_male()
        # aadhar.enter_aadhaar_number_of_dp("111111111121")
        # aadhar.click_to_update_aadhaar_details()
        # bank.upload_bank_check_book_proof(self.adr)
        # bank.enter_bank_name_of_dp("ICICI")
        # bank.enter_account_holders_name("rohit bagal")
        # bank.enter_bank_account_number("52478614778524")
        # bank.enter_ifsc_code_of_bank("ICIC0000123")
        # bank.click_update_to_upload_bank_details()
        education.select_dp_education_type_from_drop_down("Post Graduation")
        education.upload_dp_eduction_proof(self.adr)
        education.click_to_update_education_details()
        business.select_dp_source_of_income_from_drop_down("Other")
        business.select_years_of_exp_from_drop_down("Fresher")
        business.click_on_update_dp_education_details()
        personnel.upload_dp_profile_picture(self.adr)
        personnel.click_update_to_upload_personnel_details()
        personnel.get_status_of_dp_after_uploading_all_details()
        personnel.getting_status_of_all_six_details()
        personnel.landing_back_to_profile_page()
        # new tab
        # self.driver.execute_script("window.open('https://app.sanity.stage.mintpro.in/signup', 'tab2');")
        # time.sleep
        # in base package will define all methods that required in all pages so will inerite that class in all page class


