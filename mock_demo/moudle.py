# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: moudle
# Author: xiaxu
# DATA: 2022/9/23
# Description:一些功能模块
# ---------------------------------------------------


class AlarmDeal():
    """
    报警处理流程
    """
    def __init__(self,alarm):
        alarm_inf = alarm

    def alarm_confirm(self,alarm):
        """
        报警确认
        :param alarm:
        :return:
        """
        pass

    def alarm_reson(self,seson):
        """
        报警原因
        :param seson:
        :return:
        """
        pass

    def alarm_delete(self,alarm):
        """
        报警销号
        :param alarm:
        :return:
        """

class Count():

    def price(self,a,b):
        """
        ：计算选中商品的价钱
        :param a:
        :param b:
        :return:
        """
        return a+b

    def pay(self,price):
        print("支付完成:",price)
