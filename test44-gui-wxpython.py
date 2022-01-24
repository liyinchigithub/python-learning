#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# test44-gui-wxpython.py
# Python GUI
# https://blog.csdn.net/qq_15158911/article/details/87600828
# https://xufive.blog.csdn.net/article/details/82665460
import pytest
import wx


'''
    python gui（图形化）常用模块介绍
    [Tkinter]
    python最简单的图形化模块，总共只有14种组建，（也叫Tk接口）是Tk图形用户界面工具包标准的Python接口。
    Tk是一个轻量级的跨平台图形用户界面（GUI）开发工具。
    Tk和Tkinter可以运行在大多数的Unix平台、Windows、和Macintosh系统。
    
    [Pyqt]
    python最复杂也是使用最广泛的图形化，PyQt是Qt库的Python版本。PyQt是用SIP写的。PyQt 提供 GPL版和商业版。
    
    [Pywin]
    python windows 下的模块，摄像头控制(opencv)，常用于外挂制作，Windows Pywin32允许你像VC一样的形式来使用PYTHON开发win32应用。
    代码风格可以类似win32 sdk，也可以类似MFC，由你选择。如果你仍不放弃vc一样的代码过程在python下，那么这就是一个不错的选择。
    
    [wxPython]
    最流行的Python GUI开发框架之一，基于[wxWidgets]，是一个C++编写的跨平台GUI库，除了标准的对话框，还提供一个2D路径绘制API，支持多种文件格式以及文本编辑和字处理widgets。
    wxPython是Python 语言的一套优秀的 GUI 图形库，允许 Python 程序员很方便的创建完整的、功能键全的 GUI 用户界面。
    作为优秀的[跨平台]GUI库wxWidgets的Python封装和Python模块的方式提供给用户的。
    就如同Python和wxWidgets一样，wxPython也是一款开源软件，并且具有非常优秀的跨平台能力，能够运行在32位windows、绝大多数的Unix或类Unix系统、Macintosh OS X上。

'''

'''
    [安装依赖]
     sudo  pip3 install wxpython
'''


'''
    [参数介绍]
    parent = None   #父元素，假如为None，代表顶级窗口。
    id = None       #组件的标识，唯一，假如id为-1代表系统分配id。
    title=None      #frame窗口的标题栏。
    value = None    #文本框当中的内容。
    GetValue        #获取文本框的值。
    SetValue        #设置文本框的值。
    pos = None      #组件的位置，就是组件左上角点距离父组件或者桌面左和上的距离。
    size = None     #组件的尺寸，宽高。
    style = None    #组件的样式。
    name = None     #组件的名称，也是用来标识组件的，但是用于传值。
'''

'''
    [组件介绍]    
'''

# 1.frame(窗口)


# 2.TextCtrl（文本框）


# 3.Button（按钮）


# 4.创建窗口基础代码
'''

app = wx.App() #实例化一个主循环
frame = wx.Frame(None,title='test',size=(300,300)) #实例化一个窗口
frame.Show()#调用窗口展示功能
app.MainLoop()#启动主循环
'''

# 登录

import wx
 
class LoginFrame(wx.Frame):
    """
    登录窗口
    """
    def __init__(self, parent, id, title, size):
        # 初始化，添加控件并绑定事件
        wx.Frame.__init__(self, parent, id, title)
        self.SetSize(size)#自动调节窗口大小
        self.Center()#设置登录弹窗在桌面中心
        self.serverAddressLabel = wx.StaticText(self, label="Server Address", pos=(10, 50), size=(120, 25))
        self.userNameLabel = wx.StaticText(self, label="UserName", pos=(40, 100), size=(120, 25))
        self.serverAddress = wx.TextCtrl(self, pos=(120, 47), size=(150, 25),style=wx.TE_PROCESS_TAB)
        self.userName = wx.TextCtrl(self, pos=(120, 97), size=(150, 25),style=wx.TE_PROCESS_TAB)
        self.loginButton = wx.Button(self, label='Login', pos=(80, 145), size=(130, 30))
        # 绑定登录方法
        self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        self.Show()#显示以上控件
    
    def login(self, event): 
        pass
      
if __name__ == '__main__':
    app = wx.App()#实例化一个主循环
    LoginFrame(None, -1, title="Login", size=(320, 250))
    app.MainLoop()#启动主循环


# 命令行执行：python test44-gui-wxpython.py