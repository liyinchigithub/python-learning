
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test07.py
# selenium 
# https://selenium-python-zh.readthedocs.io/en/latest/

import requests
import time
# import pytesseract # 验证码识别
# from selenium.webdriver import Remote
# import json
from selenium import webdriver
from PIL import Image, ImageEnhance
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager # 自动更新下载chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())# 自动更新下载chromedriver
# driver = webdriver.Chrome("./chromedriver/chromedriver")# 手动指定chromedriver


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
def baiduSearch():
   
    driver.maximize_window()
    url="http://www.baidu.com"
    driver.get(url)
    file=driver.get_screenshot_as_png
    print(file)
    time.sleep(1)
    driver.find_element_by_id("kw").send_keys("python")
    driver.find_element_by_id('su').click()
    time.sleep(10)
    driver.close()
    
    
# baiduSearch()


