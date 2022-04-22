#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from datetime import timedelta

# jwt scret key
JWT_SECRET_KEY = "liyinchi1234567890" # 
# jwt 过期时间
JWT_EXPIRATION_DELTA = timedelta(seconds=3600*48) # 
# jwt 校验的声明
JWT_VERIFY_CLAIMS = ['signature', 'exp', 'iat']
# jwt 必须的声明
JWT_REQUIRED_CLAIMS = ['exp', 'iat']
# jwt
JWT_AUTH_ENDPOINT = 'jwt'
# jwt 加密方式
JWT_ALGORITHM = 'HS256'
# jwt 偏移量时间间隔
JWT_LEEWAY = timedelta(seconds=10)
# jwt 头部前缀
JWT_AUTH_HEADER_PREFIX = 'JWT'
# jwt 不是在之前
JWT_NOT_BEFORE_DELTA = timedelta(seconds=0)

# 数据库配置
DB_USERNAME = 'root'
DB_PASSWORD = 'lyc123456'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME='flask_demo'