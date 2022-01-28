# -*- coding: UTF-8 -*-
# 文件名：driver_init.py
from selenium import webdriver
from PIL import Image, ImageEnhance
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager  # 自动更新下载chromedriver
from selenium.webdriver import Remote # 运行远程服务器webdriver
import platform;
# driver = webdriver.Chrome(ChromeDriverManager().install())# 自动更新下载chromedriver
# driver = webdriver.Chrome("./chromedriver/chromedriver")# 手动指定chromedriver


class DriverConfig:
    # 构造函数
    def __init__(self, webdriver):
        self.driver=webdriver;
    # 初始化webDriver
    def driver_config(self):
        
        # 设置默认下载目录
        download_file_path = './download_file/'
        prefs = {
            "download.prompt_for_download": False,
            "download.default_directory": download_file_path
        }
        options = webdriver.ChromeOptions()
        # 谷歌浏览器驱动路径
        options.binary_location = '/usr/bin/google-chrome-stable'
        # ChromeOptions
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
        # 浏览器驱动
        # 通过global关键字表示我在函数里面的这个变量是使用的全局那个
        self.driver =webdriver.Chrome(ChromeDriverManager().install(
        ), options=options, desired_capabilities=options.to_capabilities())
        # 谷歌浏览器驱动路径
        # 判断当前系统
        if(platform.system()=='Windows'):
            driverpath = './chromedriver/chromedriver.exe'
        else:    
            driverpath = './chromedriver/chromedriver'
        # 浏览器驱动
        self.driver = webdriver.Chrome(driverpath, options=options, desired_capabilities=des)# 运行本地chrome
        # self.driver = webdriver.Remote(command_executor="http://10.224.2.98:4444/wd/hub", desired_capabilities=des,options=options)# 运行远程chrome
        implicitly_wait = 60000
        self.driver.implicitly_wait(implicitly_wait)
        
        return self.driver

        '''
            chrome options
            https://note.youdao.com/s/ER8jfnYo
        '''