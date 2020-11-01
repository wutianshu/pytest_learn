from page_objects import PageObject, PageElement
import time
from ..common.cookie import cookie_to_selenium_format


class BasePage(PageObject):
    target_page = ''

    def __init__(self, driver, session):
        self.driver = driver
        self.session = session
        self.login()

    def login(self):
        self.driver.get(self.target_page)
        self.driver.delete_all_cookies()
        all_cookie = self.session.cookies._cookies[".djtest.cn"]["/"]
        for k, v in all_cookie.items():
            self.driver.add_cookie(cookie_to_selenium_format(v))
        self.driver.get(self.target_page)

    def wait(self, sec):
        time.sleep(sec)
