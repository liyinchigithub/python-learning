#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test23-golb.py
# Python 通配符
# https://note.youdao.com/s/KO8xvnYy

from glob import glob
import pytest
import string
import glob
'''
    文件通配符
'''
@pytest.mark.test
def test_glob():
    files =glob.glob('*.py');# 过滤，只搜索以py结尾的文件
    print(files)
    
'''
输出
test23-golb.py::test_glob ['test7-list.py', 'test_class-object.py', 'test19.py', 'test20-date-time.py', 'test_server-http.py', 'test21-string-find.py', 'test6-condition.py', 'test14-input-output.py', 'test17.py', 'test16-namespace.py', 'test2-comments.py', 'test22-golbal-variable.py', 'test9-tuple.py', 'test_mysql.py', 'test3-operator.py', 'test_mongodb.py', 'test_client-http-urllib.py', 'test11-dict.py', 'test12-function.py', 'test8-for-while.py', 'test_server-socket.py', 'test_file.py', 'test_pytesseract.py', 'test_client-http-requests.py', 'test1-data-type.py', 'test10-set.py', 'test_client-http-request.py', 'test13-module.py', 'test15-error-exception.py', 'test_csv.py', 'test18-os.py', 'test23-golb.py']
'''


'''
listglob1 = glob.glob("/Users/my_python/*.py")
# 过滤，只搜索以py结尾的文件。
print(listglob1)

listglob2 = glob.glob("/Users/my_python/0?.py")
print(listglob2)

listglob3 = glob.glob("/Users/my_python/0[0,1,2].py")
print(listglob3)

listglob4 = glob.glob("/Users/my_python/0[0-3].py")
print(listglob4)

listglob5 = glob.iglob("/Users/my_python/0[a-z].py")
print(listglob5)


for item in listglob1:
    print(item)
'''