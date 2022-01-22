
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test-pytest-mark.py
# pytest smoke
# 配置冒烟测试

'''
    一个完整的项目，测试用例比较多，比如：我们想将某些用例用来做冒烟测试，那该怎么办呢？pytest中可以自定义配置文件，用例按照指定的方式去运行。
    可以在项目根目录下，创建一个文件：pytest.ini  文件内容如下：
'''

'''
    [pytest]
    markers =
        demo: just for demo
        smoke
'''




import pytest
import sys

@pytest.mark.skip(reason="功能未实现,暂不执行")
# 类级别冒烟测试
@pytest.mark.smoke
class TestDemo:
    def test_demo01(self):
        print("这是test_demo01")

    def test_demo02(self):
        print("这是test_demo02")

    def test_demo03(self):
        print("这是test_demo03")

    def test_demo04():
        print("这是test_demo04")

@pytest.mark.skip(reason="功能未实现,暂不执行")
# 函数级别冒烟测试
@pytest.mark.smoke
def test_demo04():
    print("这是test_demo04")
    
'''
    命令行执行：pytest -v -m smoke test_demo.py
'''
if __name__=="__main__":
    TestDemo.__name__