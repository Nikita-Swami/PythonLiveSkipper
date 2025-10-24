import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import org.openqa.selenium.InvalidSelectorException;
# Assertions and use the Page Object class

# Webdriver Start
# User Interaction + Assertions
# Close Webdriver

from Skipper.pageObjectsSkipper.loginPage import LoginPageSkipper
from Skipper.pageObjectsSkipper.dashboardPage import DashboardPageSkipper
from Skipper.pageObjectsSkipper.dmsPage import DMSPageSkipper
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://beatskpltest.prowessbeat.net/")
    return driver

@allure.epic("Dhanuka Login Test")
@allure.feature("TC#1 Dhanuka Positive Test")
@pytest.mark.positive

def test_skipper_dms(setup):
    login_page = LoginPageSkipper(driver=setup)
    login_page.login_to_skipper(usr="D001", pwd="Dist@123")

    dms_Page = DMSPageSkipper(driver=setup)
    dms_Page.get_prime_page()
    time.sleep(10)

    retailer_invoice_Page = DMSPageSkipper(driver=setup)
    retailer_invoice_Page.get_retailer_invoice()
    time.sleep(10)

    add_invoice_Page = DMSPageSkipper(driver=setup)
    add_invoice_Page.get_add_invoice()
    time.sleep(10)