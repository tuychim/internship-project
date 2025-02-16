from behave import given, when, then


@given('Open the main page.')
def open_main(context):
    context.app.main_page.open_main()


@given('Sign in')
def login_page(context):
    context.app.main_page.login_page()


@when('Click on “settings” at the left side menu.')
def click_settings_btn(context):
    context.app.verify_settings_page.click_settings_btn()


@when('Click on the verification option.')
def click_verification_btn(context):
    context.app.verify_settings_page.click_verification_btn()


@when('Verify the right page opens.')
def verify_right_page(context):
    context.app.verify_settings_page.verify_right_page()


@then('Verify “upload image” and “Next step” buttons are available.')
def verify_two_btn_available(context):
    context.app.verify_settings_page.verify_two_btn_available()
