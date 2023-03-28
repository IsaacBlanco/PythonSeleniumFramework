import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# function to add command line options to run testt
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chromer or firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_name")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    # add implicit wait
    driver.implicitly_wait(4)
    # go to url
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

    ## return driver  THIS WONT WORK WITH YEILD SO BEFORE
    ## so we need to add a "request" instance as parameter to setup
    ## and then add "request.cls.driver = driver" before "yeld"
    ## we assing our driver to a class diver(cls.driver) so we can use cls
    ## to get our driver in any class that use the fixture
