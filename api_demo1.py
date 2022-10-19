#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: api_demo1
# Author: xiaxu
# DATA: 2022/9/22
# Description:了解request的应用
# ---------------------------------------------------
import requests
import json

"""
#post请求提交数据
url = 'http://39.98.138.157:5000/api/login'
data = {
    "username":"admin",
    "password":"123456"
}
res = requests.post(url=url,data = data)
print("响应码：",res.status_code) #500
#print("内容content：",res.content)#会将整个html的所有数据以bytes的形式显示出来
#print("响应文本：",type(res.text),res.text)#会将整个html的所有数据以str的形式显示出来
#print("原始响应",res.raw) #显示为内存地址
print("url地址:",res.url)#
print("encoding编码方式:",res.encoding)#utf-8
print("cookies数据:",res.cookies)
#print("失败（非200）异常：",res.raise_for_status()) #500 Server Error
print("json格式:",res.json)
print("header响应头：",res.headers)
print(res)"""

#get请求
url = 'http://39.98.138.157:5000/api/getproductinfo'
params = "productid=8888"
res = requests.get(url,params)
print(res)
print(res.text)
data = json.loads(res.text) #转换为字典格式
print(data,type(data))
print(data['httpstatus'])
print(res.json()['data'],type(res.json())) #返回json格式
