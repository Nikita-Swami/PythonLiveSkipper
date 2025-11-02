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

    add_invoice_to_retailer = DMSPageSkipper(driver=setup)
    add_invoice_to_retailer.select_dropdown_by_visible_text_add_invoice_to_retailer()
    time.sleep(20)

    add_invoice_ship_to = DMSPageSkipper(driver=setup)
    add_invoice_ship_to.select_dropdown_by_visible_text_add_invoice_ship_to_retailer()
    time.sleep(10)

    add_invoice_bill_to = DMSPageSkipper(driver=setup)
    add_invoice_bill_to.select_dropdown_by_visible_text_add_invoice_bill_to_retailer()
    time.sleep(10)

    add_invoice_next_button =DMSPageSkipper(driver=setup)
    add_invoice_next_button.next_button()
    time.sleep(10)

    add_product_button_one = DMSPageSkipper(driver=setup)
    add_product_button_one.add_product_button1()
    time.sleep(10)

    add_first_product = DMSPageSkipper(driver=setup)
    add_first_product.add_product1()
    time.sleep(10)

    add_product_button_second = DMSPageSkipper(driver=setup)
    add_product_button_second.add_product_button2()
    time.sleep(15)

    add_second_product = DMSPageSkipper(driver=setup)
    add_second_product.add_product2()
    time.sleep(15)

    next_button_invoice = DMSPageSkipper(driver=setup)
    next_button_invoice.next_button_invoice()
    time.sleep(10)

    run_test_scroll = DMSPageSkipper(driver=setup)
    run_test_scroll.run_test()
    time.sleep(10)

    view_details_click_next = DMSPageSkipper(driver=setup)
    view_details_click_next.view_details_click_on_next()
    time.sleep(10)

    save_invoice_details = DMSPageSkipper(driver=setup)
    save_invoice_details.save_button()
    time.sleep(10)