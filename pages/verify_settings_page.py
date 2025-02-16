from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


CLICK_SETTINGS = (By.CSS_SELECTOR, "a[href='/settings']")
VERIFICATION_BTN = (By.CSS_SELECTOR, "a[href='/verification/step-0']")
UPLOAD_IMAGE_BTN = (By.CSS_SELECTOR, "div[class='upload-button-2 w-embed']")
NEXT_STEP_BTN = (By.CSS_SELECTOR, "div[class='next-step--']")


class SettingsPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def click_settings_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CLICK_SETTINGS)
        ).click()

    def click_verification_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(VERIFICATION_BTN)
        ).click()

    def verify_right_page(self):
        self.verify_url('https://soft.reelly.io/verification/step-0')

    def verify_two_btn_available(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(UPLOAD_IMAGE_BTN)
                                             )
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(NEXT_STEP_BTN)
                                             )

