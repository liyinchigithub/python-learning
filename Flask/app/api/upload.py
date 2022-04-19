#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件上传接口
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
upload=Blueprint('upload',__name__)

# [文件重命名]
def random_filename(f):
   try:
        # 获取文件扩展名
        ext = secure_filename(f.filename).split('.')[-1]
        print("secure_filename(filename)为：",secure_filename(f.filename))# secure_filename(filename)为：upload.jpg
        print(ext)# jpg
        # 重新生成文件名
        new_filename = uuid.uuid4().hex +"." +ext
        # 返回文件名
        return new_filename
   except Exception as e:
       print(e)

# [文件上传接口]
@upload.route('/', methods=['GET', 'POST'])
def upload_api():
    try:
        # 判断是否是POST请求
        if request.method == 'POST':
            # 获取上传的文件
            f = request.files['file']
            print(request.files['file'])# <FileStorage: 'upload.jpg' ('image/jpeg')>
            # 重命名文件
            filename = random_filename(f)
            # 保存文件
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            # 显示提示信息
            # flash('Upload success.')  
            # 会话设置
            # session['filenames'] = [filename]
            # 返回上传成功的文件名
            return {"msg": "success", "status": 200, "data": filename}
            # return redirect(url_for('show_images'))  # 重定向到上传成功的页面
    except Exception as e:
        print(e)
        return {'code': 413, 'msg': 'fail',"data":e}

# [文件上传]渲染页面
@upload.route('/render_template', methods=['GET', 'POST'])
def show_images():
    return render_template('uploaded.html')

# [上传文件]文件名通过url参数传递 /a/b/1.txt
@upload.route('/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)