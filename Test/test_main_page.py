import time
import pytest
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
from Configuration.conftest import init_driver
from selenium import webdriver
from Pages.mouse_Hover_Page import MouseHover
from TestData.config import TestData
from Pages.login_Page import LoginPage
from Pages.alert_page import AlertPage
from Pages.register_page import RegisterPage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import ElementNotSelectableException

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_loginPage(BaseTest):

    @pytest.mark.run(order=1)
    def test_login(self):
        self.driver.get(TestData.BASE_URL)
        self.driver.implicitly_wait(10)
        try:
            assert "Index" in self.driver.title
            print("Title is printed")
        except Exception as e:
            print("Title is not printed", format(e))
        try:
            assert "demo" in self.driver.current_url
            print("Current title is printed")
        except (TimeoutException, NoSuchElementException) as e:
            print("Current title is not printed", format(e))
        try:
            self.driver.find_element_by_xpath("//button[@id='btn1']").is_enabled()
            print("button is enable")
        except (ElementNotSelectableException,InvalidSelectorException) as e:
            print("button not enable")

        self.lp = LoginPage(self.driver)
        self.lp.click_on_signin_button(),time.sleep(1)
        self.lp.enter_username(TestData.USERNAME),time.sleep(1)
        self.lp.enter_password(TestData.PASSWORD),time.sleep(1)
        self.lp.press_login_button()

        verify_invalid_user = self.driver.find_element(By.XPATH, Locators.VERIFY_WRONG_EMAIL_XPATH)
        assert verify_invalid_user.text == Locators.VERIFY_EMAIL_MESSAGE
        self.driver.back()

    @pytest.mark.run(order=2)
    def test_enter_valid_password(self):
        self.lp = LoginPage(self.driver)
        self.lp.enter_valid_email(TestData.USERNAME),time.sleep(1)
        self.lp.press_index_login()

        verifyPageName = self.driver.find_element(By.XPATH, "//h1[contains(text(),'Automation Demo Site')]")
        if verifyPageName is not None:
            print("Verified Page Name")
        else:
            print("Page name is not verified")
        link = None
        while not link:
            try:
                link = self.driver.find_element_by_xpath("//h2[contains(text(),'Register')]")
                print("verified register title")
            except NoSuchElementException:
                time.sleep(2)

    @pytest.mark.run(order=3)
    def test_register_form(self):
        self.rf = RegisterPage(self.driver)
        self.rf.enter_firstname(TestData.FIRST_NAME),time.sleep(2)
        self.rf.enter_lastname(TestData.LAST_NAME)
        self.rf.upload_profile_image(TestData.FILE_UPLOAD_PATH)
        self.rf.enter_address(TestData.ADDRESS)
        self.rf.enter_email_address(TestData.ENTER_VALID_EMAIL_ID)
        self.rf.enter_phone_number(TestData.ENTER_PHONE_NUMBER)
        self.driver.execute_script("window.scrollBy(0,200)", "")
        self.rf.select_gender(),time.sleep(1)
        self.rf.select_hobby()
        self.rf.select_language_dropdown()
        self.rf.select_skills()
        self.rf.select_country()
        #self.rf.select_dob()
        verify_dob_year = self.rf.select_dob()
        if verify_dob_year is not None:
            print("bod year element selected")
        else:
            print("bod year element is not selected")

        self.rf.submit_password(TestData.SUBMIT_PASSWORD)
        self.rf.confirm_password(TestData.CONFIRM_SUBMIT_PASSWORD)
        self.rf.press_submit()









































