# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: interface_request
# Author: xiaxu
# DATA: 2022/9/28
# Description:
# ---------------------------------------------------
import requests


url = "http://127.0.0.1:5000"
data = {
    "user":"xx",
    "password":'123456'
}
res = requests.get(url=url,params=data)
print(res)
print(res.content)
print(res.headers)