from selenium.webdriver.common.by import By
from behave import given, when, then

from pages.base_page import Page
from time import sleep


LOGIN_INPUT = (By.ID, "email-2")
PASSWORD_INPUT = (By.ID, "field")
SUBMIT_BUTTON = (By.CSS_SELECTOR, ".login-button")
CLICK_BUTTON = (By.CSS_SELECTOR, ".menu-twobutton")
VERIFY_RIGHT_PAGE = (By.CSS_SELECTOR, ".page-title")
CLICK_FILTER = (By.CSS_SELECTOR, ".filter-button")
CLICK_LAST_UNIT = (By.XPATH, "//div[@wized='priorityStatusLastUnits']")
VERIFY_TAG = (By.CSS_SELECTOR, 'div[class="commision_box"] [class="_5-comission"]')


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main()


@when('Log in to the page')
def login_page(context):
    context.driver.find_element(*LOGIN_INPUT).send_keys('tuychi.m@gmail.com')
    context.driver.find_element(*PASSWORD_INPUT).send_keys('passwordtest')
    context.driver.find_element(*SUBMIT_BUTTON).click()
    sleep(6)


@when('Click on “off plan” at the left side menu')
def click_on_off(context):
    context.driver.find_element(*CLICK_BUTTON).click()
    sleep(4)


@when('Verify the right page opens')
def verify_page(context):
    context.app.main_page.verify_page()


@when('Filter by sale status of “Last Units”')
def filter_by_last_units(context):
    context.driver.find_element(*CLICK_FILTER).click()
    context.driver.find_element(*CLICK_LAST_UNIT).click()
    sleep(6)


@then('Verify each product contains the Last Units tag')
def verify_last_units(context):
    actual_text = context.driver.find_element(*VERIFY_TAG).text
    assert actual_text == "Last units", f"Expected text 'Last units', but got '{actual_text}'"
