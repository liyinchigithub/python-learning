#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 引入了Flask类
from crypt import methods
from encodings import utf_8
from importlib.resources import path
from flask import Flask, url_for, request, render_template, redirect, flash, session, make_response,Blueprint,jsonify
from flask_wtf.file import FileField, FileRequired, FileAllowed  # 文件上传
from flask import send_from_directory  # 发送静态文件
from flask_cors import CORS  # 跨域访问
from werkzeug.utils import secure_filename
from werkzeug.routing import BaseConverter # 正则表达式
import os
import uuid  # 生成随机字符串
import json
from api.login import * # [蓝图]模块化
from api.upload import * # [蓝图]模块化
from api.logout import * # [蓝图]模块化
from api.register import * # [蓝图]模块化

# 实例化Flask对象 app
app = Flask(__name__, template_folder='./myProject/templates/',static_folder="./static/") # 访问静态文件夹下的文件 http://127.0.0.1:5876/static/文件名.jpg

# [允许跨域]
CORS(app, supports_credentials=True)

# 注册路由（蓝图）
app.register_blueprint(login,url_prefix='/login')
app.register_blueprint(upload,url_prefix='/upload')
app.register_blueprint(logout,url_prefix='/logout')
app.register_blueprint(register,url_prefix='/register')


# [文件上传]存放位置
print("上传文件存放路径为",os.path.dirname(os.path.abspath(__file__)))
app.config['UPLOAD_FOLDER'] = 'upload/' # 注意 ：upload 前面不能加“/”
# [文件上传文件大小限制
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 # 10M
# [jwt配置]
app.config["JWT_SECRET"] = "JWT_SECRET_KEY"
app.config["JWT_EXPIRY_HOURS"] = 60
app.config["JWT_REFRESH_DAYS"] = 1

# [动态路由参数]正则表达式
class RegexConver(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConver,self).__init__(url_map)
        self.regex = items[0]
        
app.url_map.converters['regex'] = RegexConver


# [静态路由]
@app.route('/')
#  每个路由对应一个函数（路由映射函数）
def root():
    return redirect(url_for('home'))# 重定向到home路由

# 后端渲染模板（前端页面）
@app.route('/home')
def home():
    return render_template('home.html', title="欢迎") # 模板内容进行渲染返回

# [动态路由]参数name在url中，数据类型默认为字符串
@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    return  {"msg": "success", "status": 200, "data": name} 

# [动态路由]限制参数类型为整型
@app.route('/user_int/<int:id>', methods=['GET', 'POST'])
def user_int(id):
    print(id)
    return  {"msg": "success", "status": 200, "data": id}  #

# [动态路由]限制参数类型为浮点型
@app.route('/user_float/<float:score>', methods=['GET', 'POST'])
def user_float(score):
    return  {"msg": "success", "status": 200, "data": score} 

# [动态路由]限制参数类型为字符串
@app.route('/user_string/<string:name>', methods=['GET', 'POST'])
def user_string(name):
    return {"msg": "success", "status": 200, "data": name}

# [动态路由]限制参数类型为
@app.route('/user_any/<any(a,b,c):name>', methods=['GET', 'POST'])
def user_any(name):
    return {"msg": "success", "status": 200, "data": name}

# [动态路由]参数为接受用作目录分隔符的斜杠
@app.route('/myProject/templates/<path:filename>', methods=['GET', 'POST'])
def user_path(filename):
    return {"msg": "success", "status": 200, "data": filename}

# [动态理由]正则表达式
@app.route('/user_regex/<regex("[a-z]{3}"):name>',methods=['GET']) # 参数长度必须为3个字符，小写字母组成
def user_regex(name):
    request.cookies.get('username')
    return {"msg": "success", "status": 200, "data": name}

# [获取url ? 后面的参数]    request.args.to_dict()
@app.route('/find', methods=['GET', 'POST'])
def find():
    get_data = request.args.to_dict()# 获取传入的params参数
    username = get_data.get('username')
    password = get_data.get('password')
    return {"msg": "success", "status": 200, "data": {"username":username,"password":password}}

