from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTittle = (By.XPATH, "//div[@class='card h-100']")
    cardTarget = (By.XPATH, "div/button")
    btnCheckout = (By.XPATH, "//a[contains(text(), 'Checkout')]")
    btnSuccess = (By.CLASS_NAME, "btn-success")

    def getCardTittle(self):
        return self.driver.find_elements(*CheckOutPage.cardTittle)
        # elements = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    def getCardTarget(self, card):
        return card.find_element(*CheckOutPage.cardTarget)
        # card.find_element(By.XPATH, "div/button").click()

    def clickCheckOut(self):
        return self.driver.find_element(*CheckOutPage.btnCheckout)
        # self.driver.find_element(By.XPATH, "//a[contains(text(), 'Checkout')]").click()

    def clickSuccess(self):
        return self.driver.find_element(*CheckOutPage.btnSuccess)
