from behave import given, when, then


@given('Open the main page.')
def open_main(contex):
    contex.app.main_page.open_main()


@given('Sign in')
def sign_in(context):
    context.app.main_page.login_page()


@when('Click on settings option.')
def click_settings(contex):
    contex.app.add_project.click_settings()


@when('Click on Add a project.')
def click_add_project(contex):
    contex.app.add_project.click_add_project()


@when('Verify the right page opens.')
def verify_page(context):
    context.app.add_project.verify_page()


@then('Enter name')
def enter_name(context):
    context.app.add_project.enter_name('Tim Tim')


@then('Enter company name')
def enter_company(context):
    context.app.add_project.enter_project_company('New Dream')


@then('Enter Role in the company')
def enter_company_role(context):
    context.app.add_project.enter_company_role('CEO')


@then('Enter Age of the company')
def enter_company_age(context):
    context.app.add_project.enter_company_age()


@then('Enter Country for placing the project')
def enter_project_country(context):
    context.app.add_project.enter_project_country("USA")


@then('Enter Name of the project to hos')
def enter_project_name(context):
    context.app.add_project.enter_project_name("New Jersey")


@then('Enter Phone')
def enter_company_phone_number(context):
    context.app.add_project.enter_company_phone_number("555-555-1234")


@then('Enter Email')
def enter_company_email(context):
    context.app.add_project.enter_company_email("testemail@gmail.com")


@then('Verify “Send an application” button is available and clickable.')
def verify_app_button_clickable(context):
    context.app.add_project.send_app_btn()
