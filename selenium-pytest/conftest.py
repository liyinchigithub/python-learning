# import pytest;
# from selenium import webdriver
# from PIL import Image, ImageEnhance
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from webdriver_manager.chrome import ChromeDriverManager # 自动更新下载chromedriver
# driver = webdriver.Chrome(ChromeDriverManager().install())# 自动更新下载chromedriver

# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from apitest.uitest.UIMethod import getyamlconf


# class DriverConfig:
#     def driver_config(self):
#         """
#         浏览器驱动
#         :return:
#         """
#         # 实例化ChromeOptions
#         options = webdriver.ChromeOptions()
#         # 关闭浏览器提示信息
#         options.add_argument('disable-infobars')
#         # 浏览器全屏
#         options.add_argument('start-fullscreen')
#         # 设置默认下载目录
#         download_path = getyamlconf.GetConf().get_joinpath() + r"\Requests\apitest\uitest\DownloadFile"
#         prefs = {'download.default_directory': download_path}
#         options.add_experimental_option('prefs', prefs)
#         # 获取谷歌浏览器所有控制台信息
#         des = DesiredCapabilities.CHROME
#         des['loggingPrefs'] = {'performance': 'ALL'}
#         # 谷歌浏览器驱动路径
#         joinpath = getyamlconf.GetConf().get_joinpath()
#         driverpath = joinpath + r'\Requests\apitest\uitest\WebDriver\chromedriver.exe'
#         # 浏览器驱动
#         driver = webdriver.Chrome(driverpath, options=options, desired_capabilities=des)
#         # driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=des,
#         #                           options=options)
#         implicitly_wait = getyamlconf.GetConf().get_implicitly_wait()
#         driver.implicitly_wait(implicitly_wait)
#         return driver