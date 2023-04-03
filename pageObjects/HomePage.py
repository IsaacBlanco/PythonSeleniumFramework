from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    # create a constructos with driver, driver is send from TC class
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    pwd = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        # add * to let python know that is considerd as tuple
        self.driver.find_element(*HomePage.shop).click()
        # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPwd(self):
        return self.driver.find_element(*HomePage.pwd)

    def getCheck(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlertSuccessMessage(self):
        return self.driver.find_element(*HomePage.alert)