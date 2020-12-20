from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
from selenium.webdriver import ActionChains


class AlertPage():

    def __init__(self, driver):
        self.driver = driver

        self.navigate_switch_to_xpath = Locators.SWITCH_TO_XPATH
        self.navigate_alert_page_xpath = Locators.ALERT_TO_XPATH
        self.alert_with_ok_xpath = Locators.ALERT_WITH_OK_XPATH
        self.alert_with_cancel_xpath = Locators.ALERT_WITH_OK_CANCEL_XPATH
        self.alert_cancel_button_xpath = Locators.ALERT_CANCEL_BUTTON_XPATH
        self.alert_textbox_xpath = Locators.ALERT_TEXTBOX_XPATH
        self.alert_textbox_field_xpath = Locators.ALERT_TEXTBOX_FIELD_XPATH

    def navigate_switch_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.navigate_switch_to_xpath)).perform()

    def navigate_alert_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.navigate_alert_page_xpath)).click().perform()

    def click_on_ok_alert(self):
        self.driver.find_element(By.XPATH, self.alert_with_ok_xpath).click()
        alert = self.driver.switch_to.alert
        print(alert.text),time.sleep(1)
        alert.accept()

    def click_on_cancel_alert(self):
        self.driver.find_element(By.XPATH, self.alert_with_cancel_xpath).click(),time.sleep(2)
        self.driver.find_element(By.XPATH, self.alert_cancel_button_xpath).click()
        alert = self.driver.switch_to.alert
        print(alert.text),time.sleep(2)
        alert.dismiss()

    def alert_textbox(self):
        self.driver.find_element(By.XPATH, self.alert_textbox_xpath).click(),time.sleep(2)
        self.driver.find_element(By.XPATH, self.alert_textbox_field_xpath).click()
        alert = self.driver.switch_to.alert
        alert.send_keys("Hi fathih")
        time.sleep(2)
        alert.accept()

















