# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: md5_demo1
# Author: xiaxu
# DATA: 2022/9/23
# Description:
# ---------------------------------------------------
import hashlib


def hashstr(string):
    return hashlib.md5(string.encode("utf-8")).hexdigest()

if __name__ == '__main__':
    string = "python天下第一"
    print(hashstr(string))