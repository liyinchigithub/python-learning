#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# test-server-http.py
# requests库
# http://www.zzvips.com/article/150840.html
# https://mp.weixin.qq.com/s/ZUCx7_sOGtPYDNMlx5I7IQ
# https://blog.csdn.net/qq_43645530/article/details/104088859   
# [代码可以通过postman生python code]

from os import error
import requests
import pytest
import json

'''
    [pip命令安装]
    windows系统下，输入命令 'pip install requests'
    linux、mac系统下，输入命令 'sudo pip install requests'
    
    [下载安装包安装（手动安装）]
    由于pip命令可能安装失败所以有时我们要通过下载第三方库文件来进行安装。
    在github上的地址为：https://github.com/requests/requests 下载文件到本地之后，解压到python安装目录。
    之后打开解压文件，在此处运行命令行并输入：
    'python setup.py install'
'''

'''
    [requests]7个主要方法
            方法	        解释
    requests.request()	构造一个请求，支持以下各种方法
    requests.get()	获取html的主要方法
    requests.head()	获取html头部信息的主要方法
    requests.post()	向html网页提交post请求的方法
    requests.put()	向html网页提交put请求的方法
    requests.patch()	向html提交局部修改的请求
    requests.delete()	向html提交删除请求
'''

'''
    [response]
            属性	            说明
    response.status_code	    http请求的返回[状态码]，若为200则表示请求成功。
    response.text	            http响应内容的[字符串形式]，即返回的页面内容
    response.encoding	        从http header 中猜测的相应内容[编码方式]
    response.apparent_encoding	从内容中分析出的响应内容[编码方式]（备选编码方式）
    response.content	        http响应内容的[二进制形式]
'''

