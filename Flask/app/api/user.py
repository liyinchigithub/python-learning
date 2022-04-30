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
import os,sys
import uuid  # 生成随机字符串
import json
from flask import current_app as app # 让蓝图可以使用app对象

sys.path.append('../')
from app.db import db_user # 导入用户模型


# 创建蓝图对象
user=Blueprint('user',__name__)


'''
    [注册接口]
    [request body json]
    获取参数方式：
    request.json['key']
    request.json.get('key')
    request.get_data()
    request.get_json()
    request.form.get('username')
'''
@user.route('/add', methods=['POST'])
def user_add_api():
    try:
        request_data = request.json
        print("request.json",request.json)
        # 查询数据库是否存在该用户，且密码是否正确
        print(type(db_user.select_user_first_one(request_data["username"])))
        # 如果用户名已存在，则返回一个数据类型为字典的json数据，如果不存在，则返回None
        if db_user.select_user_first_one(request_data["username"])==None:
            # 数据库插入数据
            result=db_user.insert_user(request_data["username"],request_data["password"],request_data["type"])
            #  判断是否插入成功
            if result==True:
                return {"msg": "success", "code": 200, "data":  "注册成功"}
            else:
                return {"msg": "error", "code": 500, "data": f"注册失败，失败原因:s{result}"}
        else:    
            return {"msg": "fail", "code": 201, "data": "用户名已存在"}
    except Exception as e:
        print(e)
        return {"msg": "fali", "code": 401, "data": e}


@user.route('/list', methods=['POST'])
def user_list_api():
    try:
        request_data = request.json
        print("request.json",request.json)
        # 查询数据库是否存在该用户，且密码是否正确
        print(type(db_user.select_user_page(request_data["page_num"],request_data["page_size"])))
        # 如果用户名已存在，则返回一个数据类型为字典的json数据，如果不存在，则返回None
        result=db_user.select_user_page(request_data["page_num"],request_data["page_size"])
        print("user list ：",result)
        return dict(code=200, msg="success", data=result)
    except Exception as e:
        print(e)
        return {"msg": "fali", "code": 401, "data": e}

@user.route('/update', methods=['PUT'])
def user_update_api():
    try:
        request_data = request.json
        print("request.json",request.json)
        # 查询数据库是否存在该用户，且密码是否正确
        # 如果用户名已存在，则返回一个数据类型为字典的json数据，如果不存在，则返回None
        result=db_user.update_user(request_data["id"],request_data["data"])
        print("user_monitor list ：",result)
        return dict(code=200, msg="success", data=result)
    except Exception as e:
        print(e)
        return {"msg": "fali", "code": 401, "data": e}

@user.route('/delete', methods=['DELETE'])
def user_delete_api():
    try:
        request_data = request.json
        print("request.json",request.json)
        result=db_user.delete_user(request_data["id"])
        print("delete_user ：",result)
        if result==1:
            return dict(code=200, msg="success", data="删除成功")
        else:
            return dict(code=201, msg="error", data="删除失败")
    except Exception as e:
        print(e)
        return {"msg": "fali", "code": 401, "data": e}