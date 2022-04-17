# Flask-demo

## 启动服务

```shell
cd /Flask/app
python run.py
```



## Flask JWT


## Flask 跨域

```shell
pip install flask-cors
```

```python
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app, supports_credentials=True)
 
if __name__ == "__main__":
    app.run()
```

Response header中加入header
```python
@app.after_request
def af_request(resp):     
    """
     #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp
```

### 获取请求参数方式

* 1.request.form['key']

针对 request body json 或 form-data
```python
    data = request.form['data']  # 获取值
    return json.dumps(data, ensure_ascii=False)
```
* 2.request.get_data    

>针对 POST request body json
```python
    # 获取请求参数
    request_data = request.get_data() 
    # 对于前端POST请求发送过来的json数据，Flask后台可使用 request.get_data() 来接收数据，数据的格式为 bytes；再使用 json.loads() 方法就可以转换字典。
    # 将bytes类型转换为json数据
    request_json_data = json.loads(request_data)# 将json字符串数据转换为字典
    username = request_json_data.get('username')# 获取num1
    password = request_json_data.get('password')# 
    # return json.dumps({"username":username,"password":password})# 将字典转换为json字符串
    return {"username":username,"password":password }# 返回json数据
```

* 3.request.args.get('key') 

>针对 GET url ?之后的参数

```python
request.args.get('key') # request url param
```

* 4.request.form['key']

>针对GET 但有from-data

```python
get_data=request.form['username']# request form-data

```

* 5.request.args.to_dict()

>针对 POST request url params
```python
    get_data = request.args.to_dict()# 获取传入的params参数
    username = get_data.get('username')
    password = get_data.get('password')
    return {"msg": "success", "status": 200, "data": {"username":username,"password":password}}
```

* 6.request.json.get('key')

>针对 POST request body json
```python
    username = request.json.get('username')
    password = request.json.get('password')
    return {"msg": "success", "status": 200, "data": {"username":username,"password":password}}
```


### 重定向到指定路由函数

```python
return redirect(url_for('函数名'))  # 重定向
```


## Content-Type

### application/json

### application/x-www-form-urlencode

### application/xml

### mulitipart/form-data

#### 文件上传

在 Flask 中处理文件上传非常简单。它需要一个 HTML 表单，其 ​enctype​ 属性设置为“​multipart/form-data”​，将文件发布到 URL。

URL 处理程序从 ​request.files[]​ 对象中提取文件，并将其保存到所需的位置。

每个上传的文件首先会保存在服务器上的临时位置，然后将其实际保存到它的最终位置。

目标文件的名称可以是硬编码的，也可以从 ​request.files[file] ​对象的​ filename ​属性中获取。

使用 ​secure_filename()​ 函数获取它的安全版本。



