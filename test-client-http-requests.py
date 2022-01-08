#!/usr/bin/python
# -*- coding: UTF-8 -*-
# test-server-http.py
# requests库
# http://www.zzvips.com/article/150840.html
# https://blog.csdn.net/qq_36814756/article/details/97113251

import requests

'''
    GET
'''

def getDemo01():
    response = requests.get('http://httpbin.org/get')
    print(response.text)
    print(type(response.text))
    # 字符串转字典

# getDemo01()

'''
    GET
'''
def getDemo02():
    response =requests.get("https://www.csdn.net");
    # 输出response的类型、状态码、响应体的类型、内容以及 Cookies
    print(type(response))
    print(response.status_code) # 响应状态码
    print(response.headers) # 响应头
    print(type(response. text)) # 响应body类型
    print(response.text)# 响应body
    print(response.cookies)# 响应cookie

# getDemo02()


'''
    GET
    请求参数
'''
def getDemo03():
    #附加额外的信息，比如:URL想添加两个参数， 其中 name 是 germey, age 是 22
    data={
        'name':'germey',
        'age':'22'
    }
    response = requests.get('http://httpbin.org/get',params=data) # 相当于response = requests.get(‘http://httpbin.org/get?name=germey&age=22’)
    print(response.text)

# getDemo03()

'''
    GET
    请求头信息
'''
def getDemo04():
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    response=requests.get("https://www.zhihu.com/", headers=headers)
    print(response.text)

# getDemo04()

'''
    GET
    提取到的图片保存下来
'''
def getDemo05():
    response=requests.get("https://github.com/favicon.ico")
    with open('favicon','wb') as f:
        f.write(response.content)

# getDemo05()



'''
    POST 
    Content-Type：application/form-data
'''

'''
    POST 
    Content-Type：application/json
'''

def postDemo01():
    # 请求body
    data={ 'age':'22'}
    response=requests.post("http://httpbin.org/post",data=data)
    print(response.text)
# postDemo01()  
  
'''
    POST 
    Content-Type：application/x-www-form-urlencoded
'''

'''
    POST 
    Content-Type：multipart/form-data
'''

'''
    POST 
    Content-Type：text/xml
'''