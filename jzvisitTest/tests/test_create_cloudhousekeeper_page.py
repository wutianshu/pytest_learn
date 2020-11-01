from jzvisitTest.pages.create_cloudhousekeeper_page import ClouderPage
import pytest
from ..common.pytest_ddt import read_data_from_json_yaml


# class TestOne():
#     @pytest.mark.parametrize('phone,expect_num',
#                              [('15377319326', '4'), ('15377319327', '0'), ('15377319328', '4'), ('15377319329', '4')])
#     def test_1(self, driver, houtai_session, phone, expect_num, ):
#         page = ClouderPage(driver, houtai_session)
#         page.input_query_text(phone)
#         page.query()
#         page.wait(2)
#         assert expect_num in page.get_count_info()


class TestOne():
    @pytest.mark.parametrize('phone,expect_num', read_data_from_json_yaml('../ddts/create_cloudhousekeeper.json'))
    def test_1(self, driver, houtai_session, phone, expect_num):
        page = ClouderPage(driver, houtai_session)
        page.input_query_text(phone)
        page.query()
        page.wait(2)
        assert expect_num in page.get_count_info()
