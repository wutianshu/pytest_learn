from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import os

class ClouderPage(BasePage):
    # QUERY_TEXT_LOCATOR = '/html/body/div/form/div[4]/div/div[1]/input'
    QUERY_TEXT_LOCATOR = "input[autocomplete='off'][placeholder='请输入订单编号、客户姓名或者手机号码进行搜索']"
    QUERY_BUTTON_LOCATOR = '/html/body/div/form/div[4]/div/button'
    DATA_COUNT_LOCATOR = '/html/body/div/form/div[4]/div/div[2]/div[1]/div[2]/span[1]'
    target_page = os.environ.get('cloudkeeper_url')

    def input_query_text(self,key_word):
        try:
            query_tex_obj = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.QUERY_TEXT_LOCATOR)))
        except TimeoutError:
            raise TimeoutError('Run time out')
        query_tex_obj.send_keys(key_word)

    def query(self):
        try:
            query_button_obj = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.QUERY_BUTTON_LOCATOR)))
        except TimeoutError:
            raise TimeoutError('Run time out')
        query_button_obj.click()

    def get_count_info(self):
        try:
            data_count_obj = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.DATA_COUNT_LOCATOR)))
        except TimeoutError:
            raise TimeoutError('Run time out')
        return data_count_obj.get_attribute("innerHTML")
