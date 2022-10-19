# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: web_interface_demo1
# Author: xiaxu
# DATA: 2022/9/28
# Description:flask 的web demo
# ---------------------------------------------------
from flask import Flask

app = Flask(__name__)

#只允许get请求
@app.route('/zz/',methods=['get','post'])
def ccc_flask():
    #response
    return 'Hello zz'

if __name__ == '__main__':
    app.run()