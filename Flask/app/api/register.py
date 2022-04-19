#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 登录接口
from crypt import methods
from importlib.resources import path
from lib2to3.pgen2.token import RPAR
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
register=Blueprint('register',__name__)

# [request body json]  多方式：request.json.get('key')、request.get_data()、
@register.route('/', methods=['GET', 'POST'])
def register_api():
    try:
        request_data = request.json
        print("request.json",request.json)
        return {"msg": "success", "status": 200, "data": request_data}
    except Exception as e:
        print(e)
        return {"msg": "fali", "status": 401, "data": e}
