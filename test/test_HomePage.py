import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utils.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_fromSubmission(self, getData):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["fname"])
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Valac Shiro")

        homePage.getEmail().send_keys(getData["email"])
        # driver.find_element(By.NAME, "email").send_keys("valac@shiro.com")

        homePage.getPwd().send_keys(getData["pwd"])
        # driver.find_element(By.ID, "exampleInputPassword1").send_keys("1223456")

        homePage.getCheck().click()
        # driver.find_element(By.ID, "exampleCheck1").click()

        # selectos static

        self.selectOptionByText(homePage.getGender(), getData["sex"])

        homePage.submitForm().click()
        # driver.find_element(By.XPATH, "//input[@value='Submit']").click()

        message = homePage.getAlertSuccessMessage().text

        assert "Success" in message
        self.driver.refresh()

    # ------ we removed the paramatized data from this fixture to a new class that will holds all data related to this page
    # ------ test_HomePage_data has a variavble withis this data
    # @pytest.fixture(params=[{"fname":"Valac","email":"valac@shiro.com", "pwd":"test@123", "sex":"Male"},
    #                       {"fname":"Ale","email":"ale@shiro.com", "pwd":"test@123", "sex":"Female"}])
    @pytest.fixture(params=HomePageData.test_homePage_data)
    # get data loads all of testdata before tc execute, this is included in def arguments
    def getData(self, request):
        return request.param
