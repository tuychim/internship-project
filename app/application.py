from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_up_page import SignUpPage
from pages.language_settings import LanguageSettings
from pages.product_detail import ProductDetail
from pages.market_page import MarketPage
from pages.verify_settings_page import SettingsPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_up_page = SignUpPage(driver)
        self.language_settings = LanguageSettings(driver)
        self.product_detail = ProductDetail(driver)
        self.market_page = MarketPage(driver)
        self.verify_settings_page = SettingsPage(driver)







