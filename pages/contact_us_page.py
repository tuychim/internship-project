from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


CLICK_SETTINGS = (By.CSS_SELECTOR, "a[href='/settings'] div[class='menu-button-text']")
CLICK_CONTACT_US_BTN = (By.CSS_SELECTOR, "a[href='/contact-us'] div[class='setting-text']")
SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, '.text-social')
VERIFY_COMPANY_PAGE = (By.XPATH, "//div[@class='get-free-period menu' and text()='Connect the company']")


class ContactUsPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def click_settings(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CLICK_SETTINGS)
        ).click()

    def click_contact_us_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CLICK_CONTACT_US_BTN)
        ).click()

    def verify_page(self):
        self.verify_url('https://soft.reelly.io/contact-us')

    def verify_social_media_icons(self, number):
        all_social = self.find_elements(*SOCIAL_MEDIA_ICONS)
        assert len(all_social) >= int(number), f'Error! Expected {number}, but got {len(all_social)}'

    def verify_connect_the_company(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(VERIFY_COMPANY_PAGE)
        )
        verify_connect_the_company = self.driver.find_element(*VERIFY_COMPANY_PAGE)
        assert verify_connect_the_company.is_displayed(), "Connect the company is not visible on the page"
