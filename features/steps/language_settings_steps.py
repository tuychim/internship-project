from behave import given, when, then


@given('Open the main page')
def open_the_main_page(context):
    context.app.main_page.open_main()


@when('Log in to the page')
def login_to_the_page(context):
    context.app.language_settings.login_page()


@when('Click on Main menu')
def click_on_main_menu(context):
    context.app.language_settings.click_on_main_menu()


@when('Change the language of the page to Russian. The option will be “RU” which is the list of the languages')
def change_language(context):
    context.app.language_settings.change_language()


@then('Verify the language has changed')
def verify_language(context):
    assert context.app.language_settings.verify_language()
