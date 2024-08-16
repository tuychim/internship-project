from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from pages.base_page import Page


@given('Open the registration page or sign up page')
def open_sign_up_page(context):
    context.app.main_page.open_main()


@when('Enter some test information in the input fields.')
def enter_some_test_information(context):
    context.app.sign_up_page.signup()
    sleep(8)


@then('Verify the right information is present.')
def verify_the_information(context):
    context.app.sign_up_page.verify_the_right_information()
