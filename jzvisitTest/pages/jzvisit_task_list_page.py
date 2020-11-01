from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import os


class TaskListPage(BasePage):
    PROJECT_NAME_LOCATOR = '//*[@id="search_form"]/span/div[14]/span/button[2]/span/span[1]'
    target_page = os.environ.get('jzvisit_url')

    def get_project_name(self):
        try:
            project_name = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.PROJECT_NAME_LOCATOR)))
            return project_name.get_attribute("innerHTML")
        except TimeoutError:
            raise TimeoutError('Run time out')
