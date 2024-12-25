from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

FIRST_PRODUCT = (By.CSS_SELECTOR, "div[class='project-image']")
VISUALIZATION_OPTIONS = (By.CSS_SELECTOR, "div[class*='tabs-menu-project']")
ARCHITECTURE_LOCATOR = (By.CSS_SELECTOR, "a[class*='tab']")
LOBBY_LOCATOR = (By.CSS_SELECTOR, "a[wized='lobbyTabProject']")


class ProductDetail(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def click_first_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(FIRST_PRODUCT)
        ).click()

    def verify_visualization_options(self):
        # Fetch text for the "Architecture" option
        architecture_option = self.driver.find_element(*ARCHITECTURE_LOCATOR).text.strip()

        # Fetch text for the "Lobby" option
        lobby_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LOBBY_LOCATOR)  # Pass the tuple directly
        ).text.strip()

        # Combine both options into a list
        actual_options = [architecture_option, lobby_option]

        # Expected visualization options
        expected_options = ["Architecture", "Lobby"]

        # Verify the options are as expected
        assert actual_options == expected_options, (
            f"Expected options {expected_options}, but found {actual_options}"
        )

    def verify_visualization_options_clickable(self):
        # Wait for the individual options to be clickable
        print("Waiting for clickable options...")  # Debugging statement
        options = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located(VISUALIZATION_OPTIONS)
        )

        # Ensure that each option is clickable (enabled)
        for option in options:
            assert option.is_enabled(), f"Option '{option.text.strip()}' is not clickable."

        print("All options are clickable.")


