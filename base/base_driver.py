from appium import webdriver
def BaseDriver():
    # 声明 字典
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    # 获取 toast
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['deviceName'] = '192.168.67.101:5555'
    desired_caps['appPackage'] = 'com.tpshop.malls'
    desired_caps['appActivity'] = '.SPMainActivity'
    # 设置中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote( "http://127.0.0.1:4723/wd/hub", desired_caps )
    return driver