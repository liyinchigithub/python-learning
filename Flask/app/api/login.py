#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 登录接口
from crypt import methods
from importlib.resources import path
from typing import Type
from flask import Flask, url_for, request, render_template, redirect, flash, session, make_response, Blueprint, g
from flask_wtf.file import FileField, FileRequired, FileAllowed  # 文件上传
from flask import send_from_directory  # 发送静态文件
from flask_cors import CORS  # 跨域访问
from werkzeug.utils import secure_filename
from werkzeug.routing import BaseConverter  # 正则表达式
import functools
from datetime import datetime, timedelta
import os
import uuid  # 生成随机字符串
import json
import jwt
from flask import current_app as app  # 让蓝图可以使用app对象
from config import *  # JWT参数配置文件
# 创建蓝图对象
login = Blueprint('login', __name__)

# [request body json]  多方式：request.json.get('key')、request.get_data()、


@login.route('/', methods=['POST'])
def login_api():
    try:
        # 获取请求参数
        # 对于前端POST请求发送过来的json数据，Flask后台可使用 request.get_data() 来接收数据，数据的格式为 bytes；再使用 json.loads() 方法就可以转换字典。
        request_data = request.get_data()
        # 将bytes类型转换为json数据
        request_json_data = json.loads(request_data)  # 将json字符串数据转换为字典
        username = request_json_data.get('username')  # 获取num1
        password = request_json_data.get('password')
        # return json.dumps({"username":username,"password":password})# 将字典转换为json字符串
        return {"username": username, "password": password}  # 返回json数据
    except Exception as e:
        return {"msg": "error", "status": 500, "data":  str(e)}


# @login.route('/getToken', methods=['GET', 'POST'])
# def get_token():
#     try:
#         token = jwt.encode({'some': {"jwt": "jwt"}, 'exp': datetime.utcnow(
#         )}, JWT_SECRET_KEY, algorithm='HS256')
#         print("token", Type(token))
#         return json.dumps({"username": "username", "password": "password"})
#     except Exception as e:
#         print(e)
#         return {"msg": "error", "status": 500, "data": e}  # 重定向到指定路由

