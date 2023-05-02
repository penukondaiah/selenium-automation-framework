import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from base.base_driver import BaseDriver



class Launchpage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    STARTING_FLIGHT_FIELD = "flight_origin"
    ORIGIN_FLIGHT_FIELD = "flight_destination"
    ORIGIN_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    CLICK_YATRA = "//img[@alt='Flat 16% OFF (up to Rs. 2,000)']"

    def getStartingFromField(self):
        return self.driver.find_element(By.NAME, self.STARTING_FLIGHT_FIELD)

    def getOriginToField(self):
        return self.driver.find_element(By.NAME, self.ORIGIN_FLIGHT_FIELD)

    def getOriginToResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ORIGIN_TO_RESULT_LIST)

    def getStartingdateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def getClickYatraButton(self):
        return self.driver.find_element(By.XPATH, self.CLICK_YATRA)

    def enterStartingFromLocation(self, startinglocation):
        self.getStartingFromField().click()
        time.sleep(4)
        self.getStartingFromField().send_keys(startinglocation)
        self.getStartingFromField().send_keys(Keys.ENTER)
        time.sleep(3)

    def enterOriginToLocation(self, OriginToLocation):
        self.getOriginToField().click()
        time.sleep(3)
        self.getOriginToField().send_keys(OriginToLocation)
        check_details = self.getOriginToResults()
        for details in check_details:
            if OriginToLocation in details.text:
                time.sleep(5)
                details.click()
                time.sleep(5)
                break

    def enterStartingdate(self, startingdate):
        self.getStartingdateField().click()
        Date_check = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES)
        for Date in Date_check:
            if Date.get_attribute("data-date") == startingdate:
                Date.click()
                time.sleep(6)
                break

    def enteryatraspecial(self):
        self.getClickYatraButton().click()
        time.sleep(2)
        all_handlers = self.driver.window_handles
        self.driver.switch_to.window(all_handlers[1])

        time.sleep(2)

    def searchFlights(self, startinglocation, OriginToLocation, startingdate):
        self.enterStartingFromLocation(startinglocation)
        self.enterOriginToLocation(OriginToLocation)
        self.enterStartingdate(startingdate)
        self.enteryatraspecial()
