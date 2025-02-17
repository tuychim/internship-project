# from selenium.webdriver.common.by import By
# from pages.base_page import Page
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# MARKET_BTN = (By.XPATH, '//div[text()="Market"]')
# ADD_COMPANY_BTN = (By.CSS_SELECTOR, "a[class='add-company-button w-inline-block']")
# PUBLISH_MY_COMPANY_BTN = (By.CSS_SELECTOR, "a[class='publish-button _1 w-button']")
#
#
# class AddCompanyPage(Page):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     def click_market(self):
#         WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(MARKET_BTN)
#         ).click()
#
#     def verify_page(self):
#         self.verify_url('https://soft.reelly.io/market-companies')
#
#     def click_add_company(self):
#         WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(ADD_COMPANY_BTN)
#                                              ).click()
#
#     def verify_the_right_page(self):
#         self.verify_url('https://soft.reelly.io/presentation-for-the-agency')
#
#     def verify_btn_available(self):
#         WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located(PUBLISH_MY_COMPANY_BTN)
#         )
