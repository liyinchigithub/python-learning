
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
                        'app':'/Users/liyinchi/workspace/python/python-learning/appium-android-unittest/apk/com.youdao.calculator-2.0.0.apk',# 
                        # 'browserName':'Chrome',# 'Safari' 对应 iOS，'Chrome', 'Chromium', 或 'Browser' 则对应 Android
                        'appPackage': 'com.youdao.calculator',  # apk的包名
                        'appActivity': 'com.youdao.calculator.activities.MainActivity',  # activity 名称
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
        
        self.driver.find_element_by_id('').click()
        
    # def test_calculator(self, t=500, n=4):
    #     """计算器测试"""
    #     time.sleep(3)# 等待3秒
    #     window = self.driver.get_window_size() #获取窗口大小
    #     x0 = window['width'] * 0.8  # 起始x坐标
    #     x1 = window['width'] * 0.2  # 终止x坐标
    #     y = window['height'] * 0.5  # y坐标
    #     for i in range(n):
    #         self.driver.swipe(x0, y, x1, y, t)# 滑动
    #         time.sleep(1)
    #     self.driver.find_element_by_id('com.youdao.calculator:id/guide_button').click()# 点击
    #     for i in range(6):
    #         self.driver.find_element_by_accessibility_id('Mathbot Editor').click()# 点击
    #         time.sleep(1)

    #     btn_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.View/android.widget.GridView/android.widget.FrameLayout[{0}]/android.widget.FrameLayout'
    #     self.driver.find_element_by_xpath(btn_xpath.format(7)).click()
    #     self.driver.find_element_by_xpath(btn_xpath.format(10)).click()
    #     self.driver.find_element_by_xpath(btn_xpath.format(8)).click()
    #     time.sleep(3)
        
    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()



if __name__=="__main__":
    MyTests.__name__
