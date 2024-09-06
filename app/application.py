from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_up_page import SignUpPage
from pages.settings_page import SettingsPage
from pages.language_settings import LanguageSettings


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_up_page = SignUpPage(driver)
        self.settings_page = SettingsPage(driver)
        self.language_settings = LanguageSettings(driver)







