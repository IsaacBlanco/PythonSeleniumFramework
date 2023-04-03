import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyInputSugestions(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        # dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
        dropdown.select_by_visible_text(text)
