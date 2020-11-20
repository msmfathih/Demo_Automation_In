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

    def test_enter_valid_password(self):
        self.driver.get(TestData.BASE_URL)
        self.driver.implicitly_wait(15)

        self.lp = LoginPage(self.driver)
        self.lp.enter_valid_email(TestData.USERNAME),time.sleep(1)
        self.lp.press_index_login()

        verifyPageName = self.driver.find_element(By.XPATH, "//h1[contains(text(),'Automation Demo Site')]")
        if verifyPageName is not None:
            print("Verified Page Name")
        else:
            print("Page name is not verified")

        act_title = self.driver.title
        if act_title =="Register":
            assert True
        else:
            assert False

        link = None
        while not link:
            try:
                link = self.driver.find_element_by_xpath("//h2[contains(text(),'Register')]")
                print("verified register title")
            except NoSuchElementException:
                time.sleep(2)

        act_current_url = self.driver.current_url
        if act_current_url =="http://demo.automationtesting.in/Register.html":
            assert True
        else:
            assert False

    def test_alert_page(self):
        self.ap = AlertPage(self.driver)
        self.ap.navigate_switch_page()
        self.ap.navigate_alert_page(),time.sleep(5)
        self.ap.click_on_ok_alert(),time.sleep(5)
        self.ap.click_on_cancel_alert(),time.sleep(5)
        self.ap.alert_textbox(),time.sleep(3)

    def test_mouse_hover(self):
        self.mh = MouseHover(self.driver)
        self.mh.navigate_interaction()
        self.mh.navigate_dragdrop()
        self.mh.navigate_static()

