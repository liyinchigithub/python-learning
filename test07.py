
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test07.py
# selenium

# import requests
import time
from selenium import webdriver
# import pytesseract

driver = webdriver.Chrome("./chromedriver/chromedriver")
driver.maximize_window()
url="http://www.baidu.com"
driver.get(url)
file=driver.get_screenshot_as_png
print(file)
time.sleep(1)
driver.find_element_by_id("kw").send_keys("python")

    
