
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


class MasterCommonSkipperStartingNumber:
    def __init__(self, driver):
        self.driver = driver

        #Locators
        self.main_master = (By.XPATH, "//a[@id='tooltip3']")
        self.common_master = (By.XPATH, "//div[@id='menu']/ul/li/a/span[@class='menu-text' and contains(text(), 'Common')]")
        self.starting_number = (By.XPATH, "//a[@href='/generalsetting/getdocnumlist/68']")

    # click on master menu
    def get_master_menu(self):
        self.driver.find_element(*self.main_master).click()

    def user_master_in_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.main_master, timeout=25)
        self.get_master_menu()

    # click on common master
    def get_common_master(self):
        self.driver.find_element(*self.common_master).click()

    def common_master(self):
        webdriver_wait(driver=self.driver, element_tuple=self.common_master, timeout=25)
        self.get_common_master()

    #click on starting number
    def get_starting_number(self):
        self.driver.find_element(*self.starting_number).click()

    def starting_number(self):
        webdriver_wait(driver=self.driver, element_tuple=self.starting_number, timeout=25)
        self.get_starting_number()

    #add button
    def add_button(self):
        wait = WebDriverWait(self.driver, 25)
        add_new_starting_number = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnAdd']")))
        add_new_starting_number.click()

    def select_dropdown_by_visible_text_sys_doc(self):
   # Step 1: Click the Select2 control to open the dropdown
         wait = WebDriverWait(self.driver, 25)
         drop_down_element = wait.until((EC.element_to_be_clickable((By.XPATH, "//div[@id='s2id_SYSDOCID']"))))
         drop_down_element.click()

    #Step 2: Wait for the input box inside the dropdown and type
         wait = WebDriverWait(self.driver, 25)
         dropdown_element = wait.until((EC.presence_of_element_located((By.XPATH, "//div[@id='select2-drop']//input"))))
         dropdown_element.send_keys("Returns")
         dropdown_element.send_keys(Keys.ENTER)

    # Step 3 (optional): Click the matching option
         wait = WebDriverWait(self.driver, 25)
         click_and_select = wait.until((EC.element_to_be_clickable((By.XPATH, "//div[@id='select2-drop']/ul/li/div/span"))))
         click_and_select.click()

    def select_dropdown_by_visible_text_document(self):
   # Step 1: Click the Select2 control to open the dropdown
          wait = WebDriverWait(self.driver, 25)
          drop_down_document = wait.until((EC.element_to_be_clickable((By.XPATH, "//div[@id='s2id_DOCID']"))))
          drop_down_document.click()

   # Step 2: Wait for the input box inside the dropdown and type
          wait = WebDriverWait(self.driver, 25)
          dropdown_document = wait.until((EC.presence_of_element_located((By.XPATH, "//div[@id='select2-drop']//input"))))
          dropdown_document.send_keys("Returns")

    # Step 3 (optional): Click the matching option
          wait = WebDriverWait(self.driver, 25)
          click_and_select_document = wait.until((EC.element_to_be_clickable((By.XPATH, "//div[@id='select2-drop']/ul/li/div/span"))))
          click_and_select_document.click()

    def select_dropdown_by_visible_text_control_number(self):
    # Step 1: Click the Select2 control to open the dropdown
        wait = WebDriverWait(self.driver, 25)
        drop_down_control_number = wait.until((EC.element_to_be_clickable((By.XPATH, "//div[@id='s2id_CONTROLNO']"))))
        drop_down_control_number.click()

    # Step 2: Wait for the input box inside the dropdown and type
        wait = WebDriverWait(self.driver, 25)
        dropdown_control_number = wait.until((EC.presence_of_element_located((By.XPATH, "//div[@id='select2-drop']//input"))))
        dropdown_control_number.send_keys("2025-2026")
        dropdown_control_number.send_keys(Keys.ENTER)

    # Step 3 (optional): Click the matching option
        wait = WebDriverWait(self.driver, 25)
        click_and_select_control_number = wait.until((EC.element_to_be_clickable((By.XPATH, "//div[@id='select2-drop']/ul/li/div/span"))))
        click_and_select_control_number.click()

    def prefix_text(self):
        wait = WebDriverWait(self.driver, 25)
        add_prefix_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PERFIX']")))
        add_prefix_text.send_keys("RET")

    def suffix_text(self):
        wait = WebDriverWait(self.driver, 25)
        add_suffix_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='SUFFIX']")))
        add_suffix_text.send_keys("")

    def starting_number_text(self):
        wait = WebDriverWait(self.driver, 25)
        add_starting_number = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='INVCNUMB']")))
        add_starting_number.send_keys("000001")

    def number_digit_text(self):
        wait = WebDriverWait(self.driver, 25)
        add_number_digit = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='NUMBDIGIT']")))
        add_number_digit.send_keys("6")

    def save_button(self):
        wait = WebDriverWait(self.driver, 25)
        save_data = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSubmit']")))
        save_data.click()

    def search_box(self):
        wait = WebDriverWait(self.driver, 25)
        search_box_text = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='lookupTbl_filter']/label/input")))
        search_box_text.send_keys("Returns")

    def edit_button_on_view(self):
        wait = WebDriverWait(self.driver,25)
        edit_button_data = wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@id='lookupTbl']/tbody/tr[1]/td[8]/div/button[@class='btn btn-xs btn-info']")))
        edit_button_data.click()

    #//table[@id="lookupTbl"]/tbody/tr[1]/td[8]/div/button[@class="btn btn-xs btn-info"]

    def edit_clear_prefix_details(self):
        wait = WebDriverWait(self.driver, 25)
        clear_prefix = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PERFIX']")))
        clear_prefix.clear()
        clear_prefix.send_keys("INV")

    def edit_clear_add_starting_number_details(self):
        wait = WebDriverWait(self.driver, 25)
        clear_starting_number = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='INVCNUMB']")))
        clear_starting_number.clear()
        clear_starting_number.send_keys("202600001")

    def edit_clear_add_number_digit_details(self):
        wait = WebDriverWait(self.driver, 25)
        clear_number_digit = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='NUMBDIGIT']")))
        clear_number_digit.clear()
        clear_number_digit.send_keys("9")

    def edit_and_uncheck_checkbox_active_details(self):
        wait = WebDriverWait(self.driver, 25)
        untick_active_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='ISACTIVE']")))
        #if untick_active_checkbox.is_selected():
        #    untick_active_checkbox.click()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", untick_active_checkbox)

        if untick_active_checkbox.is_selected():
            self.driver.execute_script("arguments[0].click();", untick_active_checkbox)

    def after_edit_submit_details(self):
        wait = WebDriverWait(self.driver, 25)
        after_edit_submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSubmit']")))
        after_edit_submit.click()






