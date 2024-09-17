from behave import given, when, then


@given('Open the main page.')
def open_main(contex):
    contex.app.main_page.open_main()


@given('Sign in')
def sign_in(context):
    context.app.main_page.login_page()


@when('Click on settings option.')
def click_settings(contex):
    contex.app.community_page.click_settings()


@when('Click on Community option.')
def click_community_btn(contex):
    contex.app.community_page.click_community_btn()


@when('Verify the right page opens.')
def verify_page(context):
    context.app.community_page.verify_page()


@then('Verify “Contact support” button is available and clickable.')
def verify_support_button(context):
    context.app.community_page.verify_support_button()

