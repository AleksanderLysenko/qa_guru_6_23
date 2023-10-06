import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser
import os

import project


@pytest.fixture(scope='function')
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformVersion": "9.0",
        "deviceName": "Huawei P30",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "qa_guru_6_23",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack_6_23",

            # Set your access credentials
            "userName": project.config.browserstack_username,
            "accessKey": project.config.browserstack_accesskey,
        }
    })

    browser.config.driver = webdriver.Remote(project.config.remote_url, options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
