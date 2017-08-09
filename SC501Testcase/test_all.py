#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki

import unittest
import sys
from config import globalconfig

# sys.path.append("E:\\Python_simple\\SC501Testcase\\test_case")
sys.path.append(globalconfig.test_case_path)
from test_case import *
import HTMLTestRunner
import time

# allcase = "E:\\Python_simple\\SC501Testcase\\test_case"  # 指明要自动查找的py文件所在文件夹路径


allcase = globalconfig.test_case_path
allsuite = unittest.defaultTestLoader.discover(allcase, pattern='test*.py', top_level_dir=None)
# def createsuite():  # 加载所有测试用例成测试套件函数
#     testsuite = unittest.TestSuite()
#     discover = unittest.defaultTestLoader.discover(allcase, pattern='test*.py', top_level_dir=None)
#     for suite in discover:
#         for case in suite:
#             testsuite.addTest(case)
#     print(testsuite)  # 打印出加载的测试用例
#     return testsuite
#
# allsuite = createsuite()

# suite.addTest(unittest.makeSuite(testlogin.Weblogin))  # 注意使用套件时，在单个py文件中下的多个用例用（类名（"方法名"））,导入多个py的类下，用（py名.类名）

# 读取当前时间，将时间加到测试报告名称中去,文件名规定不许有”\/:?*“等符号
now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time())))

# 定义测试报告存放的路径
# file_path = "E:\\Python_simple\\SC501Testcase\\test_reports\\" + now + "result.html"
file_path = globalconfig.report_path + "\\" + now + "result.html"
file_result = open(file_path, 'wb')

# 定义测试报告输出格式
runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title="测试报告", description="用例执行情况")

# 运行测试用例
runner.run(allsuite)
file_result.close()  # 关闭文件
