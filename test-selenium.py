
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test07.py
# selenium 
# https://selenium-python-zh.readthedocs.io/en/latest/

import requests
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # 自动更新下载chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())# 自动更新下载chromedriver
import pytesseract # 验证码识别
# driver = webdriver.Chrome("./chromedriver/chromedriver")

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