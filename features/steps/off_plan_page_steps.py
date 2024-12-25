from behave import given, when, then


@given('Open the main page.')
def open_main(context):
    context.app.main_page.open_main()


@given('Sign in')
def sign_in(context):
    context.app.main_page.login_page()


@when('Click on “off plan” at the left side menu')
def click_off_plan_btn(context):
    context.app.off_plan_page.click_off_plan_btn()


@when('Verify the right page opens.')
def verify_page(context):
    context.app.off_plan_page.verify_page()


@when('Click on Filters')
def click_filters_btn(context):
    context.app.off_plan_page.click_filters_btn()


@when('Filter by sale status of “Out of Stocks"')
def filter_by_out_of_stocks(context):
    context.app.off_plan_page.filter_by_out_of_stocks()


@then('Verify each product contains the Out of Stocks tag')
def verify_out_of_stocks_tag(context):
    context.app.off_plan_page.verify_out_of_stocks_tag()
