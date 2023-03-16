# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: interface_request
# Author: xiaxu
# DATA: 2022/9/28
# Description: 模拟连接请求
# ---------------------------------------------------
import requests


url = "http://172.16.30.105:9060/FileUpload/services/UploadFile"
data = {
    "user":"xx",
    "password":'123456'
}
res = requests.get(url=url,params=data)
print(res)
print(type(res))
print(res.content)
print(res.headers)