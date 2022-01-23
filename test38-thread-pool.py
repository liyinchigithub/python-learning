#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# test38-thread-pool.py
# Python 多线程、线程池
# 
import pytest
import threading
import hashlib
import logging
from utils.progress import PrintProgress
from utils.save import SaveToSqlite

'''
    [多线程]
'''
@pytest.mark.test
def test_thread01():
    print("生成 0 ~ 9 之间的随机数:".format())


'''
    [线程池]
'''
@pytest.mark.test
def test_thread02():
    print("生成 0 ~ 9 之间的随机数:".format())

