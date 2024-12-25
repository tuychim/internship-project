from behave import given, when, then


@given('Open the main page,')
def open_main(context):
    context.app.main_page.open_main()


@given('Sign in.')
def sign_in(context):
    context.app.main_page.login_page()


@when('Click on “off plan” at the left side menu.')
def click_off_plan_btn(context):
    context.app.off_plan_page.click_off_plan_btn()


@when('Click on the first product')
def click_first_product(context):
    context.app.product_detail.click_first_product()


@when('Verify the three options of visualization are “architecture”, “lobby”')
def verify_visualization_options(context):
    context.app.product_detail.verify_visualization_options()


@then('Verify the visualization options are clickable.')
def visualization_options_clickable(context):
    context.app.product_detail.verify_visualization_options_clickable()
