#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from python_utils import converters
import pytest;

'''
    工具库
    https://python-utils.readthedocs.io/en/latest/
'''

@pytest.mark.test
def test_():
    number = converters.to_int('spam15eggs')
    assert number == 15
    
    number = converters.to_int('spam')
    assert number == 0
    
    number = converters.to_int('spam', default=1)
    assert number == 1
    
    number = converters.to_float('spam1.234')