# 每个请求前执行
@app.before_request
def jwt_authentication():
    # 判断是否为登录请求
    print(request.url)
    if ('login' in request.url):
        print("登录接口不进行token验证，只进行token生成")
        return
    else:
        """
        1.获取请求头Authorization中的token
        2.判断是否以 Bearer开头
        3.使用jwt模块进行校验
        4.判断校验结果,成功就提取token中的载荷信息,赋值给g对象保存
        """
        # 获取请求头Authorization中的token
        auth = request.headers.get('Authorization')
        # 判断是否以 Bearer开头
        if auth and auth.startswith('Bearer '):
            "提取token 0-6 被Bearer和空格占用 取下标7以后的所有字符"
            token = auth[7:]
            print("token:",token)
            "校验token"
            payload = verify_jwt(token)
            print("payload:",payload)
            if payload!=None:
                "判断token的校验结果"
                g.user_id = None
                g.refresh = None
                if payload:
                    "获取载荷中的信息赋值给g对象"
                    g.user_id = payload.get('user_id')
                    g.refresh = payload.get('refresh')
            else:
                # 校验失败  例如：Signature has expired 签名过期
                return jsonify({"msg": "登录超时，请重新登录", "status": 401}) 
        else:
            return jsonify({"msg": "登录超时，请重新登录", "status": 401}) 



# [后置处理]针对所有请求，对请求的Response header中加入header
@app.after_request
def after_request(resp):
    """
    请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    # 
    resp = make_response(resp)
    # 允许跨域访问
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    # 生成token
    token,refresh_token=generate_token("1000")# TODO 获取请求头userid
    resp.headers['token'] = token
    resp.headers['refresh_token'] = refresh_token
    # 设置cookie，也可以把token放入cookie中
    # resp.set_cookie("token", token, max_age=3600)
    # resp.set_cookie("refresh_token", refresh_token, max_age=3600)
    return resp



# [错误处理]
@app.errorhandler(404)
def page_not_found(error):
    # return render_template('404.html'), 404
    return {"msg": "fial", "status": 201, "data": error}

# [启动服务器]
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

# [错误处理]
@app.errorhandler(InvalidUsage)
def invalid_usage(error):
    #  构造响应  返回错误异常内容给客户端
    response = make_response(error.message)
    #  响应状态码
    response.status_code = error.status_code
    return response

# [异常处理]
@app.route('/exception')
def exception():
    #  抛出异常
    raise InvalidUsage('No privilege to access the resource', status_code=403)


# 生成token
def generate_token(user_id, need_refresh_token=True):
    """
    生成token 和refresh_token
    :param user_id: 用户id
    :return: token2小时, refresh_token14天
    """
    pass
    '生成时间信息'
    current_time = datetime.utcnow()
    '指定有效期  业务token -- 2小时,我们这里测试所以设置的秒数'
    expire_time = current_time + \
        timedelta(seconds=app.config['JWT_EXPIRY_HOURS'])

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
            timedelta(seconds=app.config['JWT_REFRESH_DAYS'])
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

def generate_jwt(payload, expiry, secret=None):
    """
    生成jwt
    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :param secret: 密钥
    :return: jwt
    """
    _payload = {'exp': expiry}
    _payload.update(payload)

    if not secret:
        secret = app.config['JWT_SECRET']

    token = jwt.encode(_payload, secret, algorithm='HS256')
    return token


def verify_jwt(token, secret=None):
    """
    检验jwt
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
    """
    if not secret:
        secret = app.config['JWT_SECRET']
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.PyJWTError as e:
        print("jwt.PyJWTError：",e)
        payload = None
    return payload


# [启动服务器]
if __name__ == "__main__":
    # 打印路由
    print(app.url_map)
    
    # debug=True        设置调试模式，生产模式的时候要关掉debug
    # host              主机地址
    # port              端口号，默认是5000
    # use_reloader=True 是否自动重启代码
    app.run(debug=True, host="127.0.0.1", port=5876, use_reloader=True)