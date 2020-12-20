from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
import pytest

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.signin_button_id = Locators.SINGIN_BUTTON_ID
        self.enter_username_xpath = Locators.USERNAME_XPATH
        self.enter_password_xpath = Locators.PASSWORD_XPATH
        self.press_login_button_id = Locators.LOGIN_BUTTON_ID
        self.enter_valid_email_id = Locators.VALID_EMAIL_ID
        self.click_login_button_id = Locators.INDEX_LOGIN_BUTTON_ID

    def click_on_signin_button(self):
        #self.driver.find_element(By.ID, self.signin_button_id).click()
        try:
            elem = self.driver.find_element(By.ID, self.signin_button_id)
            if elem.is_displayed():
                elem.click()
                print("FOUND THE ELEMENT CREATE ACTIVITY! and Clicked it!")
        except NoSuchElementException:
            print("Element not clickable")

    def enter_username(self, username):
        #self.driver.find_element(By.XPATH, self.enter_username_xpath).send_keys(username)
        try:
            elem = self.driver.find_element(By.XPATH, self.enter_username_xpath)
            if elem.is_displayed():
                elem.send_keys(username)
                print("FOUND THE ELEMENT CREATE ACTIVITY! and Clicked it!")
        except NoSuchElementException:
            print("Element not clickable")

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.enter_password_xpath).send_keys(password)

    def press_login_button(self):
        self.driver.find_element(By.ID, self.press_login_button_id).click()

    def enter_valid_email(self, email):
        #self.driver.find_element(By.ID, self.enter_valid_email_id).send_keys(email)
        try:
            elem = self.driver.find_element(By.ID, self.enter_valid_email_id)
            if elem.is_displayed():
                elem.send_keys(email)
                print("Entered valid email id")
        except NoSuchElementException:
            print("Entered invalid email id")

    def press_index_login(self):
        try:
            element = self.driver.find_element(By.ID, self.click_login_button_id)
            if element.is_displayed():
                element.click()
            return True
        except:
            return False






























