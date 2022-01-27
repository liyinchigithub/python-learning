#!/usr/bin/python3
# -*- coding: UTF-8 -*-




class compute:
    # 构造函数（模块类被实例化时执行，接收入参）
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # 类中的自定义函数
    def structure(self):
        result = self.a-self.b
        return result


if __name__ == "__main__":
        # 模块被其他模块引入调用时候，这边便会输出
    print("package_demo.module_b.compute.py __init__")

