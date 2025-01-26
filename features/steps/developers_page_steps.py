from behave import given, when, then


@given('Open the main page.')
def open_main(context):
    context.app.main_page.open_main()


@given('Sign in')
def login_page(context):
    context.app.main_page.login_page()


@when('Click on “market” at the left side menu')
def click_market_btn(context):
    context.app.developers_page.click_market_btn()


@when('Verify the right page opens')
def verify_right_page(context):
    context.app.developers_page.verify_right_page()


@when('Click on Developers filter at the top of the page')
def click_developers_btn(context):
    context.app.developers_page.click_developers_btn()


@then('Verify all cards has the license tag')
def verify_license_tag(context):
    context.app.developers_page.verify_license_tag()
