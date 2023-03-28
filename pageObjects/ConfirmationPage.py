from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    countries = (By.ID, "country")
    country = (By.LINK_TEXT, "Spain")
    check = (By.XPATH, "//label[@for='checkbox2']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getCountries(self):
        return self.driver.find_element(*ConfirmationPage.countries)
        #self.driver.find_element(By.ID, "country").send_keys("in")

    def selectCountry(self):
        return self.driver.find_element(*ConfirmationPage.country)

    def selectCheckBox(self):
        return  self.driver.find_element(*ConfirmationPage.check)

    def clickSubmit(self):
        return self.driver.find_element(*ConfirmationPage.submit)
    def getAlert(self):
        return  self.driver.find_element(*ConfirmationPage.alert)