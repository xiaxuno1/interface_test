# --------------------------------------------------
# coding=gbk
# !/usr/bin/python
# PN: interface_test
# FN: mock_server
# Author: xiaxu
# DATA: 2022/9/28
# Description:基于flask实现mock_server，其实就是模拟服务器
# ---------------------------------------------------
from flask import Flask
from flask import request,jsonify
import json


app = Flask(__name__)
app.config['JSONIFY_MIMETYPE'] ="application/json;charset=utf-8"
@app.route("/FileUpload/services/UploadFile",methods=["POST","GET"])
def upload():
    """登陆接口"""
    # 调试信息，打印请求方法
    print(request.method)
    #获取内容格式信息
    print(request.headers.get("content-type"))
    # 获取请求数据，将数据变为字典
    data = request.args.to_dict()
    # 调试信息，打印请求的数据
    print(data)
    print(type(data))
    response = {}
    info = [{"filePk":"FILE00002115452"}]


    response["info"]=info
    response["status"] = "false"

    return jsonify(response)


if __name__ == '__main__':
    # debug=True 开启调试模式
    app.run(host="172.16.30.105",port= 9060,debug=True)