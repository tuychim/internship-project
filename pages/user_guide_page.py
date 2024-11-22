from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


CLICK_SETTINGS = (By.CSS_SELECTOR, "a[href='/settings'] div[class='menu-button-text']")
CLICK_USER_GUIDE = (By.CSS_SELECTOR, "a[href='/user-guide'] div[class='setting-text']")
VERIFY_VIDEO = (By.XPATH, "//div[text()='Full overview of Reelly platform']")


class UserGuidePage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def click_settings(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CLICK_SETTINGS)
        ).click()

    def click_user_guide(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CLICK_USER_GUIDE)
            ).click()

    def verify_page(self):
        self.verify_url('https://soft.reelly.io/user-guide')

    def verify_videos(self):
        titles = self.driver.find_elements(*VERIFY_VIDEO)
        assert all(title.text.strip() != "" for title in titles), "Not all lesson videos have titles"
