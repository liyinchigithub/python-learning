
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test_pytest-allure-report.py
# pytest+allure
# 测试报告
# https://www.cnblogs.com/hl-2030/p/13690165.html?ivk_sa=1024320u

'''
    1.下载allure
    https://github.com/allure-framework/allure2/releases
    2.放入到根目录
    安装
    pip install allure-pytest
    3.配置环境变量
        【window】
         https://www.cnblogs.com/hl-2030/p/13690165.html?ivk_sa=1024320u
        【mac、linux】
         cd ~
         vim .bash_profile 
         export ALLURE_HOME=/Users/liyinchi/workspace/python/python-learning/allure-2.17.2/
         export PATH=$PATH:ALLURE_HOME/bin
         allure --version
    4.在项目根目录下新建目录report
'''

'''
    在report目录下，新建目录html，用于存放html报告
'''

import pytest

@pytest.mark.flaky(reruns=2,reruns_delay=2)
def test_demo():
    assert 3==4
    
'''
    执行命令：cd test-pytest
    执行命令（json）：pytest -s -q --alluredir ./report
    执行命令（html）：allure generate ./report -o ./report/html
'''