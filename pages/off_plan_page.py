# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from pages.base_page import Page
#
#
# CLICK_SETTINGS = (By.CSS_SELECTOR, "a[href='/settings'] div[class='menu-button-text']")
# OFF_PLAN_BTN = (By.CSS_SELECTOR, "[class='menu-twobutton']")
# CLICK_FILTERS = (By.CSS_SELECTOR, "[wized='saleStatusFilter']")
# OUT_OF_STOCK_OPT = (By.XPATH,"//*[@value='Out of stock']")
# VERIFY_TAGS = (By.CSS_SELECTOR, "div[class='cards-properties']")
#
#
# # class OffPlanPage(Page):
# #     def __init__(self, driver):
# #         super().__init__(driver)
#
#     def click_off_plan_btn(self):
#         WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(OFF_PLAN_BTN)
#         ).click()
#
#     def verify_page(self)
#         self.verify_url('https://soft.reelly.io/')
#
#     def click_filters_btn(self):
#         WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(CLICK_FILTERS)
#         ).click()
#
#     def filter_by_out_of_stocks(self):
#         WebDriverWait(self.driver, 20).until(
#             EC.presence_of_element_located(OUT_OF_STOCK_OPT)
#         ).click()
#
#     def verify_out_of_stocks_tag(self):
#         tags = self.find_elements(*VERIFY_TAGS)
#
#         for tag in tags:
#             tag_text = tag.text
#             if 'out of stock' not in tag_text.lower():
#                 print(f'{tag_text} is not out of stock')
#             else:
#                 print(f'{tag_text} is out of stock')
