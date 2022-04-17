# #!/usr/bin/python3
# # -*- coding: UTF-8 -*-
# # 存放所有视图函数，如果多，将其变为一个包

# from werkzeug.security import check_password_hash
# from decorator import  jwt_required, jwt_encode, current_identity
# from flask import Flask, url_for, request, render_template, redirect, flash, session, make_response,jsonify
# from flask_wtf.file import FileField, FileRequired, FileAllowed  # 文件上传
# from flask import send_from_directory  # 发送静态文件
# from flask_cors import CORS  # 跨域访问

# mod =Flask(__name__, template_folder='./myProject/templates/',
#            static_folder="****")
# # 允许跨域
# CORS(mod, supports_credentials=True)

# @mod.route('/login', methods=['POST'])
# def login():
#     name = request.json.get('name', '')
#     password = request.json.get('password', '')
#     if len(name) == 0 or len(password) == 0:
#         return jsonify(code=RETCODE.LOGINERR, msg='请输入正确的用户名或密码')

#     manager = Manager.query.filter(Manager.name==name).first() # Manager仅作为示例
#     if not manager:
#         return jsonify(code='2100', msg='未找到用户')

#     if not check_password_hash(manager.password, password):
#         return jsonify(code=RETCODE.PWDERR, msg='密码错误')

#     token = jwt_encode({ 'mid': manager.id, 'name': manager.name})
#     return jsonify(code=RETCODE.OK, data={'token': token.decode('utf8')})

# @mod.route('/token/update', methods=['POST'])
# @jwt_required
# def update_token():
# 	token = jwt_encode({ 'mid': current_identity.get('mid'), 'name': current_identity.get('name')})
# 	return jsonify(code=RETCODE.OK, data={'token': token.decode('utf8')})
