#!/usr/bin/python3
# -*- coding: UTF-8 -*-


if __name__=="__main__":
    print("主程序入口")
else :
    # 模块被其他模块引入调用时候，这边便会输出
    print("package __init__ 初始化/非主程/被引入或单元测试")
    