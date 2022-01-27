
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test_selenium.py
# selenium
# https://selenium-python-zh.readthedocs.io/en/latest/
# https://selenium-python-zh.readthedocs.io/en/latest/locating-elements.html

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
from webdriver_manager.chrome import ChromeDriverManager  # 自动更新下载chromedriver
# driver = webdriver.Chrome(ChromeDriverManager().install())# 自动更新下载chromedriver
# driver = webdriver.Chrome("./chromedriver/chromedriver")# 手动指定chromedriver
driver=any

'''
    [By类]的一些可用属性
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
    
    find_element_by_id
    find_element_by_name
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector

    [一次查找多个元素 (这些方法会返回一个list列表)]:

    find_elements_by_name
    find_elements_by_xpath
    find_elements_by_link_text
    find_elements_by_partial_link_text
    find_elements_by_tag_name
    find_elements_by_class_name
    find_elements_by_css_selector
'''
def driverInit():
    # chrome options https://note.youdao.com/s/ER8jfnYo
    # 设置默认下载目录
    download_file_path = './download_file/'
    prefs = {
        "download.prompt_for_download": False,
        "download.default_directory": download_file_path
    }

    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/google-chrome-stable' # 谷歌浏览器驱动路径
    options = webdriver.ChromeOptions() # 实例化ChromeOptions
    options.add_argument('disable-infobars')# 关闭浏览器提示信息
    options.add_argument('start-fullscreen')# 浏览器全屏
    # options.add_argument('--headless')# 无头模式
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-setuid-sandbox')
    options.add_experimental_option('prefs', prefs)
    # 获取谷歌浏览器所有控制台信息
    des = DesiredCapabilities.CHROME
    des['loggingPrefs'] = {'performance': 'ALL'}
    # 浏览器驱动 executable_path=chromedriver
    global driver # 对全局变量给了重新的指向
    # 通过global关键字表示我在函数里面的这个变量是使用的全局那个
    driver = webdriver.Chrome(ChromeDriverManager().install(
    ), options=options, desired_capabilities=options.to_capabilities())
    

def setup_module():
    print("teardown_module():每个模块（文件）之前执行")


def setup_class():
    print("setup_class():每个类之前执行")


def teardown_class():
    print("teardown_class():每个类之后执行")


def setup_function():
    print("setup_function():非类中的方法，每个方法之前执行")
    driverInit()


def teardown_function():
    print("teardown_function():非类中的方法，每个方法之后执行")

def setup_method():
    print("setup_method():类中的方法，每个方法之前执行")

def teardown_method():
    print("teardown_method():类中的方法，每个方法之后执行")


def setup_module():
    print("teardown_module():每个模块（文件）之后执行")


data = [("http://www.baidu.com", "百度搜索"), ("http://www.bing.com", "必应搜索")]
'''
    DDT 数据驱动（参数化）
'''


@pytest.mark.parametrize("url,search_text", data)
def test_baidu_search(url, search_text):
    driver.maximize_window()
    driver.get(url)
    try:
        if("baidu" in url):
            driver.find_element_by_id("kw").send_keys(search_text)
            driver.find_element_by_id('su').click()
        elif("bing" in url):
            driver.find_element_by_id("sb_form_q").send_keys("python")
            driver.find_element_by_id('search_icon').click()
    except(ValueError):
        print(ValueError)
    time.sleep(10)
    # 截图-输出控制台
    file = driver.get_screenshot_as_png
    print(file)
    # 截图-保存本地
    save_screenshot()
    print("测试数据为{}".format(url))
    print("测试数据为{}".format(search_text))


'''
    跳过
'''


@pytest.mark.skip
@pytest.mark.smoke
def test_bing_search():
    driver.maximize_window()
    url = "http://www.bing.com"
    driver.get(url)
    driver.find_element_by_id("sb_form_q").send_keys("python")
    driver.find_element_by_id('search_icon').click()
    time.sleep(2)
    # 截图-输出控制台
    file = driver.get_screenshot_as_png
    print(file)
    # 截图-保存本地
    save_screenshot()


'''
    截图保存本地
'''


def save_screenshot():
    now_time = time.strftime('%Y-%m-%d %H:%M:%S')
    if driver.get_screenshot_as_file('./save_images/%s.png' % now_time):
        print('保存成功')
    else:
        print('保存失败')
