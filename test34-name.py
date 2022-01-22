#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test34-name.py
# Python 当前程序的模块名称
# https://www.runoob.com/python3/python3-module.html
import sys
import pytest
import support;

'''
__name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。
如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
'''


@pytest.mark.test
def test_import01():
  support.print_func("Runoob") # support.py Hello :  Runoob


if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')  # 会被输出
   
'''
说明: 每个模块都有一个__name__属性，当其值是'__main__'时，[表明该模块自身在运行，否则是被引入]。
说明:__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
'''

'''
  dir() 函数 [返回模块内所有函数、变量名称]
  内置的函数 dir() 可以找到模块内定义的所有名称。
  以一个字符串列表的形式返回:

>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
 '__package__', '__stderr__', '__stdin__', '__stdout__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
 '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
 'call_tracing', 'callstats', 'copyright', 'displayhook',
 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
 'thread_info', 'version', 'version_info', 'warnoptions']


'''

'''
如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir() # 得到一个当前模块中定义的属性列表
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
>>> a = 5 # 建立一个新的变量 'a'
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'sys']
>>>
>>> del a # 删除变量名a
>>>
>>> dir()
['__builtins__', '__doc__', '__name__', 'sys']
>>>
'''