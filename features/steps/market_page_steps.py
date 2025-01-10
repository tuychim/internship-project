from behave import given, when, then


@given('Open the main page')
def open_main(context):
    context.app.main_page.open_main()


@given('Sign in')
def login_page(context):
    context.app.main_page.login_page()


@when('Click on “market” at the left side menu.')
def click_market(context):
    context.app.market_page.click_market()


@when('Verify the right page opens.')
def verify_page(context):
    context.app.market_page.verify_page()


@when('Go to the final page using pagination.')
def go_to_final_page(context):
    context.app.market_page.go_to_final_page()


@then('Go to the first page using pagination.')
def go_to_first_page(context):
    context.app.market_page.go_to_first_page()
