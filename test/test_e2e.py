import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmationPage import ConfirmationPage
from pageObjects.HomePage import HomePage
from utils.BaseClass import BaseClass


#@pytest.mark.fixture("setup") is inherit from BaseClass
class TestE2E(BaseClass):
    # def test_e2e(self, setup): we cna remove setup because self is loaded with the driver variabler
    def test_e2e(self):

        # to acces the driver assigned in setup fixture to the class driver
        # we need to use keyword "self" to acces class variables
        # so to call our driver it should go like "self.driver"

        shop = HomePage(self.driver)
        shop.shopItems().click()

        time.sleep(2)
        # finding and adding blacberry tp cart

        checkoutPage = CheckOutPage(self.driver)
        cards = checkoutPage.getCardTittle()
        for card  in cards:
            target_element = card.find_element(By.XPATH, "div/h4/a")
            print(target_element.text)
            if target_element.text == "Blackberry":
                checkoutPage.getCardTarget(card).click()

        # clicking  checkout button
        checkoutPage.clickCheckOut().click()

        # clicking checkot
        checkoutPage.clickSuccess().click()

        # entering country
        confirmation = ConfirmationPage(self.driver)
        confirmation.getCountries().send_keys("in")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='suggestions']//a")))

        confirmation.selectCountry().click()
        confirmation.selectCheckBox().click()
        confirmation.clickSubmit().click()

        result = confirmation.getAlert().text
        expected = "Success! Thank you!"
        print(result)
        print(expected)
        assert expected in result
