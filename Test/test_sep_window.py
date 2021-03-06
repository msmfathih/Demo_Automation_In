import time
import pytest
from Configuration.conftest import init_driver
from selenium import webdriver
from Pages.window_page import WindowPage
from TestData.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_SepWindowPage(BaseTest):

    def test_window_handler2(self):
        self.driver.get(TestData.WINDOWS_PAGE_URL)
        self.wp = WindowPage(self.driver)
        self.wp.click_seperate_window(),time.sleep(3)
        self.driver.quit()





