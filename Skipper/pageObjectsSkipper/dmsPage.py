# Customer Master Page Class
from selenium.common import InvalidSelectorException
from selenium.webdriver import Keys
# Page Locators
# Page Actions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Skipper.pageObjectsSkipper.dashboardPage import DashboardPageSkipper
from Skipper.utilsSkipper.common_utils import webdriver_wait
from selenium.webdriver.support.ui import Select

class DMSPageSkipper:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.prime_dms = (By.XPATH, "//div/div/div/ul/li/a/span[text()='Prime']")
        self.retailer_invoice = (By.XPATH, "//a[@href='/RetailerInvoice/GetRetailerInvoiceDetails/7121']")
        self.add_invoice = (By.XPATH, "//a[@href='#RetailerInvoice3']")

    #Click on Prime menu
    def get_prime_page(self):
        self.driver.find_element(*self.prime_dms).click()

    def user_prime_in_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.prime_dms, timeout=15)
        self.get_prime_page()

    # Click on Retailer Invoice Menu
    def get_retailer_invoice(self):
        self.driver.find_element(*self.retailer_invoice).click()

    def retailer_invoice(self):
        webdriver_wait(driver=self.driver, element_tuple=self.retailer_invoice, timeout=15)
        self.get_retailer_invoice()

    def get_add_invoice(self):
        self.driver.find_element(*self.add_invoice).click()

    def add_invoice_tab(self):
        webdriver_wait(driver=self.driver, element_tuple=self.add_invoice, timeout=15)
        self.get_add_invoice()

