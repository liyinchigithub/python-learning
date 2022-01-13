
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test-pytest.py
# pytest
# 第三方单元测试框架

'''
pytest是一个非常成熟的全功能的Python测试框架，主要特点有以下几点：
1、简单灵活，容易上手，文档丰富；
2、支持参数化，可以细粒度地控制要测试的测试用例；
3、能够支持简单的单元测试和复杂的功能测试，还可以用来做selenium/appnium等自动化测试、接口自动化测试（pytest+requests）;
4、pytest具有很多第三方插件，并且可以自定义扩展，比较好用的如pytest-selenium（集成selenium）、pytest-html（完美html测试报告生成）、pytest-rerunfailures（失败case重复执行）、pytest-xdist（多CPU分发）等；
5、测试用例的skip和xfail处理；
6、可以很好的和CI工具结合，例如jenkins

'''

'''
编写规则：
[测试文件]以test_开头（以_test结尾也可以）
[测试类]以Test开头，并且不能带有 init 方法
[测试函数]以test_开头
[断言]使用基本的assert即可
'''




import pytest
import sys

# # 
# @pytest.fixture(scope='function')
# def setup_function(request):
#     def teardown_function():
#         print("teardown_function called.")
#     request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
#     print('setup_function called.')

# # 
# @pytest.fixture(scope='module')
# def setup_module(request):
#     def teardown_module():
#         print("teardown_module called.")
#     request.addfinalizer(teardown_module)
#     print('setup_module called.')

# # 
# @pytest.mark.website
# def test_1(setup_function):
#     print('Test_1 called.')

# # 
# def test_2(setup_module):
#     print('Test_2 called.')

# # 
# def test_3(setup_module):
#     print('Test_3 called.')
#     assert 2 == 1+1


# 跳过整个类，执行测试用例(可选参数reason)跳过的原因，会在执行结果中打印
@pytest.mark.skip(reason="功能未实现,暂不执行")
class TestDemo():
 def test_demo01(self):
    print("这是test_demo01")
 def test_demo02(self):
    print("这是test_demo02")
@pytest.mark.skip(reason="功能未实现,暂不执行")
# 跳过某个方法
class TestDemo():
    def test_demo01(self):
        print("这是test_demo01")
    @pytest.mark.skip(reason="功能未实现,暂不执行")
    def test_demo02(self):
        print("这是test_demo02")

# 满足条件跳过
@pytest.mark.skipif(sys.version < '3.7', reason="python版本必须大于3.7")
def test_demo02():
    print("这是test_demo02")
    
@pytest.mark.skip(reason="功能未实现,暂不执行")
# 用例断言失败，且标记为xfail
@pytest.mark.xfail()
def test_demo02():
    print("这是test_demo02")
    assert 1==2
@pytest.mark.skip(reason="功能未实现,暂不执行")
# 用例断言成功，标记为xfail
@pytest.mark.xfail()
def test_demo02():
    print("这是test_demo02")
    assert 1==1
    
    
