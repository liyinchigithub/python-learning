#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 引入了Flask类
from flask import Flask, url_for, request, render_template, redirect, flash, session, make_response
from flask_wtf.file import FileField, FileRequired, FileAllowed  # 文件上传
from flask import send_from_directory  # 发送静态文件
from flask_cors import CORS  # 跨域访问
import os
import uuid  # 生成随机字符串
import json
# 实例化Flask
app = Flask(__name__, template_folder='./myProject/templates/',
            static_folder="****")
# 允许跨域
CORS(app, supports_credentials=True)

# 文件上传
class UploadForm():
    #
    photo = FileField('Upload Image', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    # submit = SubmitField()

# 配置上传文件存放路径
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
# 配置上传文件的最大大小 todo
# 配置上传文件名称
def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename

# 定义上传文件的路径
@app.route('/uploaded-images')
def show_images():
    return render_template('uploaded.html')

# 定义上传文件的路径
@app.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

# 定义上传文件的路径
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # 判断是否是POST请求
    form = UploadForm()
    # 判断请求方式
    if form.validate_on_submit():
        # 获取文件名
        f = form.photo.data
        # 获取文件名
        filename = random_filename(f.filename)
        # 保存文件
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload success.')  # 显示提示信息
        #
        session['filenames'] = [filename]
        #
        return redirect(url_for('show_images'))  # 重定向到上传成功的页面
    return render_template('upload.html', form=form)  # 渲染模板

#  修饰器定义路由
@app.route('/')
#  每个路由对应一个函数（路由映射函数）
def root():
    return redirect(url_for('home'))# 重定向到home路由

@app.route('/home')
def home():
    return render_template('home.html', title="欢迎")

# request body json
@app.route('/login', methods=['post'])
def login():
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


# request body form-data
@app.route('/login2', methods=['GET'])
def login2():
    try:
        # 判断请求方式
        if request.method == 'GET':
            # 获取请求参数
            if request.form['username'] == 'liyinchi': # request body form-data
                # 重定向到首页
                return 'welcome liyinchi!'
            else:
                return 'No such user!'  # 显示提示信息
        #
        title = request.args.get('title', 'Default')  # 获取请求参数
        #  返回视图模板给客户端浏览器
        return render_template('login.html', title=title)  # 渲染模板
    except Exception as e:
        print(e)
        return  {"msg": "error", "status": 500, "data": str(e)}  # 重定向到指定路由
        # return redirect(url_for('home'))  # 重定向到指定路由

@app.route('/register', methods=['GET', 'POST'])
def register():
    # 数据库插入数据 TODO
    
    return {"msg": "success", "status": 200, "data": "注册成功"}

@app.route('/logout')
def logout():
    # 清除token
    return {"msg": "success", "status": 200, "data": "退出成功"}

@app.route('/find', methods=['GET', 'POST'])
def find():
    get_data = request.args.to_dict()# 获取传入的params参数
    username = get_data.get('username')
    password = get_data.get('password')
    return {"msg": "success", "status": 200, "data": {"username":username,"password":password}}


# 对请求的Response header中加入header
@app.after_request
def af_request(resp):
    """
     #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp





# 错误处理
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 启动服务器
class InvalidUsage(Exception):  # 继承父类Exception
    # 定义异常类
    status_code = 400
    # 定义异常状态码
    def __init__(self, message, status_code=400):
        #  调用基类构造函数
        Exception.__init__(self)
        #  接收类实例化入参
        self.message = message
        self.status_code = status_code

# 定义路由
@app.errorhandler(InvalidUsage)# 定义错误处理
def invalid_usage(error):
    #  构造响应  返回错误异常内容给客户端
    response = make_response(error.message)
    #  响应状态码
    response.status_code = error.status_code
    return response

# 定义路由
@app.route('/exception')
def exception():
    #  抛出异常
    raise InvalidUsage('No privilege to access the resource', status_code=403)


# 设置调试模式，生产模式的时候要关掉debug
# 主机地址
# 端口号，默认是5000
# 是否自动重启代码
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5876, use_reloader=True)  # 启动程序
