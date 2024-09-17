from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep

CLICK_SETTINGS = (By.CSS_SELECTOR, "a[href='/settings'] div[class='menu-button-text']")
CLICK_COMMUNITY_BTN = (By.XPATH, '//div[@class="setting-text" and text()="Community"]')
NAME_TEXT_BOX = (By.ID, 'Your-name')
SUPPORT_BTN = (By.ID, "w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf-7f66deba")


class CommunityPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def click_settings(self):
        self.driver.find_element(*CLICK_SETTINGS).click()
        sleep(3)

    def click_community_btn(self):
        self.driver.find_element(*CLICK_COMMUNITY_BTN).click()
        sleep(2)

    def verify_page(self):
        self.verify_url('https://soft.reelly.io/community')

    def verify_support_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SUPPORT_BTN)
        )
        support_button = self.driver.find_element(*SUPPORT_BTN)
        assert support_button.is_displayed(), "Support button is not visible on the page"
