from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep


LOGIN_INPUT = (By.ID, "email-2")
PASSWORD_INPUT = (By.ID, "field")
SUBMIT_BUTTON = (By.CSS_SELECTOR, ".login-button")
# CLICK_OFF_PLAN_BUTTON = (By.CSS_SELECTOR, "[wized='mobileTabProperties']")
CLICK_OFF_PLAN_BUTTON = (By.CSS_SELECTOR, ".html-embed")
# CLICK_FILTER = (By.CSS_SELECTOR, "[.filter-button]")
CLICK_FILTER = (By.CSS_SELECTOR, "div[class='filter-button']")
CLICK_LAST_UNIT = (By.CSS_SELECTOR, "[wized='priorityStatusLastUnits']")
VERIFY_TAG = (By.CSS_SELECTOR, '[wized="projectStatus"]')


class MainPage(Page):

    def open_main(self):
        self.open("https://soft.reelly.io/main-menu")

    def login_page(self):
        self.driver.find_element(*LOGIN_INPUT).send_keys('tuychi.m@gmail.com')
        self.driver.find_element(*PASSWORD_INPUT).send_keys('passwordtest')
        self.driver.find_element(*SUBMIT_BUTTON).click()
        sleep(10)

    def click_on_off(self):
        self.driver.find_element(*CLICK_OFF_PLAN_BUTTON).click()
        sleep(10)

    def verify_page(self):
        self.verify_url('https://soft.reelly.io/')
        sleep(10)

    def filter_by_last_units(self):
        self.driver.find_element(*CLICK_FILTER).click()
        self.driver.find_element(*CLICK_LAST_UNIT).click()
        sleep(10)

    def verify_last_units(self):
        tags = self.driver.find_elements(*VERIFY_TAG)
        expected_text = 'Last units'
        assert tags, "No elements found with the Last Units tag"
        for tag in tags:
            assert tag.text == expected_text, f"Expected text 'Last units', but got '{tag.text}'"


