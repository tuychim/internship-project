from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MARKET_BTN = (By.XPATH, '//div[text()="Market"]')
NEXT_BTN = (By.CSS_SELECTOR, '[wized="nextPageMarket"]')
PREV_BTN = (By.CSS_SELECTOR, "div[wized='previousPageMarket']")
TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageMarket"]')
CURRENT_PAGE = (By.CSS_SELECTOR, '[wized="currentPageMarket"]')


class MarketPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def click_market(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MARKET_BTN)
        ).click()

    def verify_page(self):
        expected_url = 'https://soft.reelly.io/market-companies'
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    def go_to_final_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # Wait for the TOTAL_PAGES element to be visible and get its text
        try:
            total_pages_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TOTAL_PAGES)
            )
            total_number_of_pages = int(total_pages_element.text.strip())
        except Exception as e:
            raise ValueError(f"Failed to retrieve total number of pages: {e}")

        print(f'Total number of pages: {total_number_of_pages}')

        page = 1
        while page < total_number_of_pages:
            print(f'Navigating to page {page + 1}')
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(NEXT_BTN)
            ).click()
            page += 1
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(CURRENT_PAGE, str(page))
            )

        print("Reached the last page.")

    def go_to_first_page(self):
        try:
            current_page_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(CURRENT_PAGE)
            )
            current_page = int(current_page_element.text.strip())
        except Exception as e:
            raise ValueError(f"Failed to retrieve current page number: {e}")

        while current_page > 1:
            print(f"Currently on page {current_page}. Go to the previous page.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PREV_BTN)
            ).click()
            current_page -= 1
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(CURRENT_PAGE, str(current_page))
            )

        print("Reached the first page.")
