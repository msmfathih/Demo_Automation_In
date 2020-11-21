from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class MouseHover():

    def __init__(self, driver):
        self.driver = driver

        self.navigate_interaction_xpath = Locators.HOVER_INTERACTION_XPATH
        self.navigate_dragdrop_xpath = Locators.HOVER_DRAG_DROP_XPATH
        self.navigate_static_xpath = Locators.HOVER_STATIC_XPATH


    def navigate_interaction(self):
        ack = ActionChains(self.driver)
        ack.move_to_element(self.driver.find_element(By.XPATH, self.navigate_interaction_xpath)).perform()

    def navigate_dragdrop(self):
        ack = ActionChains(self.driver)
        ack.move_to_element(self.driver.find_element(By.XPATH, self.navigate_dragdrop_xpath)).perform()

    def navigate_static(self):
        ack = ActionChains(self.driver)
        ack.move_to_element(self.driver.find_element(By.XPATH, self.navigate_static_xpath)).click().perform()











