# -*- coding:utf-8 -*-
#@author:Fillico
#@date:2019/4/23 15:12

import random
from python_api_3.common.do_excel import *
from python_api_3.common import contants
from python_api_3.common.config import *
from python_api_3.common import do_mysql
from python_api_3.common import do_excel
from ddt import ddt,data,unpack
import unittest

@ddt
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'register')
    cases = excel.get_cases()

    def setUp(self):
        self.http_request = HttpSessionRequest()
        self.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_register(self, case):
        cases=DoExcel(contants.case_file,'register').get_cases()

        if case.data.find('register_mobile') > -1:
            sql = 'SELECT MAX(mobilephone) FROM future.member'
            max_phone = self.mysql.fetch_one(sql)[0]  # 查询最大手机号码,fetch_one()返回的是一个元组
            # max_phone = int(max_phone) + 1
            print(max_phone)
            random_num = random.randint(100, 999)
            phone = int(max_phone) - random_num  # 用最大手机号减去一个随机数，生成一个新的手机号
            case.data = case.data.replace('register_mobile', str(phone))
            print(case)



