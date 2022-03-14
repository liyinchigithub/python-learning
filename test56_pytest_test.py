#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test56_pytest.py

import pytest

# def setup_function() -> None:
#         print("不在类中，每个测试用例执行之前")
        
# def teardown_function() -> None:
#         print("不在类中， 每个测试用例执行之后")

# @pytest.mark.test
# @pytest.mark.L1
# def test_not_class_function():
#     print("test_not_class_function 不在类中，测试用例")


class Test():
    def setup_class(self) -> None:
        print("setup_class 整个类之前")
        
    def teardown_class(self) -> None:
        print("teardown_class 整个类之后")
        
    def setup_method(self) -> None:
        print("Test_class_01 类中每个测试用例执行之前")
        
    def teardown_method(self) -> None:
        print("Test_class_01 类中每个测试用例执行之后")
        
    def setUp(self) -> None:
        print("setUp 每个测试用例执行之前")
        
    def tearDown(self) -> None:
        print("tearDown 每个测试用例执行之后")
    
    @pytest.mark.L1
    def test_01(self) -> None:
        print("test_01 测试用例")
        
    @pytest.mark.L2
    def test_02(self) -> None:
        
        print("test_02 测试用例")
        
    @pytest.mark.skip(reason="跳过用例")
    @pytest.mark.L3
    def test_03(self) -> None:
        print("test_03 测试用例")

                
if __name__ == '__main__':
        pytest.main(["-s","test56_pytest.py","--html=./reports/report.html"])# 运行指定文件
        
'''
    运行脚本：
    pytest -v test56_pytest_test.py
'''      

'''
    注意事项：
    1.文件名（模块）：必须以test_ 或者 _test开头
    2.测试类：必须以Test开头
    3.测试方法：必须以test_
    4.断言：assert
    5.执行结果：.表示成功 F表示失败 E表示发生错误
    6.测试固件：setup_module/teardown_module、setup_function/teardown_function、setup_class/teardown_class、setup_method/teardown_method、setup/teardown
'''