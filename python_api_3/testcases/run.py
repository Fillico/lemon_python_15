# -*- coding:utf-8 -*-
# @author:Fillico
# @date:2019/4/26 11:09

import sys

sys.path.append('./')
print(sys.path)

import HTMLTestRunnerNew
import os
import unittest
from python_api_3.common import contants


suite = unittest.TestSuite()
loader = unittest.TestLoader()

discover = unittest.defaultTestLoader.discover(contants.case_dir, "test_*.py")

# 执行测试用例，并把结果输出到html文件中

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_file = os.path.join(base_dir, 'reports', 'test_future.html')

with open(html_file, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='20190426-前程贷测试报告',
        description='前程贷测试报告',
        tester='Fillico')
    runner.run(discover)
