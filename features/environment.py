from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application

#  Run Behave tests with Allure results
#behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/


def browser_init(context, scenario_name):

    """
    :param context: Behave context
    """

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### Chrome HEADLESS MODE ###
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument("--window-size=1920,1080")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### Firefox HEADLESS MODE ###
    # options = webdriver.FirefoxOptions()
    # options.add_argument('headless')
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'tuychim_BCR4o2'
    # bs_key = '2RsxhhcnZw44SbRHw2p1'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Monterey',
    #     'browserName': 'Safari',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(6)
    context.wait = WebDriverWait(context.driver, timeout=15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        # context.app.base_page.save_screenshot(step)


def after_scenario(context, feature):
    context.driver.quit()
