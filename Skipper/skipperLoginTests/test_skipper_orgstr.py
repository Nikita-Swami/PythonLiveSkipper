import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Skipper.pageObjectsSkipper.loginPage import LoginPageSkipper
from Skipper.pageObjectsSkipper.dashboardPage import DashboardPageSkipper
from Skipper.pageObjectsSkipper.orgstrPage import MasterCommonSkipperOrganizationStructure
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://beatskpltest.prowessbeat.net/")
    return driver


@allure.epic("Skipper Master Organization Structure Test")
@allure.feature("#TC1 Skipper Positive Test")
@pytest.mark.positive

def test_skipper_master_starting_number(setup):
    login_page = LoginPageSkipper(driver=setup)
    login_page.login_to_skipper(usr="Portaladmin", pwd="Abc@123")

    master_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    master_Page.get_master_menu()
    time.sleep(10)

    setup_master_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    setup_master_Page.get_setup_master()
    time.sleep(10)

    organization_structure_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    organization_structure_Page.get_organization_structure()
    time.sleep(10)

    president_org_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    president_org_Page.president_org()
    time.sleep(10)

    avp_org_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    avp_org_Page.avp_org()
    time.sleep(10)

    zm_org_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    zm_org_Page.zonal_manager_org()
    time.sleep(10)

    bm_org_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    bm_org_Page.branch_manager_org()
    time.sleep(10)

    run_test_scroll = MasterCommonSkipperOrganizationStructure(driver=setup)
    run_test_scroll.run_test()
    time.sleep(10)

    ass_wre_org_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    ass_wre_org_Page.assistant_wre_org()
    time.sleep(10)

    run_test_scroll1 = MasterCommonSkipperOrganizationStructure(driver=setup)
    run_test_scroll1.run_test1()
    time.sleep(10)

    add_button_for_dso_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    add_button_for_dso_Page.area_manager_add_button_org()
    time.sleep(10)

    employee_code_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    employee_code_Page.employee_code()
    time.sleep(10)

    designation_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    designation_Page.designation()
    time.sleep(10)

    first_name_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    first_name_Page.first_name()
    time.sleep(10)

    middle_name_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    middle_name_Page.middle_name()
    time.sleep(10)

    last_name_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    last_name_Page.last_name()
    time.sleep(10)

    login_id_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    login_id_Page.login_id()
    time.sleep(10)

    email_id_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    email_id_Page.email_id()
    time.sleep(10)

    mobile_no_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    mobile_no_Page.mobile_no()
    time.sleep(10)

    dob_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    dob_Page.dob()
    time.sleep(10)

    stockist_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    stockist_Page.select_dropdown_stockist()
    time.sleep(10)

    run_test_scroll2 = MasterCommonSkipperOrganizationStructure(driver=setup)
    run_test_scroll2.run_test2()
    time.sleep(10)

    save_form_Page = MasterCommonSkipperOrganizationStructure(driver=setup)
    save_form_Page.save_button()
    time.sleep(10)



