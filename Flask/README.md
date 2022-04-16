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

## Content-Type

### application/json

### application/x-www-form-urlencode

### application/xml

### mulitipart/form-data

