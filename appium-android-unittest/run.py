import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

test_dir = './testcase'
discover = unittest.defaultTestLoader.discover(start_dir='./testcase', pattern="test*.py")

if __name__ == "__main__":
    # 报告生成
    report_dir = './test_report' # 报告存放路径位置
    os.makedirs(report_dir, exist_ok=True)# 创建文件夹
    now = time.strftime("%Y-%m-%d %H-%M-%S")# 获取当前日期时间
    report_name = '{0}/{1}.html'.format(report_dir, now) # 报告文件名拼接
    # 写入数据到报告中
    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="测试报告", description="本测试报告内容包含超级计算器的简单测试")
        runner.run(discover)# 调用HTMLTestRunner.py函数，解析数据，生成报告
        
'''
    python run.py
'''