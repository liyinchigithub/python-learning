# Flask-demo


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
```python
    data = request.form['data']  # 获取值
    return json.dumps(data, ensure_ascii=False)
```
* 2.request.get_data
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

* 3.request.form['key']

```python
request.form['username']
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