'''
    [response属性示例]
    >>> import requests
    >>> r=requests.get("http://www.baidu.com")
    >>> r.status_code
    200
    >>>  r.encoding
    'ISO-8859-1'
    >>> r.apparent_encoding
    'utf-8'
    >>> r.text
    '<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta ht。。。
    >>> r.encoding='utf-8'
    >>> r.text
    '<!DOCTYPE html>\r\n<!--STATUS OK--><html>。、。。
    以上r.text内容过长，自行删除了部分，看出编码效果即可）
'''
'''
    [request]
    requests.request(）支持其他所有的方法。 
    requests.request(method，url,**kwargs)

    method: “GET”、”HEAD”、”POST”、”PUT”、”PATCH”等等
    url: 请求的网址
    **kwargs: 控制访问的参数
'''
@pytest.mark.test
def test_requests_request():
    url = "http://110.xx.xx.59:8000/api/json?pretty=true"
    payload={}
    headers = {
    'username': 'liyinchi',
    'Authorization': 'Basic xxxx=='
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
'''
    [GET]
    [示例]
    r=requests.get(url,params,**kwargs)
    [参数]
    第一个参数  url:需要爬取的网站地址。
    第二个参数  params:翻译过来就是参数， url中的额外参数，字典或者字节流格式，可选。
    第三个参数  **kwargs:12个控制访问的参数
    
        ①params:字典或字节序列， 作为[参数]增加到[url中],使用这个参数可以把一些键值对以"?key1=value1&key2=value2"的模式增加到url中
            例如:kv = {'key1':' values', 'key2': 'values'} 
            r = requests.get('http:www.python123.io/ws', params=kv)
        ②data:字典，字节序或文件对象，作为[参数]重点作为向服务器提供或提交资源是提交，作为request的内容，与params不同的是，data提交的数据并不放在url链接里， 而是放在url链接对应位置的地方作为数据来存储。它也可以接受一个字符串对象。
        ③json:json格式的数据，作为[参数]json合适在相关的html，http相关的web开发中非常常见， 也是http最经常使用的数据格式， 他是作为内容部分可以向服务器提交。
            例如:kv = {'key1': 'value1'} 
            r = requests.post('http://python123.io/ws', json=kv)
        ④headers:字典是http的相关语，作为[请求头参数]对应了向某个url访问时所发起的http的头i字段， 可以用这个字段来定义http的访问的http头，可以用来模拟任何我们想模拟的浏览器来对url发起访问。
            例子: hd = {'user-agent': 'Chrome/10'} 
            r = requests.post('http://python123.io/ws', headers=hd)
        ⑤cookies:字典或CookieJar，指的是从http中解析cookie
            如何共享cookie？通过requests内置session方法（这边session区别于后端开发session）
        ⑥auth:元组，用来支持http[认证]功能
            例子: auth = {'': 'Chrome/10'} 
            r = requests.post('http://python123.io/ws', auth=auth)
        ⑦files:字典， 是用来向服务器[传输文件]时使用的字段。
            例子:fs = {'files': open('data.txt', 'rb')} 
            r = requests.post('http://python123.io/ws', files=fs)

        ⑧timeout: 用于设定[超时时间]， 单位为秒，当发起一个get请求时可以设置一个timeout时间， 如果在timeout时间内请求内容没有返回， 将产生一个timeout的异常。
        ⑨proxies: 字典,用来设置访问[代理]服务器。
        ⑩allow_redirects: 开关,表示是否允许对url进行[重定向]， 默认为True。
        stream: 开关,指是否对获取内容进行立即下载， 默认为True。
        verify: 开关,用于认证[SSL证书]， 默认为True。
        cert: 用于设置保存本地[SSL证书路径]
'''
'''
    [GET]
'''


@pytest.mark.skip
def test_get_01():
    response = requests.get('http://httpbin.org/get')
    print(response.text)# 返回的是json格式的数据
    print(type(response.text))# 返回的是str类型
    # 字符串转字典 str转dict
    print(eval(response.text))# 字符串转字典

'''
    [GET]
'''


@pytest.mark.skip
def test_get_02():
    response = requests.get("https://www.csdn.net")
    # 输出response的类型、状态码、响应体的类型、内容以及 Cookies
    print(type(response))# <class 'requests.models.Response'>
    print(response.status_code)  # 响应状态码
    print(response.headers)  # 响应头
    print(response.request.headers)  # 获取发送给服务器的头文件信息
    print(type(response.text))  # 响应body类型
    print(response.text)  # 响应body
    # 响应cookies  urllib 处理过 Cookies，写法比较复杂，而有了 requests，获取和设置 Cookies 只需 一步即可完成
    print(response.cookies)
    # print(response.cookies['cookie'])# 获取cookies中cookie，用于长久登录
    print(response.encoding)  # 获取当前的编码
    headers = response.headers
    print('headers["Server"]:'+headers['Server'])
    #
    print(response.json())  # JSON格式的响应内容，如果解码失败，result.json()将会引发异常
    print(response.content)  # J二进制响应内容


'''
    [GET]
    params相当于response = requests.get(‘http://httpbin.org/get?name=germey&age=22’)
'''


@pytest.mark.skip
def test_get_03():
    # 附加额外的信息，比如:URL想添加两个参数， 其中 name 是 germey, age 是 22
    p = {
        'name': 'germey',
        'age': '22'
    }
    response = requests.get('http://httpbin.org/get', params=p)# 参数是一个字典，相当于response = requests.get('http://httpbin.org/get?name=germey&age=22')
    print(response.text)


'''
    [GET]
    请求头信息
'''


@pytest.mark.skip
def test_get_04():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'content-type': "application/json"
    }
    response = requests.get("https://www.zhihu.com/", headers=headers)
    print(response.text)
    print(eval(response.text))# 字符串转字典


'''
    [GET]
    提取到的图片保存下来
'''


@pytest.mark.skip
def test_get_05():
    response = requests.get("https://github.com/favicon.ico")# 获取图片
    # 保存图片
    with open('favicon.ico', 'wb') as f:
        f.write(response.content)  # 保存本地


'''
    [GET]
    可以直接用 Cookie来[维持登录状态]
'''


