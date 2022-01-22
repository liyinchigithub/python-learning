
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# test_appium.py
# appium for android


import time
import unittest

from appium import webdriver


class MyTests(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '10.0',  # 系统版本号
                        'deviceName': '4c50413241583398',  # 设备名称 在'设置->关于手机->设备名称'里查看 或 adb devices
                        # 'app':'',# 
                        # 'browserName':'Chrome',# 'Safari' 对应 iOS，'Chrome', 'Chromium', 或 'Browser' 则对应 Android
                        'appPackage': 'com.mt.mtxx.mtxx',  # apk的包名
                        'appActivity': 'com.mt.mtxx.mtxx.MainActivity',  # activity 名称
                        'noReset':True,# 在当前 session 下不会重置应用的状态。默认值为 false
                        'fullReset':False,# 在当前 session 下不会重置应用的状态。默认值为 false
                        'autoWebview':True ,# 直接转换到 Webview 上下文（context）。默认值为 false
                        'deviceReadyTimeout':5, # 用于等待模拟器或真机准备就绪的超时时间
                        'androidInstallTimeout':90000, # 用于等待在设备中安装 apk 所花费的时间（以毫秒为单位）。默认值为 90000
                        'unicodeKeyboard':False, # 使用 Unicode 输入法。 默认值为 false
                        'resetKeyboard':False, # 在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。如果单独使用，将会被忽略。默认值为 false
                        'noSign':False, # 跳过检查和对应用进行 debug 签名的步骤。仅适用于 UiAutomator，不适用于 selendroid。 默认值为 false
                        'adbPort':5037, # 	用来连接 ADB 服务器的端口（默认值为 5037）
                        'androidScreenshotPath':'/sdcard/screenshots/' # 	在设备中截图被保存的目录名。默认值为 /data/local/tmp
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium server
        self.driver.implicitly_wait(8)

    def test_(self):
        time.sleep(10);
        self.driver.find_element_by_accessibility_id('我').click();
        time.sleep(3);
        
    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()



if __name__=="__main__":
    MyTests.__name__
