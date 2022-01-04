
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test07.py
# selenium

import requests
import time
from selenium import webdriver
import pytesseract

driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()
url="http://www.baidu.com"
driver.get(url)