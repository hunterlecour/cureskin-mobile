from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.firefox.service import Service as Firefox_Service
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    # # CHROME DRIVER
    # service = Chrome_Service(executable_path=ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service)

    # HEADLESS MODE ####
    # CHROME
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )

    # FIREFOX DRIVER
    # service = Firefox_Service(executable_path=GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(service=service)

    # # HEADLESS MODE ####
    # # FIREFOX
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Firefox(
    #     options=options, service=service
    # )

    # BROWSER STACK #

    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'hunterlecour_hWPdTv'
    # bs_key = 'pXs7ZT4NHsRbZkCJgmMV'
    #
    # desired_cap = {
    #     'browserName': 'Firefox',
    #     'bstack:options': {
    #         'os': 'OS X',
    #         'osVersion': 'Ventura',
    #         'sessionName': test_name
    #     }
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    #
    ## Mobile Web Emulator ##
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    #
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver= context.driver)


def before_scenario(context, scenario):
    print('\nStarted step: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()