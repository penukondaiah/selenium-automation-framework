import logging

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from base.base_driver import BaseDriver
from utilities.utils import Utils


class searchflightResults(BaseDriver):
    log = Utils.cust_logger(loglevel=logging.WARNING)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    DOMESTIC_FLIGHT_FIELD = "flight_origin"
    def getdestingfromfield(self):
        return self.driver.find_element(By.NAME, self.DOMESTIC_FLIGHT_FIELD)

    def enterdestinationfromlocation(self, startingfrom):
        a = self.getdestingfromfield()
        a.click()
        a.send_keys(startingfrom)
        time.sleep(2)
        self.log.warning("special_page not completed")


