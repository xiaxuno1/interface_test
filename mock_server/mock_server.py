# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: interface_test
# FN: mock_server
# Author: xiaxu
# DATA: 2022/9/28
# Description:基于flask实现mock_server，其实就是模拟服务器
# ---------------------------------------------------
from flask import Flask
from flask import request,jsonify


app = Flask(__name__)
app.config['JSONIFY_MIMETYPE'] ="application/json;charset=utf-8"
@app.route("api/login",methods=["POST"])
def login():
    """登陆接口"""
    # 调试信息，打印请求方法
    print(request.method)
    # 获取请求数据，将数据变为字典
    data = request.get_json()
    # 调试信息，打印请求的数据
    print(data)
    print(type(data))

    # 定义用户名和密码变量，从data中取值
    username = data['username']
    pwd = data['password']
    """
        测试场景设计
        1)  参数为空
        2）用户名密码正确
        3）用户密码错误
    """
    if username == '' or pwd == '':
        # Flask 框架里，可以用 jsonify 返回 json 数据,
        # 使用 jsonify 时，返回的 http response 的 Content-Type是 application/json
        # 这样做是符合 HTTP 协议的规定的，这就是使用 jsonify 的原因之一。
        #起始jsonify调用了jison.dump功能，并且进行了一些增强
        return jsonify({
            "code": "001",
            "msg": "username or password can not be null"
            # "msg": "用户名或密码不允许为空"
        })
    elif username == 'zz' and pwd == '123456':
        return jsonify(
            {
                "adress": {
                    "city": "changsha"
                },
                "httpstatus": 200,
                "info": {
                    "age": 18,
                    "name": "zz"
                },
                "msg": "success",
                "token": "23657DGYUSGD126731638712GE18271H"
            }
        )
    else:
        return jsonify(
            {
                "code": "001",
                "msg": "username or password is wrong"
            }
        )
if __name__ == '__main__':
    # debug=True 开启调试模式
    app.run(debug=True)