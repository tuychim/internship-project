from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CLICK_SETTINGS_BTN = (By.CSS_SELECTOR, "a[href='/settings'] div[class='menu-button-text']")
CLICK_EDIT_PROFILE_BTN = (By.CSS_SELECTOR, "a[class*='page-setting-block']")
NAME_INPUT = (By.CSS_SELECTOR, "input[wized='nameInputProfile']")
PHONE_INPUT = (By.CSS_SELECTOR, "input[wized='phoneInputProfile']")
SAVE_CHANGES_BTN = (By.XPATH, "//*[text()='Save changes']")
CLOSE_BTN = (By.XPATH, "//*[text()='Close']")


class SettingsPage(Page):
    def login_page(self):
        self.driver.find_element(*LOGIN_INPUT).send_keys('tuychi.m@gmail.com')
        self.driver.find_element(*PASSWORD_INPUT).send_keys('passwordtest')
        self.driver.find_element(*SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(CLICK_SETTINGS_BTN)
        )

    def click_on_settings(self):
        WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(CLICK_SETTINGS_BTN)
        )
        self.click(*CLICK_SETTINGS_BTN)

    def click_edit_profile(self):
        WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(CLICK_EDIT_PROFILE_BTN)
        )
        self.click(*CLICK_EDIT_PROFILE_BTN)

    def input_name(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NAME_INPUT)
        )
        name_input = self.driver.find_element(*NAME_INPUT)
        name_input.clear()
        name_input.send_keys('test+tuychi+careerist')

    def input_phone(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PHONE_INPUT)
        )
        phone_input = self.driver.find_element(*PHONE_INPUT)
        phone_input.clear()
        phone_input.send_keys('123+test+careerist')

    def verify_input_name(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NAME_INPUT)
        )
        actual_value = self.driver.find_element(*NAME_INPUT).get_attribute('value')
        print(f"Actual value found: {actual_value}")
        assert actual_value == 'test+tuychi+careerist', f"Expected 'test+tuychi+careerist', but got {actual_value}"

    def verify_input_phone(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PHONE_INPUT)
        )
        actual_value = self.driver.find_element(*PHONE_INPUT).get_attribute('value')
        print(f"Actual value found: {actual_value}")
        assert actual_value == '123+test+careerist', f"Expected '123+test+careerist', but got {actual_value}"

    def click_save_changes_btn(self):
        WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(SAVE_CHANGES_BTN)
        )
        self.click(*SAVE_CHANGES_BTN)

    def click_close_btn(self):
        WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(CLOSE_BTN)
        )
        self.click(*CLOSE_BTN)
