import os
from datetime import datetime
from threading import Timer

# 定时任务


def task():
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    print(datetime.now())
    a = os.system("jmeter -n -t /Users/liyinchi/workspace/功能测试/好慷/测试数据（压测脚本）/阶梯拼团多维表格20230418.jmx -l /Users/liyinchi/workspace/功能测试/好慷/测试数据（压测脚本）/阶梯拼团多维表格20230418-result.jtl")
    print(a)

# 执行器


def func():
    task()
    t = Timer(60*1, func)
    t.start()


func()
