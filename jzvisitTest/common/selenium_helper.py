from selenium import webdriver


class SeleniumHelper(object):
    @staticmethod
    def initial_driver(browser_name='chrome'):
        browser_name = browser_name.lower()
        if browser_name == 'chrome':
            browser = webdriver.Chrome()
        elif browser_name in ('firefox', 'ff'):
            browser = webdriver.Firefox()
        else:
            browser = webdriver.Chrome()
        browser.maximize_window()
        browser.implicitly_wait(60)
        return browser
