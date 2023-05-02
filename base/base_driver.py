import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        time.sleep(2)
        self.driver.execute_script('window.scrollBy(0, 500)')
        time.sleep(2)
        self.driver.execute_script('window.scrollBy(0, -500)')
        time.sleep(2)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element


# some lines from sdet1

