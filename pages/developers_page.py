from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import Page

DEVELOPERS_BTN = (By.CSS_SELECTOR, "div[wized='marketTagDevelopers']")
CLICK_MARKET = (By.CSS_SELECTOR, "a[href='/market-companies']")
LICENSE_TAG = (By.CSS_SELECTOR, "div[class='license-txt']")
LICENSE_BLOCK = (By.CSS_SELECTOR, "div[class='license-block']")


class DevelopersPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def click_market_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CLICK_MARKET)
        ).click()

    def verify_right_page(self):
        self.verify_url('https://soft.reelly.io/market-companies')

    def click_developers_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DEVELOPERS_BTN)
        ).click()

    def verify_license_tag(self):
        all_cards = self.wait.until(EC.visibility_of_all_elements_located(LICENSE_BLOCK))
        for card in all_cards:
            tag = card.find_element(*LICENSE_TAG)
            assert tag.text == 'License', f"Tag does not contain 'License'"

