from behave import given, when, then


@given('Open sign in page')
def open_signin_page(context):
    context.app.main_page.open_main()


@when('Log in to the page.')
def login_page(context):
    context.app.connect_company.login_page()


@when('Click on “Connect the company"')
def click_connect_company(context):
    context.app.connect_company.click_connect_company()


@when('Switch the new tab.')
def switch_to_company(context):
    context.app.connect_company.switch_to_new_tab()


@then('Verify the right tab opens')
def verify_cc_page(context):
    context.app.connect_company.verify_cc_page()

