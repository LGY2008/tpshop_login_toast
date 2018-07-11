import os,sys

import pytest
sys.path.append(os.getcwd())
from base.base_driver import BaseDriver
from page.login_page import LoginPage
from base.base_yml import read_yml_data
class TestLogin():
    def setup(self):
        # 实例化 PageLogin
        self.login_page=LoginPage(BaseDriver())
        # 点击我的
        self.login_page.page_click_self_btn()
        # 点击 登录/注册
        self.login_page.page_click_login_reg_link()
        # 获取toast -->请先登录
        assert "请先登录" in self.login_page.page_get_toast("请先登录")
    # 点击登录
    @pytest.mark.parametrize("args",read_yml_data("login_data","test_login_up"))
    def test_login_up(self,args):
        # 输入用户名
        self.login_page.page_input_username(args["username"])
        # 输入密码
        self.login_page.page_input_password(args["password"])
        # 点击登录
        self.login_page.page_click_login_btn()
        print("登录完成！")