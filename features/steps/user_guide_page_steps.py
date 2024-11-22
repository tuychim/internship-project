from behave import given, when, then


@given('Open the main page.')
def open_main(contex):
    contex.app.main_page.open_main()


@given('Sign in')
def sign_in(context):
    context.app.main_page.login_page()


@when('Click on settings option.')
def click_settings(contex):
    contex.app.user_guide_page.click_settings()


@when('Click on User Guide option.')
def click_user_guide(contex):
    contex.app.user_guide_page.click_user_guide()


@when('Verify the right page opens.')
def verify_page(context):
    context.app.user_guide_page.verify_page()


@then('Verify all lesson videos contain titles')
def verify_videos(context):
    context.app.user_guide_page.verify_videos()

