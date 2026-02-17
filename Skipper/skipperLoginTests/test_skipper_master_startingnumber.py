import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Skipper.pageObjectsSkipper.loginPage import LoginPageSkipper
from Skipper.pageObjectsSkipper.dashboardPage import DashboardPageSkipper
from Skipper.pageObjectsSkipper.startingnumberPage import MasterCommonSkipperStartingNumber
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://beatskpltest.prowessbeat.net/")
    return driver


@allure.epic("Skipper Master Starting Number Test")
@allure.feature("#TC1 Skipper Positive Test")
@pytest.mark.positive

def test_skipper_master_starting_number(setup):
    login_page = LoginPageSkipper(driver=setup)
    login_page.login_to_skipper(usr="Portaladmin", pwd="Abc@123")

    master_Page = MasterCommonSkipperStartingNumber(driver=setup)
    master_Page.get_master_menu()
    time.sleep(10)

    common_master_Page = MasterCommonSkipperStartingNumber(driver=setup)
    common_master_Page.get_common_master()
    time.sleep(10)

    starting_number_Page = MasterCommonSkipperStartingNumber(driver=setup)
    starting_number_Page.get_starting_number()
    time.sleep(10)

    add_button_details = MasterCommonSkipperStartingNumber(driver=setup)
    add_button_details.add_button()
    time.sleep(10)

    add_sys_docs_dd = MasterCommonSkipperStartingNumber(driver=setup)
    add_sys_docs_dd.select_dropdown_by_visible_text_sys_doc()
    time.sleep(10)

    add_document_dd = MasterCommonSkipperStartingNumber(driver=setup)
    add_document_dd.select_dropdown_by_visible_text_document()
    time.sleep(10)

    add_control_number_dd = MasterCommonSkipperStartingNumber(driver=setup)
    add_control_number_dd.select_dropdown_by_visible_text_control_number()
    time.sleep(10)

    add_prefix_details = MasterCommonSkipperStartingNumber(driver=setup)
    add_prefix_details.prefix_text()
    time.sleep(10)

    add_suffix_details =MasterCommonSkipperStartingNumber(driver=setup)
    add_suffix_details.suffix_text()
    time.sleep(10)

    add_starting_number_details = MasterCommonSkipperStartingNumber(driver=setup)
    add_starting_number_details.starting_number_text()
    time.sleep(10)

    add_number_digit_details = MasterCommonSkipperStartingNumber(driver=setup)
    add_number_digit_details.number_digit_text()
    time.sleep(10)

    save_details = MasterCommonSkipperStartingNumber(driver=setup)
    save_details.save_button()
    time.sleep(10)

    search_details = MasterCommonSkipperStartingNumber(driver=setup)
    search_details.search_box()
    time.sleep(10)

    edit_details = MasterCommonSkipperStartingNumber(driver=setup)
    edit_details.edit_button_on_view()
    time.sleep(10)

    edit_clear_prefix_details = MasterCommonSkipperStartingNumber(driver=setup)
    edit_clear_prefix_details.edit_clear_prefix_details()
    time.sleep(10)

    edit_clear_starting_number_details = MasterCommonSkipperStartingNumber(driver=setup)
    edit_clear_starting_number_details.edit_clear_add_starting_number_details()
    time.sleep(10)

    edit_clear_number_digit_details = MasterCommonSkipperStartingNumber(driver=setup)
    edit_clear_number_digit_details.edit_clear_add_number_digit_details()
    time.sleep(10)

    edit_clear_active_checkbox = MasterCommonSkipperStartingNumber(driver=setup)
    edit_clear_active_checkbox.edit_and_uncheck_checkbox_active_details()
    time.sleep(10)

    edit_form_submit_details = MasterCommonSkipperStartingNumber(driver=setup)
    edit_form_submit_details.after_edit_submit_details()
    time.sleep(10)








