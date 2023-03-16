# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: interface_test
# FN: request_flask
# Author: xiaxu
# DATA: 2022/9/28
# Description:request 方法和属性整理
# ---------------------------------------------------
from flask import Flask
from flask import Flask,request


app = Flask(__name__)
@app.route("/api/login",methods=["GET","POST"])
#视图函数
def request_flask():
    # a = request.get_data() #bytes，原来格式接收数据
    # b = request.get_json() #将请求参数做了处理，得到的是字典格式的，因此排序会打乱依据字典排序规则
    # c = request.data
    # print(a)
    # print(b)
    # print(c)
    # print(type(a),type(b),type(c))#可以获取未经处理过的原始数据
    # get请求的一些request方法和属性
    print(request.args.get("user")) #获取user的值
    print(request.args) #可以获取get请求的所有参数返回值是ImmutableMultiDict类型
    print(request.args.to_dict())


    #公共方法
    print(request.headers)
    print(request.method)
    print(request.url)

    return "Hello request!"

if __name__ == '__main__':
    app.run()