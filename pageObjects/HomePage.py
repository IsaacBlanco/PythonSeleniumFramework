from selenium.webdriver.common.by import By


class HomePage:

    # create a constructos with driver, driver is send from TC class
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")

    def shopItems(self):
        # add * to let python know that is considerd as tuple
        return self.driver.find_element(*HomePage.shop)
        # self.driver.find_element(By.LINK_TEXT, "Shop").click()