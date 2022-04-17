#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
import requests

@pytest.mark.testing
def test_():
    url = "http://127.0.0.1:5876/upload"

    payload={}
    files=[
    ('file',('测试.jpg',open('../../../Flask/app/static/测试.jpg','rb'),'image/jpeg'))# 文件名，文件，文件类型 rb 二进制文件
    ]
    headers = {
    'Cookie': 'cookie_key=cookie_value'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)