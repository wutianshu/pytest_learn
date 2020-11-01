from jzvisitTest.pages.jzvisit_task_list_page import TaskListPage


class TestOne():
    def test_1(self, driver, houtai_session):
        page = TaskListPage(driver, houtai_session)
        assert page.get_project_name() == '查询'
