import time
from selenium.webdriver.common.by import By
import pytest
from pages.yatra_launch_page import Launchpage
from pages.yatra_special_page import searchflightResults
from utilities import utils
from utilities.utils import Utils
from ddt import ddt, data, file_data,  unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestsearchandverifyFilter:
    log = Utils.cust_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Launchpage(self.driver)
        self.sf = searchflightResults(self.driver)
    @data(("New Delhi", "JFK", "24/04/2023","Bangalore"), ("BOM", "JFK", "28/04/2023","Hyd"))  #data driven example its running two times
    # @unpack
    # @file_data("../testdata/testdata.json")  #data driven example its running from json format and that format store in testdata dictonory
    # @file_data("../testdata/testdata.yaml")

    # @data(*utils.read_data_from_excel("C:\\Users\\dell\\PycharmProjects\\testframeworkdemo\\testdata\\testdata.xlsx", "sheet1")) # get data from excel file its crete in utils
    # @data(*utils.read_data_from_csv("C:\\Users\\dell\\PycharmProjects\\testframeworkdemo\\testdata\tdatacsv.csv"))
    @unpack
    def test_search_flights(self, goingfrom, goingto, date, special):
        self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.page_scroll()
        self.sf.enterdestinationfromlocation(special)


