# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: interface_test
# FN: mock_demo
# Author: xiaxu
# DATA: 2022/9/23
# Description:
# ---------------------------------------------------
from unittest import mock
from mock_demo.moudle import Count
import unittest


class TestPay(unittest.TestCase):
    def test_pay01(self):
        count = Count()
        #���ص��ú�����ֵreturn_value��ֵ��side_effect�滻��return_value��ֵ
        count.price = mock.Mock(return_value=13,side_effect=count.price)
        price = count.price(99,15)
        count.pay(price)
        assert True
if __name__ == '__main__':
    unittest.main()
