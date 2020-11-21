import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
from Configuration.conftest import init_driver
from selenium import webdriver
from Pages.login_Page import LoginPage
from Pages.mouse_Hover_Page import MouseHover
from Pages.window_page import WindowPage
from TestData.config import TestData

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_loginPage(BaseTest):

    def test_login(self):

        self.driver.get(TestData.BASE_URL)
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.enter_valid_email(TestData.USERNAME), time.sleep(1)
        self.lp.press_index_login()

        self.wp = WindowPage(self.driver)
        self.wp.navigate_switch_page(),time.sleep(2)
        self.wp.hover_window(),time.sleep(2)
        self.wp.click_window_button(),time.sleep(2)
        self.wp.click_seperate_window(),time.sleep(2)
        self.wp.click_seperate_window_button(),time.sleep(2)

        #self.wp.click_multiple_button(),time.sleep
























