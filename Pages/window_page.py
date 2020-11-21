import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
import pytest

class WindowPage():

    def __init__(self, driver):
        self.driver = driver

        self.click_window_button_xpath = Locators.TABBED_CLICK_WINDOW_XPATH
        self.click_seperate_window_xpath = Locators.SEPERATE_WINDOW_XPATH
        self.click_seperate_button_window_xpath = Locators.SEPERATE_CLICK_BUTTON_XPATH
        self.click_multiple_window_xpath = Locators.SEPERATE_MULTIPLE_WINDOW_XPATH
        self.click_multiple_window_button_xpath = Locators.MULTI_WINDOW_CLICK_BUTTON_XPATH


    def click_window_button(self):
        self.driver.find_element(By.XPATH, self.click_window_button_xpath).click()
        print(self.driver.current_window_handle)  #CDwindow-3ABF0AC638485B233F933156AEEBA1C7 - parent window handlevalue

        handles = self.driver.window_handles #returns all the handle of opened windows
        for handle in handles:
            self.driver.switch_to.window(handle)
            print(self.driver.title)
            if self.driver.title=="SeleniumHQ Browser Automation": #parant window only close
                self.driver.close()

        # self.driver.close() #close only child window

    def click_seperate_window(self):
        self.driver.find_element(By.XPATH, self.click_seperate_window_xpath).click(),time.sleep(2)
        self.driver.find_element(By.XPATH, self.click_seperate_button_window_xpath).click()
        print(self.driver.current_window_handle)

        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            print(self.driver.title)
            if self.driver.title == "SeleniumHQ Browser Automation":
                self.driver.close()







    # def click_seperate_window_button(self):
    #     self.driver.find_element(By.XPATH, self.click_seperate_button_window_xpath).click()
    #
    # def click_multiple_window(self):
    #     self.driver.find_element(By.XPATH, self.click_multiple_window_xpath).click()
    #
    # def click_multiple_button(self):
    #     self.driver.find_element(By.XPATH, self.click_multiple_window_button_xpath).click()
    #
    #
    #





