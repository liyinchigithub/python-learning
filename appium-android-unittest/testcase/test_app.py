
#!/usr/bin/python
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
                        'appPackage': 'com.youdao.calculator',  # apk的包名
                        'appActivity': 'com.youdao.calculator.activities.MainActivity',  # activity 名称
                        'reset':"false"
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium server
        self.driver.implicitly_wait(8)

    def test_calculator(self, t=500, n=4):
        """计算器测试"""
        time.sleep(3)# 等待3秒
        window = self.driver.get_window_size() #获取窗口大小
        x0 = window['width'] * 0.8  # 起始x坐标
        x1 = window['width'] * 0.2  # 终止x坐标
        y = window['height'] * 0.5  # y坐标
        for i in range(n):
            self.driver.swipe(x0, y, x1, y, t)# 滑动
            time.sleep(1)
        self.driver.find_element_by_id('com.youdao.calculator:id/guide_button').click()# 点击
        for i in range(6):
            self.driver.find_element_by_accessibility_id('Mathbot Editor').click()# 点击
            time.sleep(1)

        btn_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.View/android.widget.GridView/android.widget.FrameLayout[{0}]/android.widget.FrameLayout'
        self.driver.find_element_by_xpath(btn_xpath.format(7)).click()
        self.driver.find_element_by_xpath(btn_xpath.format(10)).click()
        self.driver.find_element_by_xpath(btn_xpath.format(8)).click()
        time.sleep(3)
        
    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()



# if __name__=="__main__":
#     MyTests.__name__
