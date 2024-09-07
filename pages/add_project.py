from selenium.webdriver.common.by import By
from pages.base_page import Page

from time import sleep

CLICK_SETTINGS = (By.CSS_SELECTOR, "a[href='/settings'] div[class='menu-button-text']")
CLICK_ADD_PROJECT = (By.CSS_SELECTOR, "a[href='/add-a-project'] div[class='setting-text']")
NAME_TEXT_BOX = (By.ID, 'Your-name')
COMPANY_TEXT_BOX = (By.ID, 'Your-company-name')
ROLE_TEXT_BOX = (By.ID, 'Role')
COMPANY_AGE_INPUT = (By.ID, "Age-of-the-company")
PROJECT_COUNTRY_BOX = (By.ID, 'Country')
PROJECT_NAME_BOX = (By.ID, 'Name-project')
PHONE_NUMBER_BOX = (By.ID, 'Phone')
EMAIL_BOX = (By.ID, 'Email-add-project')
APPLICATION_BUTTON = (By.CSS_SELECTOR, "input[value='Send an application']")


class AddProject(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def click_settings(self):
        self.driver.find_element(*CLICK_SETTINGS).click()
        sleep(4)

    def click_add_project(self):
        self.driver.find_element(*CLICK_ADD_PROJECT).click()
        sleep(4)

    def verify_page(self):
        self.verify_url('https://soft.reelly.io/add-a-project')

    def enter_name(self, name):
        self.input_text(name, *NAME_TEXT_BOX)
        sleep(4)

    def enter_project_company(self, project_company):
        self.input_text(project_company, *COMPANY_TEXT_BOX)
        sleep(4)

    def enter_company_role(self, company_role):
        self.input_text(company_role, *ROLE_TEXT_BOX)
        sleep(4)

    def enter_company_age(self):
        self.find_element(*COMPANY_AGE_INPUT).send_keys('6')
        sleep(4)

    def enter_project_country(self, project_country):
        self.input_text(project_country, *PROJECT_COUNTRY_BOX)
        sleep(4)

    def enter_project_name(self, project_name):
        self.input_text(project_name, *PROJECT_NAME_BOX)
        sleep(4)

    def enter_company_phone_number(self, company_phone_number):
        self.input_text(company_phone_number, *PHONE_NUMBER_BOX)
        sleep(4)

    def enter_company_email(self, company_email):
        self.input_text(company_email, *EMAIL_BOX)
        sleep(4)

    def send_app_btn(self):
        self.click(*APPLICATION_BUTTON)
        sleep(4)