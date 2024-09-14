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


@when('User enters project details')
def step_impl(context):
    context.app.add_project.enter_name('Tim Tim')
    context.app.add_project.enter_project_company('Dream Team')
    context.app.add_project.enter_company_role('CEO')
    context.app.add_project.enter_company_age()
    context.app.add_project.enter_project_country('USA')
    context.app.add_project.enter_project_name('Project X')
    context.app.add_project.enter_company_phone_number('555-666-7788')
    context.app.add_project.enter_company_email('test@dreamteam.com')


@then('Verify the right information is present in the input fields')
def step_impl(context):
    context.app.add_project.verify_right_information(
        expected_name='Tim Tim',
        expected_company='Dream Team',
        expected_role='CEO',
        expected_age='6',
        expected_country='USA',
        expected_project_name='Project X',
        expected_phone='555-666-7788',
        expected_email='test@dreamteam.com'
    )


@then('Verify “Send an application” button is available and clickable.')
def verify_app_button_clickable(context):
    context.app.add_project.send_app_btn()

