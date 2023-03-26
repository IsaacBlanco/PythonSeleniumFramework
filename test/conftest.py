import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup():
    # add options to chrome to change behaviour using class webdriver.ChromeOptions()
    chrome_options = webdriver.ChromeOptions()

    # start maximized
    chrome_options.add_argument("--start-maximized")
    # handlre errors certificates win pages
    chrome_options.add_argument("--ignore-certificates-erros")

    # chrome driver create a service to point to where the .exe is located
    service_obj = Service("C:/Drivers/chromedriver.exe")
    # integreate chrome options to driver
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    # add implicit wait
    driver.implicitly_wait(4)
    # go to url
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    yield 
    driver.close()

    return driver
