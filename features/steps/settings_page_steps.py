from behave import given, when, then

from pages.base_page import Page


@given('Open sign in page')
def open_signin_page(context):
    context.app.main_page.open_main()


@when('Log in to the page')
def login_page(context):
    context.app.settings_page.login_page()


@when('Click on settings option')
def click_on_settings(context):
    context.app.settings_page.click_on_settings()


@when('Click on Edit profile option')
def click_edit_profile(context):
    context.app.settings_page.click_edit_profile()


@when('Enter test data into the name field')
def input_name(contex):
    contex.app.settings_page.input_name()


@when('Enter test data into the phone number field')
def input_phone(contex):
    contex.app.settings_page.input_phone()


@then('Check the right information is present in the name input fields')
def verify_input_name(context):
    context.app.settings_page.verify_input_name()


@then('Check the right information is present in the phone number input field')
def verify_input_phone(context):
    context.app.settings_page.verify_input_phone()


@then('Check “Save Changes” button is available and clickable')
def click_save_changes_btn(context):
    context.app.settings_page.click_save_changes_btn()


@then('Check “Close” button is available and clickable')
def click_close_btn(context):
    context.app.settings_page.click_close_btn()

