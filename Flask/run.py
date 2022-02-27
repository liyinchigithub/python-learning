#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 引入了Flask类
from flask import Flask, url_for, request, render_template, redirect, flash,session, make_response
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask import send_from_directory
# 实例化
app = Flask(__name__, template_folder='./myProject/templates/', static_folder="****")

 # 文件上传
class UploadForm():
    photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg','jpeg','png','gif'])])
    # submit = SubmitField()

import os
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')

import uuid

def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename

@app.route('/uploaded-images')
def show_images():
    return render_template('uploaded.html')

@app.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename =random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload success.')
        session['filenames'] = [filename]
        return redirect(url_for('show_images'))
    return render_template('upload.html', form = form)

#  修饰器定义路由
@app.route('/')
#  每个路由对应一个函数（路由映射函数）
def root():
    return {"msg": "success", "status": 200, "data": "成功"}

@app.route('/home')
#  每个路由对应一个函数（路由映射函数）
def home():
    return render_template('home.html', title="欢迎")


@app.route('/login', methods=['POST', 'GET'])
def login():
    #  获取请求方法
    if request.method == 'POST':
        #  获取请求body form
        if request.form['user'] == 'admin':
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    title = request.args.get('title', 'Default')
    #  返回视图模板给客户端浏览器
    return render_template('login.html', title=title)


# form

# json

# 文件上传


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

class InvalidUsage(Exception):#  继承父类Exception
    status_code = 400

    def __init__(self, message, status_code=400):
        #  调用基类构造函数
        Exception.__init__(self)
        #  接收类实例化入参
        self.message = message
        self.status_code = status_code


@app.errorhandler(InvalidUsage)
def invalid_usage(error):
    #  构造响应  返回错误异常内容给客户端
    response = make_response(error.message)
    #  响应状态码
    response.status_code = error.status_code
    return response

@app.route('/exception')
def exception():
    #  抛出异常
    raise InvalidUsage('No privilege to access the resource', status_code=403)

# 设置调试模式，生产模式的时候要关掉debug
# 主机地址
# 端口号，默认是5000
# 是否自动重启代码
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5001, use_reloader=True)  # 启动程序
