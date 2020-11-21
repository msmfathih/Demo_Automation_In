from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
import pytest

class WindowPage():

    def __init__(self, driver):
        self.driver = driver

        self.navigate_switch_to_xpath = Locators.SWITCH_TO_XPATH
        self.hover_window_page_xpath = Locators.WINDOWS_PAGE_XPATH
        self.click_window_button_xpath = Locators.TABBED_CLICK_WINDOW_XPATH
        self.click_seperate_window_xpath = Locators.SEPERATE_WINDOW_XPATH
        self.click_seperate_button_window_xpath = Locators.SEPERATE_CLICK_BUTTON_XPATH
        self.click_multiple_window_xpath = Locators.SEPERATE_MULTIPLE_WINDOW_XPATH
        self.click_multiple_window_button_xpath = Locators.MULTI_WINDOW_CLICK_BUTTON_XPATH


    def navigate_switch_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.navigate_switch_to_xpath)).perform()

    def hover_window(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.hover_window_page_xpath)).click().perform()

    def click_window_button(self):
        self.driver.find_element(By.XPATH, self.click_window_button_xpath).click()

    def click_seperate_window(self):
        self.driver.find_element(By.XPATH, self.click_seperate_window_xpath).click()

    def click_seperate_window_button(self):
        self.driver.find_element(By.XPATH, self.click_seperate_button_window_xpath).click()

    def click_multiple_window(self):
        self.driver.find_element(By.XPATH, self.click_multiple_window_xpath).click()

    def click_multiple_button(self):
        self.driver.find_element(By.XPATH, self.click_multiple_window_button_xpath).click()








