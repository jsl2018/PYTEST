import sys
# import os

import pytest

# sys.path.append(os.getcwd())
from base.base_read_data import ReadLoginYaml
from page.page_logan import PageLogan
from base.get_driver import get_driver


def get_data():
    list = []
    for data in ReadLoginYaml("data_login.yaml").read_login_yaml().values():
        list.append((data.get("username"), data.get("password")))
    return list

class TestLogin():
    def setup_class(self):
        self.login = PageLogan(get_driver())
        self.login.page_click_wo()
        self.login.page_click_login()

    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("username, password", get_data())
    def test_login(self, username, password):
        # self.login.page_click_wo()
        # self.login.page_click_login()
        self.login.page_input_username(username)
        self.login.page_input_password(password)
        self.login.page_click_denglu()
        print(get_data())
