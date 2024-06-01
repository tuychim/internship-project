from selenium.webdriver.common.by import By
from behave import given, when, then

from pages.base_page import Page


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main()


@when('Log in to the page')
def login_page(context):
    context.app.main_page.login_page()


@when('Click on “off plan” at the left side menu')
def click_on_off(context):
    context.app.main_page.click_on_off()


@when('Verify the right page opens')
def verify_page(context):
    context.app.main_page.verify_page()


@when('Filter by sale status of “Last Units”')
def filter_by_last_units(context):
    context.app.main_page.filter_by_last_units()


@then('Verify each product contains the Last Units tag')
def verify_last_units(context):
    context.app.main_page.verify_last_units()


