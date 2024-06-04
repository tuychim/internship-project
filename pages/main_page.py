from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import Page
from time import sleep


LOGIN_INPUT = (By.ID, "email-2")
PASSWORD_INPUT = (By.ID, "field")
SUBMIT_BUTTON = (By.CSS_SELECTOR, ".login-button")
CLICK_BUTTON = (By.CSS_SELECTOR, ".menu-twobutton")
VERIFY_RIGHT_PAGE = (By.CSS_SELECTOR, ".page-title")
CLICK_FILTER = (By.CSS_SELECTOR, ".filter-button")
CLICK_LAST_UNIT = (By.XPATH, "//div[@wized='priorityStatusLastUnits']")
VERIFY_TAG = (By.CSS_SELECTOR, 'div[class="commision_box"] [class="_5-comission"]')


class MainPage(Page):

    def open_main(self):
        self.open("https://soft.reelly.io/sign-in")

    def login_page(self):
        self.driver.find_element(*LOGIN_INPUT).send_keys('tuychi.m@gmail.com')
        self.driver.find_element(*PASSWORD_INPUT).send_keys('passwordtest')
        self.driver.find_element(*SUBMIT_BUTTON).click()
        sleep(8)

    def click_on_off(self):
        self.wait_until_clickable_click(*CLICK_FILTER)

    def verify_page(self):
        sleep(15)
        self.verify_url('https://soft.reelly.io/')

    def filter_by_last_units(self):
        self.driver.find_element(*CLICK_FILTER).click()
        sleep(8)
        self.driver.find_element(*CLICK_LAST_UNIT).click()

    def verify_last_units(self):
        tags = self.driver.find_elements(*VERIFY_TAG)
        expected_text = 'Last units'
        assert tags, "No elements found with the Last Units tag"
        for tag in tags:
            assert tag.text == expected_text, f"Expected text 'Last units', but got '{tag.text}'"
        sleep(10)

