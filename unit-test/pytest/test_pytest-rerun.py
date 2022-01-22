
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test-pytest-rerun.py
# pytest 之return
# 重新运行
# https://blog.51cto.com/u_10913485/2898629

'''
    在做UI自动化，如Selenuim或者Appium时，遇到某些元素未能及时显示，导致点击失败，如果加上重跑，那么将有效提高报告的准确性。
    在Pytest中，可以使用pytest-rerunfailures用来失败用例重跑。
'''

'''
    安装
    pip install pytest-rerunfailures
'''
import pytest
@pytest.mark.skip(reason="功能未实现,暂不执行")
# 重新运行
@pytest.mark.flaky(reruns=2)
def test_demo():
    assert 3 == 4
    print('一次')
    
@pytest.mark.skip(reason="功能未实现,暂不执行")
# 指定运行等待时间
@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_demo():
    assert 3==4
