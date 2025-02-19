from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_up_page import SignUpPage
from pages.product_detail import ProductDetail
#from pages.verify_settings_page import SettingsPage
#from pages.add_company_page import AddCompanyPage
from pages.view_page_template import ViewPageTemplate


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_up_page = SignUpPage(driver)
        self.product_detail = ProductDetail(driver)
        #self.verify_settings_page = SettingsPage(driver)
        #self.add_company_page = AddCompanyPage(driver)
        self.view_page_template = ViewPageTemplate(driver)







