#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test54_unittest_ddt.py
import unittest
from parameterized import parameterized,param

class Test_class_03(unittest.TestCase):
    @classmethod # 必要修饰器
    def setUpClass(cls):
        print("Test_class_02 所有测试用例执行之前")
        
    @classmethod # 必要修饰器
    def tearDownClass(cls) -> None:
        print("Test_class_02 所有测试用例执行之后")
        
    def setUp(self) -> None:
        print("Test_class_02 每个测试用例执行之前")
        
    def tearDown(self) -> None:
        print("Test_class_02 每个测试用例执行之后")
        
    @parameterized.expand([(1,2,3),(4,5,6),(7,8,9)])# 列表中一个元素表示一个用例；区别于ddt是一个列表一个用例
    def test_02_01_sum(self,a,b,c):
        print("a={},b={},c={}".format(a,b,c))
        self.assertEqual(1,1)
        self.assertNotEqual(1,"1")
        self.assertTrue(1==1)
        self.assertFalse(1=="1")
        print("test_02_01_sum 测试用例")
        
    # @unittest.skip("跳过用例")    
    def test_02_02_sum(self):
        self.assertEqual(2,2)
        self.assertNotEqual(2,"2")
        self.assertTrue(2==2)
        self.assertFalse(2=="2")
        print("test_02_02_sum 测试用例")
            
    # @unittest.skip("跳过用例")   # skiIf 满足条件跳过； skipUnless 不满足条件跳过； skip 无条件跳过 
    def test_02_03_sum(self):
        self.assertEqual(3,3)
        self.assertNotEqual(3,"3")
        self.assertTrue(3==3)
        self.assertFalse(3=="3")
        # print("跳过用例")
        print("test_02_03_sum 测试用例")
        
        
'''
    运行脚本：
    1.整个文件（模块）
    python -m unittest -v 文件名
    2.类
    python -m unittest -v 文件名.类
    3.方法
    python -m unittest -v 文件名.类.方法名
    4.批量执行测试文件
    
'''

if __name__ == '__main__':
    unittest.main()