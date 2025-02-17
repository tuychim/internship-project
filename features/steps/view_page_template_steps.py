from behave import given, when, then


@given('Open the main page.')
def open_the_main_page(context):
    context.app.main_page.open_main()


@given('Log in to the page')
def login_to_the_page(context):
    context.app.view_page_template.login_page()


@when('Click on “market” at the left side menu')
def click_market(context):
    context.app.view_page_template.click_market()


@when('Verify the right page open')
def verify_page(context):
    context.app.view_page_template.verify_page()


@when('Click on “Add Company” button.')
def click_add_company(context):
    context.app.view_page_template.click_add_company()


@when('Verify the right page opens.')
def verify_the_right_page(contex):
    contex.app.view_page_template.verify_the_right_page()


@then('Scroll down and click on the button “View Page Template”')
def click_view_page_template(context):
    context.app.view_page_template.click_view_page_template()


@then('Verify the button “Send my CV” button is available.')
def verify_send_my_cv(context):
    context.app.view_page_template.verify_send_my_cv()

