from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep


FULL_NAME = (By.ID, "Full-Name")
PHONE = (By.ID, "phone2")
EMAIL = (By.ID, "Email-3")
PASSWORD = (By.ID, "field")
COMPANY_NAME = (By.ID, "Company-website")
ROLE = (By.ID, "Role")
POSITION = (By.ID, "Position")
COUNTRY = (By.ID, "country-select")
COMPANY_SIZE = (By.ID, "Agents-amount-2")
#PRIVACY_POLICY_CHECKBOX = (By.ID, "checkbox")
#CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".login-button")


class SignUpPage(Page):

    def signup(self):
        self.driver.find_element(*FULL_NAME).send_keys('Johny Johny')
        self.driver.find_element(*PHONE).send_keys('1234567890')
        self.driver.find_element(*EMAIL).send_keys('test@test.com')
        self.driver.find_element(*PASSWORD).send_keys('testpassword')
        self.driver.find_element(*COMPANY_NAME).send_keys('testcompany')
        self.driver.find_element(*COUNTRY).send_keys('United States of America')
        self.driver.find_element(*COMPANY_SIZE).send_keys('5-10')

    def verify_the_right_information(self):
        self.verify_attribute_value('Johny Johny', *FULL_NAME)
        self.verify_attribute_value('1234567890', *PHONE)
        self.verify_attribute_value('test@test.com', *EMAIL)
        self.verify_attribute_value('testpassword', *PASSWORD)
        self.verify_attribute_value('testcompany', *COMPANY_NAME)
        self.verify_attribute_value('United States of America', *COUNTRY)
        self.verify_attribute_value('5-10', *COMPANY_SIZE)