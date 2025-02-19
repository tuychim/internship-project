from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def add_input(self, by: By, value: str, text: str):
        field = self.driver.find_element(by=by, value=value)
        field.send_keys(text)
        sleep(1)

    def login(self, username: str, password: str):
        self.input(by=By.ID, value='email-2', text=username)
        self.input(by=By.ID, value='field', text=password)
        self.click_button(by=By.CLASS_NAME, value='login-button w-button')

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(*locator),
            f'Element not clickable by {locator}'
        ).click()

    def select_dropdown_value(self, value, *locator):
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        select.select_by_visible_text(value)

    def get_dropdown_value(self, value, *locator):
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        selected_text = select.first_selected_option.text
        assert value == selected_text, f"Expected {value} but got {selected_text}"

    def checkbox_click(self, *locator):
        checkbox_element = self.driver.find_element(*locator)
        if checkbox_element.is_selected() != True:
            checkbox_element.click()

    def is_checkbox_selected(self, *locator):
        checkbox_element = self.driver.find_element(*locator)
        assert checkbox_element.is_selected() == True, f"Checkbox needs to selected!"

    def wait_until_visible(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(*locator),
            f'Element not visible by {locator}'
        )

    def wait_until_disappears(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(*locator),
            f'Element still visible by {locator}'
        )

    def get_current_window(self):
        current_window = self.driver.current_window_handle
        print('Current:', current_window)
        print('ALL windows:', self.driver.window_handles)
        return current_window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles  # [Win1, Win2, ...]
        print('ALL windows:', self.driver.window_handles)
        print('Switching to... ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_window_by_id(self, window_id):
        print('Switching to... ', window_id)
        self.driver.switch_to.window(window_id)

    def verify_attribute_value(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).get_attribute("value")
        assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text , f'Expected {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url), message=f'Url does not contain {expected_partial_url}')

    def verify_url(self, expected_url):
        self.wait.until(EC.url_matches(expected_url), message=f'Url does not contain {expected_url}')

    def verify_input_field_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).get_attribute("value")
        assert actual_text == expected_text, f'{actual_text} != {expected_text}'

    def save_screenshot(self, name):
        self.driver.save_screenshot(f'{name}.png')

    def close(self):
        self.driver.close()

    def input(self, by, value, text):
        pass

    def click_button(self, by, value):
        pass