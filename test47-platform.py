#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test47-platform.py
# Python 判断当前系统
# https://blog.csdn.net/weixin_39553705/article/details/111004761
import sys
import pytest
import platform
import logging
'''
  
'''


@pytest.mark.test
def my_print(x):
    logging.info("platform.machine()=%s", platform.machine())

    logging.info("platform.node()=%s", platform.node())

    logging.info("platform.platform()=%s", platform.platform())

    logging.info("platform.processor()=%s", platform.processor())

    logging.info("platform.python_build()=%s", platform.python_build())

    logging.info("platform.python_compiler()=%s", platform.python_compiler())

    logging.info("platform.python_branch()=%s", platform.python_branch())

    logging.info("platform.python_implementation()=%s",
                 platform.python_implementation())

    logging.info("platform.python_revision()=%s", platform.python_revision())

    logging.info("platform.python_version()=%s", platform.python_version())

    logging.info("platform.python_version_tuple()=%s",
                 platform.python_version_tuple())

    logging.info("platform.release()=%s", platform.release())

    logging.info("platform.system()=%s", platform.system())

    #logging.info("platform.system_alias()=%s", platform.system_alias());

    logging.info("platform.version()=%s", platform.version())

    logging.info("platform.uname()=%s", platform.uname())


'''
   
'''