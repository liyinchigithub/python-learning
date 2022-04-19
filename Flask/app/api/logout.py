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
logout=Blueprint('logout',__name__)

@logout.route('/', methods=['GET', 'POST'])
def logout_api():
    # 清除服务端 token TODO 下次的访问接口返回需要登录token 校验失败
    return {"msg": "success", "status": 200, "data": "退出成功"}