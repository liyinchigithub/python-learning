#!/usr/bin/python
# -*- coding: UTF-8 -*-
# test-server-http.py
# requests库
# http://www.zzvips.com/article/150840.html
# 代码可以通过postman生python code

from os import error
import requests
import json
'''
    GET
'''

def getDemo01():
    response = requests.get('http://httpbin.org/get')
    print(response.text)
    print(type(response.text))
    # 字符串转字典 str转dict
    # eval(response.text)
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
    print(response.cookies)# 响应cookies  urllib 处理过 Cookies，写法比较复杂，而有了 requests，获取和设置 Cookies 只需 一步即可完成
    # print(response.cookies['cookie'])# 获取cookies中cookie，用于长久登录
    headers=response.headers;
    print('headers["Server"]:'+headers['Server'])
    #
    print(response.json()) # JSON格式的响应内容，如果解码失败，result.json()将会引发异常
    print(response.content) # J二进制响应内容
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
    with open('favicon.ico','wb') as f:
        f.write(response.content)

# getDemo05()

'''
    GET
    可以直接用 Cookie 来[维持登录状态]
'''
def getDemo06():
    headers={
    'Cookie':'_zap=2c12f14e-ef5d-4afc-ab3e-af33e0d7ed0b; d_c0="ANDsdiitNxCPTspQdwQQy2y1EwauWeT9H3M=|1571394286"; _xsrf=APdnMsYkSILBvUiKknwPxvtpK6EOacPA; r_cap_id="NmRmZDY1NmM0YzZjNGE3Njg5YmM1MzM5MjNhNzI3ZjE=|1579144278|231a7c1fec00014281cfb717ea77867c2e122535"; cap_id="Y2VlODAxNWYwYzIyNDQ3NTlkZThhZDkwNDhhZTNiMDc=|1579144277|bc245c6af50afe5749eab0f8d357161829810f6a"; l_cap_id="YjQwNzAzNmYzMTA0NDkwZjliOGI0OWYyMzVmNzYxYzM=|1579144278|f2e2c15cfd95c7af51ddf9997ca386d4a3711824"; auth_type=cXFjb25u|1579144288|87cf27a6b4af8d334fa5435775572d18aee1f21d; token="QzUzMjlDNTM0NDhCQTExQjk1NEY1MUY0QTU0RTRDOUY=|1579144288|96f52c6bcd169ef7b62b98719ce2f5dbce8e9313"; client_id="RDRENDRBRjc1OUI0RjIxMDQ2REExRkY2RENFQzdFRjc=|1579144288|cae4206c32d633d8cf04e059304df93b27557e9c"; capsion_ticket="2|1:0|10:1579144305|14:capsion_ticket|44:N2E3MjE1OTBkNzhiNGE0ZGE3YmFmNzU1ODU5NDU5NGE=|73d1cd2ba8a22e91ad5afa6d35967b23f0b493afe0442a2fa02a94361aec0afd"; z_c0="2|1:0|10:1579144348|4:z_c0|92:Mi4xMDlyZ0F3QUFBQUFBME94MktLMDNFQ2NBQUFDRUFsVk5tMkZIWGdCUnFHOEotN1I1QzdmQmNHc29FOC1xUXdmZDJn|2516938d91343daf8e7424f789c79c9908672429bdb7a45bedf499c3a4346846"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1579144204,1580039199; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1580040949; KLBRSID=ca494ee5d16b14b649673c122ff27291|1580040953|1580039197',
    'Host':'https://www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
            }
    response=requests.get("https://zhihu.com",headers=headers)
    print(response.text)
# getDemo06()

'''
    GET
    [会话维持]
    解决这个问题的主要方法就是维持同一个会话，相当于打开一个新的浏览器选项卡而不是新开一个浏览器。
    但是我又不想每次设置cookie这时候就有了Session对象。
    利用Session可以做到模拟同一个会话而不用担心Cookies的问题,它通常用于模拟登录成功之后再进行下一步的操作。
'''
def getDemo07():
    response = requests.Session()
    response.get('http://httpbin.org/cookies/set/number/123456789') 
    result = response.get('http://httpbin.org/cookies ') 
    print(result.text)
# getDemo07()


'''
    GET
    [SSL证书验证]
'''
def ssl():
    try:
        response = requests.get('https://wvm.12306.cn',verify=False)
        print(response.status_code) 
    except OSError:
        print("出现异常") # 输出 <class 'OSError'>
        print(response.raise_for_status())# 抛出异常进行检查，如果我们的请求是执行成功的，即状态码为200，此时raise_for_status()的值将会是None
# ssl()

'''
    GET
    [代理设置]
'''
def prox():
    proxies = { 
               "https":"http://110.10.1.10:3128", "https":"http://10.10.1.10:1080",
                }
    requests.get("https://www.taobao.com" , proxies=proxies) 
# prox()

'''
    GET
    [超时设置]
'''
def timeoutSet():
    response = requests.get('https://www.taobao.com',timeout=10)
    print(response.status_code)    
# timeoutSet()

'''
    GET
    [身份认证]
    requests还提供了其他认证方式，如 OAuth认证,更多详细的功能可以参考requests_oauthlib的官方文档
    https://requests-oauthlib.readthedocs.org/
'''
def auth():
    response = requests.get('http://110.40.156.59:8000/api/json?pretty=true',auth=('admin','xxxx'))
    print(response.status_code)
    
# auth()


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
    Content-Type：application/json
'''

def postDemo02():
    # 请求body
    files = {'file ' : open('favicon.ico','rb')} 
    response = requests.post('http://httpbin.org/post', files=files) 
    print(response.text)
# postDemo02()  


  
'''
    POST 
    Content-Type：application/x-www-form-urlencoded
'''

'''
    POST 
    Content-Type：multipart/form-data
    [文件上传]
'''

def fileUpdate():
    with open('demo01.txt','rb') as f:
        result = requests.post('http://localhost:5000/post',files={"files":f})
fileUpdate()

'''
    POST 
    Content-Type：text/xml
'''

'''
    PUT 
    
'''


'''
    DELETE 
'''