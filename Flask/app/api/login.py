#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 登录接口
from crypt import methods
from importlib.resources import path
from flask import Flask, url_for, request, render_template, redirect, flash, session, make_response,Blueprint
from flask_wtf.file import FileField, FileRequired, FileAllowed  # 文件上传
from flask import send_from_directory  # 发送静态文件
from flask_cors import CORS  # 跨域访问
from werkzeug.utils import secure_filename
from werkzeug.routing import BaseConverter # 正则表达式
import os
import uuid  # 生成随机字符串
import json
from flask import current_app as app # 让蓝图可以使用app对象

# 创建蓝图对象
login=Blueprint('login',__name__)

# [request body json]  多方式：request.json.get('key')、request.get_data()、
@login.route('/', methods=['post'])
def login_api():
    try:
        # 获取请求参数
        request_data = request.get_data() # 对于前端POST请求发送过来的json数据，Flask后台可使用 request.get_data() 来接收数据，数据的格式为 bytes；再使用 json.loads() 方法就可以转换字典。
        # 将bytes类型转换为json数据
        request_json_data = json.loads(request_data)# 将json字符串数据转换为字典
        username = request_json_data.get('username')# 获取num1
        password = request_json_data.get('password')# 
        # return json.dumps({"username":username,"password":password})# 将字典转换为json字符串
        return {"username":username,"password":password }# 返回json数据
    except Exception as e:
        return {"msg": "error", "status": 500, "data":  str(e)}


# [request body form-data]  request.form['key']
@login.route('/2', methods=['post'])
def login_api2():
    try:
        # 判断请求方式
        if request.method == 'POST':
            # 获取form-data 请求参数
            if request.form['username'] == 'liyinchi': # request body form-data
                # 重定向到首页
                return 'welcome liyinchi!'
            else:
                return 'No such user!'  # 显示提示信息
        else:
            title = request.args.get('title', 'Default')  # request url query string
            #  返回视图模板给客户端浏览器
            return render_template('login.html', title=title)  # 渲染模板
        
    except Exception as e:
        print(e)
        return  {"msg": "error", "status": 500, "data": str(e)}  # 重定向到指定路由
        # return redirect(url_for('home'))  # 重定向到指定路由