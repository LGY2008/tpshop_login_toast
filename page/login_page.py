from selenium.webdriver.common.by import By

from base.base_init import BaseInit

# 数据暂时先放到此地方
loc_self_btn=By.XPATH,"//*[contains(@text,'我的')]"
loc_login_reg=By.XPATH,"//*[contains(@text,'登录/注册')]"
loc_login_username=By.ID,"com.tpshop.malls:id/edit_phone_num"
loc_login_password=By.ID,"com.tpshop.malls:id/edit_password"
loc_click_login_btn=By.ID,"com.tpshop.malls:id/btn_login"

class LoginPage(BaseInit):
    # 点击我的
    def page_click_self_btn(self):
        self.base_click(loc_self_btn)
    # 点击登录/注册
    def page_click_login_reg_link(self):
        self.base_click(loc_login_reg)
    # 输入用户名
    def page_input_username(self,username):
        self.base_input_text(loc_login_username,username)
    # 输入密码
    def page_input_password(self,password):
        self.base_input_text(loc_login_password,password)
    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(loc_click_login_btn)
    # 获取toast
    def page_get_toast(self,message):
        message="//*[contains(@text,'"+message+"')]"
        return self.base_find_toast((By.XPATH,message)).text