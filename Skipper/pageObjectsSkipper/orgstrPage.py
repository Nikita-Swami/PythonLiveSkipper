from selenium.common import InvalidSelectorException
from selenium.webdriver import Keys


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Skipper.pageObjectsSkipper.dashboardPage import DashboardPageSkipper
from Skipper.utilsSkipper.common_utils import webdriver_wait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time


class MasterCommonSkipperOrganizationStructure:
    def __init__(self, driver):
        self.driver = driver

        #Locators
        self.main_master = (By.XPATH, "//a[@id='tooltip3']")
        self.setup = (By.XPATH, "//div[@id='menu']/ul/li[2]/a/span[@class='menu-text']")
        self.organization_structure = (By.XPATH, "//a[@href='/OrganizationChartV2/GetOrganizationChart/6119']")

        # click on master menu
    def get_master_menu(self):
        self.driver.find_element(*self.main_master).click()

    def user_master_in_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.main_master, timeout=25)
        self.get_master_menu()

        # click on setup
    def get_setup_master(self):
        self.driver.find_element(*self.setup).click()

    def setup_master(self):
        webdriver_wait(driver=self.driver, element_tuple=self.setup, timeout=25)
        self.get_setup_master()

        #click on organization structure
    def get_organization_structure(self):
        self.driver.find_element(*self.organization_structure).click()

    def org_str_master(self):
        webdriver_wait(driver=self.driver, element_tuple=self.organization_structure, timeout=25)
        self.get_organization_structure()

    def president_org(self):
        wait = WebDriverWait(self.driver, 25)
        click_on_president_org = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/table[@id='charttable']/tbody/tr/td/div/div[@id='1']")))
        click_on_president_org.click()

    def avp_org(self):
        wait = WebDriverWait(self.driver, 25)
        click_on_avp_org = wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@id='charttable']/tbody/tr/td/div/div[@id='156']")))
        click_on_avp_org.click()

    def zonal_manager_org(self):
        wait = WebDriverWait(self.driver, 25)
        click_on_zm_org = wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@id='charttable']/tbody/tr/td/div/div[@id='157']")))
        click_on_zm_org.click()

    def branch_manager_org(self):
        wait = WebDriverWait(self.driver, 25)
        click_on_bm_org = wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@id='charttable']/tbody/tr/td/div/div[@id='158']")))
        click_on_bm_org.click()

    def scroll_down(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def run_test(self):
        target = self.driver.find_element(By.XPATH, "//table[@id='charttable']/tbody/tr/td/div/div[@id='158']")
        self.scroll_down(target)

    def assistant_wre_org(self):
        wait = WebDriverWait(self.driver, 25)
        click_on_assistant_wre_org = wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@id='charttable']/tbody/tr/td/div/div[@id='197']")))
        click_on_assistant_wre_org.click()

    def scroll_down1(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def run_test1(self):
        target = self.driver.find_element(By.XPATH, "//table[@id='charttable']/tbody/tr/td/div/div[@id='197']")
        self.scroll_down(target)

    def area_manager_add_button_org(self):
        wait = WebDriverWait(self.driver, 25)
        click_on_add_dso_org = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@data-original-title='Add Territory Sales Executive'])[3]")))
        click_on_add_dso_org.click()

    def employee_code(self):
        wait = WebDriverWait(self.driver, 25)
        employee_code_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='SHORTNAME']")))
        employee_code_text.send_keys("TESTDSO002")

    def designation(self):
        wait = WebDriverWait(self.driver, 25)
        designation_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='DESCRIPTION']")))
        designation_text.send_keys("TESTDSODATA")

    def first_name(self):
        wait = WebDriverWait(self.driver, 25)
        first_name_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='FNAME']")))
        first_name_text.send_keys("ABC")

    def middle_name(self):
        wait = WebDriverWait(self.driver, 25)
        middle_name_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='MNAME']")))
        middle_name_text.send_keys(".")

    def last_name(self):
        wait = WebDriverWait(self.driver, 25)
        last_name_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='LNAME']")))
        last_name_text.send_keys("DEF")

    def login_id(self):
        wait = WebDriverWait(self.driver, 25)
        login_id_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='LOGINID']")))
        login_id_text.send_keys("TESTDSO002")

    def email_id(self):
        wait = WebDriverWait(self.driver, 25)
        email_id_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='EMAIL']")))
        email_id_text.send_keys("pqr@gmail.com")

    def mobile_no(self):
        wait = WebDriverWait(self.driver, 25)
        mobile_no_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='MOBILE']")))
        mobile_no_text.send_keys("7890654321")

    def dob(self):
        wait = WebDriverWait(self.driver, 25)
        dob_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='DOB']")))
        dob_text.clear()
        dob_text.send_keys("22-02-2026")

    def select_dropdown_stockist(self):
        #Step 1: Click the Select2 control to open the dropdown
        wait = WebDriverWait(self.driver, 25)
        drop_down_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='s2id_autogen4']")))
        drop_down_element.click()

        # Step 2: Wait for the input box inside the dropdown and type
        wait = WebDriverWait(self.driver, 25)
        dropdown_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'select2-input')]")))
        dropdown_element.send_keys("Nutan Trading Corporation")
        dropdown_element.send_keys(Keys.ENTER)

        # Step 3 (optional): Click the matching option
        wait = WebDriverWait(self.driver, 25)
        click_and_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='select2-drop']/ul/li/div")))
        click_and_select.click()

    def scroll_down2(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def run_test2(self):
        target = self.driver.find_element(By.XPATH, "//input[@id='DOB']")
        self.scroll_down(target)

    def save_button(self):
        wait = WebDriverWait(self.driver, 25)
        save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSubmit_OC']")))
        save_button.click()
