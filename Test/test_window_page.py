import time
import pytest
from Configuration.conftest import init_driver
from selenium import webdriver
from Pages.window_page import WindowPage
from TestData.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_WindowPage(BaseTest):

    def test_window_handler(self):
        self.driver.get(TestData.WINDOWS_PAGE_URL)
        self.wp = WindowPage(self.driver)
        self.wp.click_multi_window()
        #self.driver.quit()























