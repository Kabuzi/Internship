from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, test_name):
    """
    :param test_name:
    :param context: Behave context
    """
    #service = Service('/Users/kkabu/Documents/Automation/Internship/chromedriver')
    #service = Service('/Users/kkabu/Documents/Automation/Internship/geckodriver')
    #context.driver = webdriver.Chrome(service=service)
    # context.driver = webdriver.Firefox(service=service)
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    # Browser Stack#
    bs_user = 'khumbomunthali1'
    bs_key = 'xoBy3JG4gAEgnKgvTZKA'

    desired_cap = {
        'browserName': 'Firefox',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'sessionName': test_name
        }
    }
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)

    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )

    # #HEADLESS FIREFOX#
    # options = Options()
    # options.headless = True
    # context.driver = webdriver.Firefox(service=service, options=options)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
