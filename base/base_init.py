from selenium.webdriver.support.wait import WebDriverWait


class BaseInit:
    def __init__(self,driver):
        self.driver=driver
    def base_find_element(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    def base_find_elements(self, loc,timeout=5,poll=0.5):
        return WebDriverWait( self.driver,timeout,poll ).until( lambda x: x.find_elements( *loc ) )
    def base_click(self,loc):
        self.base_find_element(loc).click()
    def base_input_text(self,loc,text):
        self.base_find_element(loc).send_keys(text)
    # 定义 toast
    def base_find_toast(self,loc):
        return self.base_find_element(loc,poll=0.01)
    def base_get_screenshot(self,filename):
        self.driver.get_screenshot_as_file("./image/"+filename+".png")