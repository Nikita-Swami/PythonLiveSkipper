
from selenium.common import InvalidSelectorException
from selenium.webdriver import Keys


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Skipper.pageObjectsSkipper.dashboardPage import DashboardPageSkipper
from Skipper.utilsSkipper.common_utils import webdriver_wait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time



class MasterCommonSkipper:
    def __init__(self, driver):
        self.driver = driver

        #Locators
        self.main_master = (By.XPATH, "//a[@id='tooltip3']")
        self.common_master = (By.XPATH, "//div[@id='menu']/ul/li/a/span[@class='menu-text' and contains(text(), 'Common')]")
        self.unit_of_measurement = (By.XPATH, "//a[@href='/CommonMast/GetUomMastList/33']")

        #click on master menu
    def get_master_menu(self):
        self.driver.find_element(*self.main_master).click()

    def user_master_in_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.main_master, timeout=25)
        self.get_master_menu()

        #click on common master
    def get_common_master(self):
        self.driver.find_element(*self.common_master).click()

    def common_master(self):
        webdriver_wait(driver=self.driver, element_tuple=self.common_master, timeout=25)
        self.get_common_master()

       #click on unit of measurement
    def get_unit_of_measurement(self):
        self.driver.find_element(*self.unit_of_measurement).click()

    def unit_of_measurement(self):
        webdriver_wait(driver=self.driver, element_tuple=self.unit_of_measurement, timeout=25)
        self.get_unit_of_measurement()

    def add_button(self):
        wait = WebDriverWait(self.driver, 25)
        add_new_uom = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='btnAdd']")))
        add_new_uom.click()

    def uom_code(self):
        wait = WebDriverWait(self.driver, 25)
        add_uom_code = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='UOMCODE']")))
        add_uom_code.send_keys("Pair")

    def uom_description(self):
        wait = WebDriverWait(self.driver, 25)
        add_uom_description = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='DESCRIPTION']")))
        add_uom_description.send_keys("Pairs")

    def uom_display_name(self):
        wait = WebDriverWait(self.driver, 25)
        add_display_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='SHORTNAME']")))
        add_display_name.send_keys("PR")

    def submit_button(self):
        wait = WebDriverWait(self.driver, 25)
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSubmit']")))
        submit_button.click()

    def search_box(self):
        wait = WebDriverWait(self.driver, 25)
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='lookupTbl_filter']/label/input[@type='text']")))
        search_box.send_keys("Pair")

    def view_search_uom(self):
        wait = WebDriverWait(self.driver, 25)
        view_uom = wait.until((EC.element_to_be_clickable((By.XPATH, "//table[@id='lookupTbl']/tbody/tr/td/label[contains(text(),'Pairs')]"))))
        view_uom.click()