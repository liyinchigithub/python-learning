#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 引入了Flask类
from crypt import methods
from encodings import utf_8
import functools
from importlib.resources import path
from flask import Flask, url_for, request, render_template, redirect, flash, session, make_response,Blueprint,jsonify
from flask_wtf.file import FileField, FileRequired, FileAllowed  # 文件上传
from flask import send_from_directory  # 发送静态文件
from flasgger import Swagger # flask swagger
from flasgger.utils import swag_from # flask swagger
from flask_cors import CORS  # 跨域访问
from werkzeug.utils import secure_filename
from werkzeug.routing import BaseConverter # 正则表达式
import os,datetime
import uuid  # 生成随机字符串
import json
import jwt
app = Flask(__name__, template_folder='./myProject/templates/',static_folder="./static/") # 访问静态文件夹下的文件 http://127.0.0.1:5876/static/文件名.jpg

# [jwt配置]
app.config["JWT_SECRET"] = "JWT_SECRET_KEY"
app.config["JWT_EXPIRY_HOURS"] = 3600 * 1 # 1小时
app.config["JWT_REFRESH_DAYS"] = 1

'''
    [生成token]
    :param user_id: 用户id
    :param need_refresh_token: 是否需要刷新token
    :return: token2小时, refresh_token14天
'''
def generate_token(user_id, need_refresh_token=True):
    pass
    '生成时间信息'
    current_time = datetime.datetime.utcnow()
    '指定有效期  业务token -- 2小时,我们这里测试所以设置的秒数'
    expire_time = current_time + \
        datetime.timedelta(seconds=app.config['JWT_EXPIRY_HOURS'])

    '生成业务token  refresh 标识是否是刷新token'
    token = generate_jwt(
        {'user_id': user_id, 'refresh': False}, expiry=expire_time)

    '给刷新token设置一个默认值None'
    refresh_token = None
    '根据传入的参数判断是否需要生成刷新token'
    '不需要生成的传入need_refresh_token=False,需要的传入True或不传使用默认值'
    if need_refresh_token:
        '指定有效期  刷新token -- 14天,我们这里测试所以设置的秒数'
        refresh_expires = current_time + \
            datetime.timedelta(seconds=app.config['JWT_REFRESH_DAYS'])
        '生成刷新token'
        refresh_token = generate_jwt(
            {'user_id': user_id, 'refresh': True}, expiry=refresh_expires)
    '返回这两个token'
    return token, refresh_token

def login_required(f):
    '让装饰器装饰的函数属性不会变 -- name属性'
    '第1种方法,使用functools模块的wraps装饰内部函数'

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if not g.user_id:
            return {'message': 'User must be authorized.'}, 401
        elif g.refresh:
            return {'message': 'Do not use refresh token.'}, 403
        else:
            return f(*args, **kwargs)

    '第2种方法,在返回内部函数之前,先修改wrapper的name属性'
    # wrapper.__name__ = f.__name__
    return wrapper

"""
    [生成jwt]
    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :param secret: 密钥
    :return: jwt
"""
def generate_jwt(payload, expiry, secret=None):

    _payload = {'exp': expiry}
    _payload.update(payload)

    if not secret:
        secret = app.config['JWT_SECRET']

    token = jwt.encode(_payload, secret, algorithm='HS256')
    return token

"""
    [检验jwt]
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
"""
def verify_jwt(token, secret=None):

    if not secret:
        secret = app.config['JWT_SECRET']
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.PyJWTError as e:
        print("jwt.PyJWTError：",e)
        payload = None
    return payload