from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

# Define selectors for the page elements
CLICK_SETTINGS = (By.CSS_SELECTOR, "a[href='/settings'] div[class='menu-button-text']")
OFF_PLN_BTN = (By.CSS_SELECTOR, "[class='menu-twobutton']")
CLICK_FILTERS = (By.CSS_SELECTOR, "[id='Location-2']")
OUT_OF_STOCK = (By.ID, "Location-2")
VERIFY_TAGS = (By.CSS_SELECTOR, "div[wized='projectStatus']")


class OffPlanPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def click_off_plan_btn(self):
        # Wait for the 'Off Plan' button to be clickable and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OFF_PLN_BTN)
        ).click()

    def verify_page(self):
        # Verify that the correct page URL is open
        self.verify_url('https://soft.reelly.io/')

    def click_filters_btn(self):
        # Wait for the 'Filters' button to be clickable and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CLICK_FILTERS)
        ).click()

    def filter_by_out_of_stocks(self):
        # Select "Out of stock" from the dropdown
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OUT_OF_STOCK)
        )
        select = Select(dropdown)
        select.select_by_visible_text("Out of stock")
        # Wait for the tags to appear after the filter is applied
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(VERIFY_TAGS)
        )

    def verify_out_of_stocks_tag(self, expected_text="Out of stock"):
        # Wait for the tags to be visible and present in the DOM
        tags = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(VERIFY_TAGS)
        )

        # Ensure that tags are found
        assert tags, "No elements found with the 'Out of stock' tag."

        # Iterate through each tag and verify the text
        for tag in tags:
            tag_text = tag.text.strip()  # Get the tag text and remove any extra spaces

            # Debugging information: Print the tag's outer HTML if the text is empty
            if not tag_text:
                print(f"Tag has no visible text. Full HTML: {tag.get_attribute('outerHTML')}")

            print(f"Tag text found: '{tag_text}'")  # For debugging

            # Verify that the tag text matches the expected text
            assert tag_text == expected_text, f"Expected text '{expected_text}', but got '{tag_text}'"
