
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test-pytest-html-report.py
# pytest-html
# pytest测试报告

'''

'''

import pytest

@pytest.mark.skip(reason="功能未实现,暂不执行")
@pytest.mark.flaky(reruns=2,reruns_delay=2)
def test_demo():
    assert 3==4
    
'''
    命令行执行：
    pytest --html=report.html   # 根目录生成html报告
    pytest --html=./pytest-html/report.html # 指定目录生成html报告
'''