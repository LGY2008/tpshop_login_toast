import os,sys

import allure
import pytest
sys.path.append(os.getcwd())
from base.base_driver import BaseDriver
from page.login_page import LoginPage
from base.base_yml import read_yml_data
class TestLogin():
    @allure.step(title="开始测试tpshop应用")
    def setup(self):
        # 实例化 PageLogin
        self.login_page=LoginPage(BaseDriver())
        # 点击我的
        allure.attach('点击按钮-》 ','我的 ')
        self.login_page.page_click_self_btn()
        # 点击 登录/注册
        allure.attach("点击按钮-》登录/注册"," ")
        self.login_page.page_click_login_reg_link()
        # 获取toast -->请先登录
        allure.attach("断言toast是否为：请先登录"," ")
        assert "请先登录" in self.login_page.page_get_toast("请先登录")
        # 截图
        self.login_page.base_get_screenshot("toast_first_login_no")
    # 点击登录
    @pytest.mark.parametrize("args",read_yml_data("login_data","test_login_up"))
    @allure.step(title="登录操作")
    @pytest.allure.severity( pytest.allure.severity_level.CRITICAL )
    def test_login_up(self,args):
        username=args["username"]
        password=args["password"]
        imgname=args["toast_login_ok"]
        # 输入用户名
        allure.attach("输入用户名",username)
        self.login_page.page_input_username(username)
        # 输入密码
        allure.attach("输入密码",password)
        self.login_page.page_input_password(password)
        # 点击登录
        allure.attach("点击登录按钮"," ")
        self.login_page.page_click_login_btn()

        # 断言登录成功 toast
        assert "登录成功" in self.login_page.page_get_toast("登录成功")
        # 截图
        self.login_page.base_get_screenshot(imgname)
        # 上传图片
        allure.attach("图片",open("./image/"+imgname+".png","rb").read(),allure.attach_type.PNG)