@pytest.mark.skip
def test_get_06():
    headers = {
        # 但这种方式cookie很长，requests提供了Session()共享cookie
        'Cookie': '_zap=2c12f14e-ef5d-4afc-ab3e-af33e0d7ed0b; d_c0="ANDsdiitNxCPTspQdwQQy2y1EwauWeT9H3M=|1571394286"; _xsrf=APdnMsYkSILBvUiKknwPxvtpK6EOacPA; r_cap_id="NmRmZDY1NmM0YzZjNGE3Njg5YmM1MzM5MjNhNzI3ZjE=|1579144278|231a7c1fec00014281cfb717ea77867c2e122535"; cap_id="Y2VlODAxNWYwYzIyNDQ3NTlkZThhZDkwNDhhZTNiMDc=|1579144277|bc245c6af50afe5749eab0f8d357161829810f6a"; l_cap_id="YjQwNzAzNmYzMTA0NDkwZjliOGI0OWYyMzVmNzYxYzM=|1579144278|f2e2c15cfd95c7af51ddf9997ca386d4a3711824"; auth_type=cXFjb25u|1579144288|87cf27a6b4af8d334fa5435775572d18aee1f21d; token="QzUzMjlDNTM0NDhCQTExQjk1NEY1MUY0QTU0RTRDOUY=|1579144288|96f52c6bcd169ef7b62b98719ce2f5dbce8e9313"; client_id="RDRENDRBRjc1OUI0RjIxMDQ2REExRkY2RENFQzdFRjc=|1579144288|cae4206c32d633d8cf04e059304df93b27557e9c"; capsion_ticket="2|1:0|10:1579144305|14:capsion_ticket|44:N2E3MjE1OTBkNzhiNGE0ZGE3YmFmNzU1ODU5NDU5NGE=|73d1cd2ba8a22e91ad5afa6d35967b23f0b493afe0442a2fa02a94361aec0afd"; z_c0="2|1:0|10:1579144348|4:z_c0|92:Mi4xMDlyZ0F3QUFBQUFBME94MktLMDNFQ2NBQUFDRUFsVk5tMkZIWGdCUnFHOEotN1I1QzdmQmNHc29FOC1xUXdmZDJn|2516938d91343daf8e7424f789c79c9908672429bdb7a45bedf499c3a4346846"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1579144204,1580039199; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1580040949; KLBRSID=ca494ee5d16b14b649673c122ff27291|1580040953|1580039197',
        'Host': 'https://www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    response = requests.get("https://zhihu.com", headers=headers)
    print(response.text)


'''
    [GET]
    [会话维持(共享cookie/共享登录状态)]
    解决这个问题的主要方法就是维持同一个会话，相当于打开一个新的浏览器选项卡而不是新开一个浏览器。
    但是我又不想每次设置cookie这时候就有了Session对象。
    利用Session可以做到模拟同一个会话而不用担心Cookies的问题,它通常用于模拟登录成功之后再进行下一步的操作。
'''


@pytest.mark.skip
def test_get_07():
    response = requests.Session()  # 共享cookie
    response.get('http://httpbin.org/cookies/set/number/123456789')  # 登录请求
    result = response.get('http://httpbin.org/cookies ')  # 业务请求
    print(result.text)  # unicode


'''
    [GET]
    [SSL证书验证]
'''


@pytest.mark.skip
def test_get_ssl_08():
    try:
        response = requests.get('https://wvm.12306.cn', verify=False)
        print(response.status_code)
    except OSError:
        print("出现异常")  # 输出 <class 'OSError'>
        # 抛出异常进行检查，如果我们的请求是执行成功的，即状态码为200，此时raise_for_status()的值将会是None
        print(response.raise_for_status())


'''
    [GET]
    [代理设置]
'''


@pytest.mark.skip
def test_get_proxy_09():
    proxies = {
        "https": "http://110.10.1.10:3128", "https": "http://10.10.1.10:1080",
    }
    response = requests.get("https://www.taobao.com", proxies=proxies)
    print(response.status_code)  # 响应状态码


'''
    [GET]
    [超时设置]
'''


@pytest.mark.skip
def test_get_timeout_10():
    response = requests.get('https://www.taobao.com', timeout=10)
    print(response.status_code)  # 响应状态码


'''
    [GET]
    [身份认证]
    requests还提供了其他认证方式，如 OAuth认证,更多详细的功能可以参考requests_oauthlib的官方文档
    https://requests-oauthlib.readthedocs.org/
'''


@pytest.mark.skip
def test_get_auth_11():
    response = requests.get(
        'http://110.40.xxx.59:8000/api/json?pretty=true', auth=('admin', 'xxxx'))
    print(response.status_code)  # 响应状态码


'''
    [POST] 
    [Content-Type：application/form-data]
'''

'''
    [POST] 
    [Content-Type：application/json]
'''


@pytest.mark.skip
def test_post_01():
    data = {'age': '22'}  # 请求body
    response = requests.post("http://httpbin.org/post", data=data) #向url post 一个字符串，自动编码为data
    print(response.text)
    print(eval(response.text)['form'])#转换为字典

@pytest.mark.skip
def test_post_json_01():
    json = {'age': '22'}  # 请求body
    response = requests.post("http://httpbin.org/post", json=json)
    print(response.text)
    
'''
    json
'''
@pytest.mark.skip
def test_post_json_02():
    response = requests.get("http://httpbin.org/get")
    print(type(response.text))# <class 'str'>
    print(response.json())# <class 'dict'>
    print(json.loads(response.text)) # <class 'dict'>

'''
    [POST] 
    [Content-Type：application/json]
'''
@pytest.mark.test
def test_post_02():
    payload={"key1":"value1","key2":"value2"}
    response=requests.post("http://httpbin.org/post",data=payload)
    print(response.text)


'''
    [POST] 
    [Content-Type:application/x-www-form-urlencoded]
'''

'''
    [POST] 
    [Content-Type:multipart/form-data]
    [文件上传/上传文件]
'''
@pytest.mark.skip
def test_fileUpdate():
    with open('./file/demo01.txt', 'rb') as f:  # 读取被上传文件
        response = requests.post(
            'http://localhost:5000/post', files={"files": f})
        print(response.status_code)


'''
 返回内容
        {
        "args": {}, 
        "data": "", 
        "files": {
            "file ": "data:application/octet-stream;base64,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AAAAAAAAKysrBhYWGUcWFhiVFRUYvxUVGNkWFhfzFhYX8xUVGNkVFRi/FhYYlRYWGUcrKysGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
        }, 
        "form": {}, 
        "headers": {
            "Accept": "*/*", 
            "Accept-Encoding": "gzip, deflate", 
            "Content-Length": "6666", 
            "Content-Type": "multipart/form-data; boundary=63947df8ef8b263c61f6532b1c37ae35", 
            "Host": "httpbin.org", 
            "User-Agent": "python-requests/2.27.1", 
            "X-Amzn-Trace-Id": "Root=1-61ef98a1-71e6cdc146ba13121cd0b97d"
        }, 
        "json": null, 
        "origin": "218.102.206.56", 
        "url": "http://httpbin.org/post"
        }
'''


'''
    [POST] 
    [Content-Type:text/xml]
'''

'''
    [PUT] 
'''
@pytest.mark.test
def test_put():
    payload={"key1":"value1","key2":"value2"}
    response=requests.put("http://httpbin.org/put",data=payload)
    print(response.text)

'''
    [PATCH] 
    requests.patch和request.put类似。 
    两者不同的是： 
    当我们用patch时仅需要提交需要修改的字段。 
    而用put时，必须将20个字段一起提交到url，未提交字段将会被删除。 
    patch的好处是：节省网络带宽。
'''

'''
    DELETE 
'''

'''
    HEAD 
'''
@pytest.mark.skip
def test_heade():
    response=requests.head("http://httpbin.org/get")
    print(eval(str(response.headers))) # 字典转字符串再转成字典


'''
    [共享cookie]
    requests库提供一个session对象
    [注意]
    这边requests的session对象，要区别于服务端开发session概念，两个不是同一个。
    这边session仅用于共享每个请求之间cookie，比如：登录状态。
'''



'''
    [捕捉状态异常]
    requests库有时会产生异常，比如网络连接错误、http错误异常、重定向异常、请求url超时异常等等。
    所以我们需要判断r.status_codes是否是200，在这里我们怎么样去捕捉异常呢？
    
    可以利用[r.raise_for_status() ]语句去捕捉异常，该语句在方法内部判断r.status_code是否等于200，如果不等于，则抛出异常
'''

@pytest.mark.skip
def test_raises():
    # 爬取网页的通用代码框架
    url="https://www.qq.com"
    try:
        response=requests.get(url,timeout=30)#请求超时时间为30秒
        response.raise_for_status()#如果状态不是200，则引发异常
        response.encoding=response.apparent_encoding #配置编码
        print(response.text)
        return response.text
    except:
        return "产生异常" 
    
    
'''
    [响应头]
'''
@pytest.mark.skip
def test_response_headers():
    response=requests.head("http://httpbin.org/get")
    print(eval(str(response.headers))) # 字典转字符串再转成字典
    
'''
    输出:
    {
	'Date': 'Tue, 25 Jan 2022 06:37:35 GMT',
	'Content-Type': 'application/json',
	'Content-Length': '307',
	'Connection': 'keep-alive',
	'Server': 'gunicorn/19.9.0',
	'Access-Control-Allow-Origin': '*',
	'Access-Control-Allow-Credentials': 'true'
    }
'''