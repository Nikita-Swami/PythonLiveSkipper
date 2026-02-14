import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Skipper.pageObjectsSkipper.loginPage import LoginPageSkipper
from Skipper.pageObjectsSkipper.dashboardPage import DashboardPageSkipper
from Skipper.pageObjectsSkipper.commonuomPage import MasterCommonSkipper
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://beatskpltest.prowessbeat.net/")
    return driver


@allure.epic("Skipper Master Test")
@allure.feature("#TC1 Skipper Positive Test")
@pytest.mark.positive

def test_skipper_master(setup):
    login_page = LoginPageSkipper(driver=setup)
    login_page.login_to_skipper(usr="Portaladmin", pwd="Abc@123")

    master_Page = MasterCommonSkipper(driver=setup)
    master_Page.get_master_menu()
    time.sleep(10)

    common_master_Page = MasterCommonSkipper(driver=setup)
    common_master_Page.get_common_master()
    time.sleep(10)

    unit_of_measurement_Page = MasterCommonSkipper(driver=setup)
    unit_of_measurement_Page.get_unit_of_measurement()
    time.sleep(10)

    add_button_details = MasterCommonSkipper(driver=setup)
    add_button_details.add_button()
    time.sleep(10)

    add_uom_code_details = MasterCommonSkipper(driver=setup)
    add_uom_code_details.uom_code()
    time.sleep(10)

    add_uom_desc = MasterCommonSkipper(driver=setup)
    add_uom_desc.uom_description()
    time.sleep(10)

    add_uom_display_name = MasterCommonSkipper(driver=setup)
    add_uom_display_name.uom_display_name()
    time.sleep(10)

    submit_button_toclick = MasterCommonSkipper(driver=setup)
    submit_button_toclick.submit_button()
    time.sleep(10)

    search_text_box = MasterCommonSkipper(driver=setup)
    search_text_box.search_box()
    time.sleep(10)

    view_uom_details = MasterCommonSkipper(driver=setup)
    view_uom_details.view_search_uom()
    time.sleep(10)
