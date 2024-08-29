from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

LOGIN_INPUT = (By.ID, "email-2")
PASSWORD_INPUT = (By.ID, "field")
SUBMIT_BUTTON = (By.CSS_SELECTOR, ".login-button")
CLICK_CONNECT_COMPANY_BTN = (By.CSS_SELECTOR, "div[class='get-free-period menu']")


class ConnectCompany(Page):

    def login_page(self):
        self.driver.find_element(*LOGIN_INPUT).send_keys('tuychi.m@gmail.com')
        self.driver.find_element(*PASSWORD_INPUT).send_keys('passwordtest')
        self.driver.find_element(*SUBMIT_BUTTON).click()
        sleep(6)

    def click_connect_company(self):
        self.click(*CLICK_CONNECT_COMPANY_BTN)
        sleep(3)

    def switch_to_new_tab(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])

    def verify_cc_page(self):
        self.verify_url('https://soft.reelly.io/book-presentation')
