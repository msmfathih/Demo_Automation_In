from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.Locators import Locators
from TestData.config import TestData


class RegisterPage():

    def __init__(self, driver):
        self.driver = driver

        self.enter_first_name_xpath = Locators.FIRST_NAME_XPATH
        self.enter_last_name_xpath = Locators.LAST_NAME_XPATH
        self.enter_address_xpath = Locators.ADDRESS_XPATH
        self.enter_email_address_xpath = Locators.EMAIL_ADDRESS_XPATH
        self.enter_phone_number_xpath = Locators.PHONE_NUMBER_XPATH

        self.select_gender_name = Locators.GENDER_NAME
        self.select_hobby_id1 = Locators.HOBBY1_ID
        self.select_hobby_id2 = Locators.HOBBY2_ID
        self.select_language = Locators.LANGUAGE_DROPDOWN_ID
        self.select_skills_id = Locators.SKILL_ID

        self.select_country_id = Locators.COUNTRY_ID
        self.select_dob_year_id = Locators.DOB_YEAR_ID
        self.select_dob_month_xpath = Locators.DOB_MONTH_XPATH
        self.select_dob_date_id = Locators.DOB_DATE_ID
        self.upload_profile_picture = Locators.UPLOAD_PROFILE_PICTURE_ID

        self.set_password_id = Locators.SET_PASSWORD_ID
        self.confirm_password_id = Locators.CONFIRM_PASSWORD_ID
        self.submit_button_id = Locators.SUBMIT_BUTTON_ID

    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.enter_first_name_xpath).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.enter_last_name_xpath).send_keys(lastname)

    def enter_address(self, address):
        self.driver.find_element(By.XPATH, self.enter_address_xpath).send_keys(address)

    def enter_email_address(self, email):
        self.driver.find_element(By.XPATH, self.enter_email_address_xpath).send_keys(email)

    def enter_phone_number(self, phone):
        self.driver.find_element(By.XPATH, self.enter_phone_number_xpath).send_keys(phone)

    def select_gender(self):
        #self.driver.find_element(By.NAME, self.select_gender_name).click()
        try:
            elem = self.driver.find_element(By.NAME, self.select_gender_name)
            if elem.is_displayed():
                elem.click()
                print("FOUND THE ELEMENT CREATE ACTIVITY! and Clicked it!")
        except NoSuchElementException:
            print("Element not clickable")

    def select_hobby(self):
        self.driver.find_element(By.ID, self.select_hobby_id1).click()
        self.driver.find_element(By.ID, self.select_hobby_id2).click()

    def select_language_dropdown(self):
        self.driver.find_element(By.ID, Locators.LANGUAGE_DROPDOWN_ID).click()
        drop_list = self.driver.find_elements(By.CSS_SELECTOR, 'a.ui-corner-all')
        for ele in drop_list:
            print(ele.text)
            if ele.text == TestData.DROPDOWN_LANGUAGE:
                ele.click()
                break
            for ele in drop_list:
                print(ele.text)
                if ele.text == TestData.DROPDOWN_LANGUAGE2:
                    ele.click()
                    break

    def select_skills(self):
        dropdown = self.driver.find_element(By.ID, self.select_skills_id)
        select1 = Select(dropdown)
        select1.select_by_index(2)
        time.sleep(2)

    def select_country(self):
        dropdown = self.driver.find_element(By.ID, self.select_country_id)
        select2 = Select(dropdown)
        select2.select_by_visible_text("Australia")
        time.sleep(2)

    def select_dob(self):
        element1 = self.driver.find_element_by_id(Locators.DOB_YEAR_ID)
        ele = Select(element1)
        ele.select_by_visible_text("1991")
        element1 = self.driver.find_element(By.XPATH, Locators.DOB_MONTH_XPATH)
        sel = Select(element1)
        sel.select_by_visible_text("November")
        element1 = self.driver.find_element(By.ID, Locators.DOB_DATE_ID)
        sel = Select(element1)
        sel.select_by_index(14)

    def upload_profile_image(self, profile_picture):
        self.driver.find_element(By.ID, self.upload_profile_picture).send_keys(profile_picture)

    def submit_password(self, password):
        self.driver.find_element(By.ID, self.set_password_id).send_keys(password)

    def confirm_password(self,confirm_password):
        self.driver.find_element(By.ID, self.confirm_password_id).send_keys(confirm_password)

    def press_submit(self):
        self.driver.find_element(By.ID, self.submit_button_id).click()








