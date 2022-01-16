
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test07.py
# selenium 
# https://selenium-python-zh.readthedocs.io/en/latest/

import requests
import time
import pytest
# import pytesseract # 验证码识别
# from selenium.webdriver import Remote
# import json
from selenium import webdriver
from PIL import Image, ImageEnhance
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager # 自动更新下载chromedriver
# driver = webdriver.Chrome(ChromeDriverManager().install())# 自动更新下载chromedriver
# driver = webdriver.Chrome("./chromedriver/chromedriver")# 手动指定chromedriver
# 设置默认下载目录
download_file_path = './download_file/'
prefs = {
    "download.prompt_for_download" : False,
    "download.default_directory": download_file_path
}

options = webdriver.ChromeOptions()
# 谷歌浏览器驱动路径
options.binary_location = '/usr/bin/google-chrome-stable'
# 实例化ChromeOptions
options = webdriver.ChromeOptions()
# 关闭浏览器提示信息
options.add_argument('disable-infobars')
# 浏览器全屏
options.add_argument('start-fullscreen')
# 无头模式
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-setuid-sandbox')
options.add_experimental_option('prefs', prefs)
# 获取谷歌浏览器所有控制台信息
des = DesiredCapabilities.CHROME
des['loggingPrefs'] = {'performance': 'ALL'}
# 浏览器驱动 executable_path=chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options, desired_capabilities=options.to_capabilities())

'''
    By 类的一些可用属性
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
'''


def setup_function():
    print("setup_function():每个方法之前执行")


def teardown_function():
    print("teardown_function():每个方法之后执行")

def setup_module():
    print("teardown_function():每个方法之后执行")
    driver.close()
    
    
data=[("http://www.baidu.com","百度搜索"),("http://www.bing.com","必应搜索")]
@pytest.mark.parametrize("url,search_text",data)
def test_baidu_search(url,search_text):
        driver.maximize_window()
        driver.get(url)
        driver.find_element_by_id("kw").send_keys(search_text)
        driver.find_element_by_id('su').click()
        time.sleep(10)
        # 截图-输出控制台
        file=driver.get_screenshot_as_png
        print(file)
        # 截图-保存本地
        save_screenshot()
        print("测试数据为{}".format(url))
        print("测试数据为{}".format(search_text))
        
        

@pytest.mark.skip
def test_bing_search():
        driver.maximize_window()
        url="http://www.bing.com"
        driver.get(url)
        driver.find_element_by_id("sb_form_q").send_keys("python")
        driver.find_element_by_id('search_icon').click()
        time.sleep(2)
                # 截图-输出控制台
        file=driver.get_screenshot_as_png
        print(file)
        # 截图-保存本地
        save_screenshot()
        



    
'''
    截图保存本地
'''
def save_screenshot():
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        if driver.get_screenshot_as_file('./save_images/%s.png' %now_time):
            print('保存成功')
        else:
            print('保存失败')




