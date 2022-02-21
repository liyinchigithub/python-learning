#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import pytest
import sys


class computed:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        result = self.a+self.b
        return result

    def avg(self):
        return self.a/self.b


if __name__ == '__main__':
    print("test  class 是main")
else:
    print("被引入")
