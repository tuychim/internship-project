from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_up_page import SignUpPage
from pages.language_settings import LanguageSettings
from pages.developers_page import DevelopersPage
from pages.product_detail import ProductDetail
from pages.market_page import MarketPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_up_page = SignUpPage(driver)
        self.language_settings = LanguageSettings(driver)
        self.developers_page = DevelopersPage(driver)
        self.product_detail = ProductDetail(driver)
        self.market_page = MarketPage(driver)







