from behave import given, when, then


@given('Open the main page.')
def open_main(contex):
    contex.app.main_page.open_main()


@given('Sign in')
def sign_in(context):
    context.app.main_page.login_page()


@when('Click on settings option.')
def click_settings(contex):
    contex.app.contact_us_page.click_settings()


@when('Click on Contact us option')
def click_contact_us_btn(contex):
    contex.app.contact_us_page.click_contact_us_btn()


@when('Verify the right page opens.')
def verify_page(context):
    context.app.contact_us_page.verify_page()


@then('Verify there are at least {number} social media icons')
def verify_social_media_icons(context, number):
    context.app.contact_us_page.verify_social_media_icons(4)


@then('Verify “Connect the company” button is available and clickable')
def verify_connect_the_company(context):
    context.app.contact_us_page.verify_connect_the_company()

