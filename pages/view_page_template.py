from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_INPUT = (By.ID, "email-2")
PASSWORD_INPUT = (By.ID, "field")
SUBMIT_BUTTON = (By.CSS_SELECTOR, ".login-button")
MARKET_BTN = (By.XPATH, '//div[text()="Market"]')
ADD_COMPANY_BTN = (By.CSS_SELECTOR, "a[class='add-company-button w-inline-block']")
VIEW_PAGE_TEMPLATE = (By.CSS_SELECTOR, "a[id='w-node-bba0a7a4-1591-cf54-faa7-fd823cb0c215-7f66df39']")
SEND_MY_CV_BTN = (By.CSS_SELECTOR, "a[href='#HR-manager']")


class ViewPageTemplate(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def login_page(self):
        self.driver.find_element(*LOGIN_INPUT).send_keys('tuychi.m@gmail.com')
        self.driver.find_element(*PASSWORD_INPUT).send_keys('passwordtest')
        self.driver.find_element(*SUBMIT_BUTTON).click()

    def click_market(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MARKET_BTN)
        ).click()

    def verify_page(self):
        self.verify_url('https://soft.reelly.io/market-companies')

    def click_add_company(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ADD_COMPANY_BTN)
        ).click()

    def verify_the_right_page(self):
        self.verify_url('https://soft.reelly.io/presentation-for-the-agency')

    def click_view_page_template(self):
        view_template_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(VIEW_PAGE_TEMPLATE)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", view_template_btn)
        view_template_btn.click()

    def verify_send_my_cv(self):
        send_cv_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEND_MY_CV_BTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", send_cv_btn)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(SEND_MY_CV_BTN)
        )
