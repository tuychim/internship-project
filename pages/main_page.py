from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page
from time import sleep


class MainPage(Page):

    def open_main(self):
        self.open("https://soft.reelly.io/sign-in")
        sleep(3)

    def verify_page(self):
        self.verify_url('https://soft.reelly.io/')
