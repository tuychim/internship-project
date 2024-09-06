from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

LOGIN_INPUT = (By.ID, "email-2")
PASSWORD_INPUT = (By.ID, "field")
SUBMIT_BUTTON = (By.CSS_SELECTOR, ".login-button")
CLICK_MAIN_BTN = (By.CSS_SELECTOR, "a[href='/main-menu']")
LANGUAGE_SELECTOR = (By.ID, "w-dropdown-toggle-0")
RU_BTN = (By.XPATH, "//a[text()='RU']")


class LanguageSettings(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def login_page(self):
        self.driver.find_element(*LOGIN_INPUT).send_keys('tuychi.m@gmail.com')
        self.driver.find_element(*PASSWORD_INPUT).send_keys('passwordtest')
        self.driver.find_element(*SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CLICK_MAIN_BTN)
        )

    def click_on_main_menu(self):
        self.driver.find_element(*CLICK_MAIN_BTN).click()

    def change_language(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LANGUAGE_SELECTOR)
        )

        self.click(*LANGUAGE_SELECTOR)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RU_BTN)
        )

        self.click(*RU_BTN)

    def verify_language(self):
        actual_text = self.find_element(*LANGUAGE_SELECTOR).text
        expected_text = 'RU'

        assert expected_text == actual_text, f'Error: expected {expected_text}, but got {actual_text}'

        return True

