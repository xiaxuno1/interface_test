# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: test
# Author: xiaxu
# DATA: 2022/10/18
# Description:
# ---------------------------------------------------

str1 = '{"read":("token",)}'
str1_dict = eval(str1)
str1_con = str1_dict['read']
print(str1_dict)
print(str1_dict['read'],type(str1_con))
print(str1_dict.get('read'))
print('构建完成')