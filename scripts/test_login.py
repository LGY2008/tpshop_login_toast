import os,sys
sys.path.append(os.getcwd())
from base.base_driver import BaseDriver
from page.login_page import LoginPage
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
    def test_login_up(self):
        # 输入用户名
        self.login_page.page_input_username("18610453007")
        # 输入密码
        self.login_page.page_input_password("123456")
        # 点击登录
        self.login_page.page_click_login_btn()