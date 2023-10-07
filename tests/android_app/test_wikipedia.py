import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search(mobile_management):

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_no_search(mobile_management):

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('ewewewewewewew')

    with allure.step('Verify content no found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.no.size_greater_than(0))
        results.first.should(have.no.text('ewewewewewewew'))


def test_open_article(mobile_management):

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Impressionism')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Impressionism'))

    with allure.step('Open article'):
        results.element_by(have.text('Impressionism')).click()
        with allure.step('Error occured'):
            error = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_wiki_error_text'))
            error.should(have.text("An error occurred"))
