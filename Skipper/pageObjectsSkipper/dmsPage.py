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
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

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
        webdriver_wait(driver=self.driver, element_tuple=self.prime_dms, timeout=25)
        self.get_prime_page()

    # Click on Retailer Invoice Menu
    def get_retailer_invoice(self):
        self.driver.find_element(*self.retailer_invoice).click()

    def retailer_invoice(self):
        webdriver_wait(driver=self.driver, element_tuple=self.retailer_invoice, timeout=25)
        self.get_retailer_invoice()

    def get_add_invoice(self):
        self.driver.find_element(*self.add_invoice).click()

    def add_invoice_tab(self):
        webdriver_wait(driver=self.driver, element_tuple=self.add_invoice, timeout=25)
        self.get_add_invoice()

    def select_dropdown_by_visible_text_add_invoice_to_retailer(self):
        # Step 1: Click the Select2 control to open the dropdown
        wait = WebDriverWait(self.driver, 25)
        drop_down_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='s2id_TOSLID']")))
        drop_down_element.click()

        # Step 2: Wait for the input box inside the dropdown and type
        wait = WebDriverWait(self.driver,25)
        dropdown_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='select2-drop']//input")))
        dropdown_element.send_keys("GUMTYA ENTERPRISE")

        # Step 3 (optional): Click the matching option
        wait = WebDriverWait(self.driver, 25)
        click_and_select = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='select2-drop']/ul/li/div")))
        click_and_select.click()

    def select_dropdown_by_visible_text_add_invoice_ship_to_retailer(self):
        # Step 1: Click the Select2 control to open the dropdown
        wait = WebDriverWait(self.driver,15)
        drop_down_ship_to = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='s2id_SHIPTO']")))
        drop_down_ship_to.click()

        # Step 2: Wait for the input box inside the dropdown and type
        wait = WebDriverWait(self.driver, 15)
        drop_down_ship_to_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='select2-drop']//input")))
        drop_down_ship_to_element.send_keys(", KAPASARIA MAHISHADAL EAST MEDNAPUR")

        # Step 3 (optional): Click the matching option
        wait = WebDriverWait(self.driver, 15)
        click_and_select_ship_to = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='select2-drop']/ul/li/div")))
        click_and_select_ship_to.click()

    def select_dropdown_by_visible_text_add_invoice_bill_to_retailer(self):
        # Step 1: Click the Select2 control to open the dropdown
        wait = WebDriverWait(self.driver, 15)
        drop_down_bill_to = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='s2id_BILLTO']")))
        drop_down_bill_to.click()

        # Step 2: Wait for the input box inside the dropdown and type
        wait = WebDriverWait(self.driver, 15)
        drop_down_bill_to_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='select2-drop']//input")))
        drop_down_bill_to_element.send_keys(", KAPASARIA MAHISHADAL EAST MEDNAPUR")

        # Step 3 (optional): Click the matching option
        wait = WebDriverWait(self.driver, 15)
        click_and_select_bill_to = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='select2-drop']/ul/li/div")))
        click_and_select_bill_to.click()

    def next_button(self):
        wait = WebDriverWait(self.driver,15)
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='submitAddressID']")))
        next_button.click()

    def add_product_button1(self):
        wait = WebDriverWait(self.driver,15)
        add_product = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='sheepItForm_add']")))
        add_product.click()

    def add_product1(self):
        # Step 1: Click the Select2 control to open the dropdown
        wait = WebDriverWait(self.driver, 15)
        drop_down_product1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='s2id_ITEMID_0']")))
        drop_down_product1.click()

        # Step 2: Wait for the input box inside the dropdown and type
        wait = WebDriverWait(self.driver, 15)
        drop_down_product1_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='select2-drop']//input")))
        drop_down_product1_element.send_keys("3000002659")

        # Step 3 (optional): Click the matching option
        wait = WebDriverWait(self.driver, 15)
        click_and_select_drop_down_product1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='select2-drop']/ul/li/div")))
        click_and_select_drop_down_product1.click()

        #Step 4 :Add product quantity input
        wait = WebDriverWait(self.driver, 15)
        quantity_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='SOQTY_0']")))
        quantity_input.send_keys("2")

    def add_product_button2(self):
        wait = WebDriverWait(self.driver, 30)
        try:
            add_product = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='sheepItForm_add']")))
            add_product.click()
            print("✅ Clicked Add Product button.")
        except TimeoutException:
            print("❌ Timeout: Add Product button not found or not clickable.")
            self.driver.save_screenshot("add_product_button_timeout.png")
            raise

    def add_product2(self):
        wait = WebDriverWait(self.driver, 30)
        try:
            # Step 1: Click the product dropdown
            drop_down_product2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='s2id_ITEMID_1']")))
            drop_down_product2.click()
            print("✅ Opened product dropdown.")

            # Step 2: Type into the Select2 input
            input_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='select2-drop']//input")))
            input_box.clear()
            input_box.send_keys("3000003081")
            print("✅ Typed product code.")

            # Step 3: Click the matching result
            option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='select2-drop']/ul/li/div")))
            option.click()
            print("✅ Selected product from dropdown.")

            # Step 4: Enter quantity
            # Step 4 :Add product quantity input
            wait = WebDriverWait(self.driver, 15)
            quantity_input1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='SOQTY_1']")))
            quantity_input1.send_keys("4")
            print("✅ Quantity entered.")

        except TimeoutException:
            print("❌ Timeout: Could not locate one of the product fields.")
            self.driver.save_screenshot("add_product2_timeout.png")
            raise
        except StaleElementReferenceException:
            print("⚠️ Element went stale, retrying...")
            time.sleep(1)
            self.add_product2()  # retry once

    def next_button_invoice(self):
        wait = WebDriverWait(self.driver, 15)
        next_button_invoice = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='submitSaleInvoice']")))
        next_button_invoice.click()

    def scroll_down(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def run_test(self):
        target = self.driver.find_element(By.XPATH, "//div[@id='step-3']//button[@class='btn btn-primary nextBtn  pull-right step3Next']")
        self.scroll_down(target)

    def view_details_click_on_next(self):
        wait = WebDriverWait(self.driver,15)
        view_details_next = wait.until((EC.presence_of_element_located((By.XPATH, "//div[@id='step-3']//button[@class='btn btn-primary nextBtn  pull-right step3Next']"))))
        view_details_next.click()

    def save_button(self):
        wait = WebDriverWait(self.driver,15)
        save_invoice_button = wait.until((EC.presence_of_element_located((By.XPATH, "//button[@id='submitInvoice']"))))
        save_invoice_button.click()

