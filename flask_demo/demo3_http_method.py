# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: demo3_http_method
# Author: xiaxu
# DATA: 2023/6/5
# Description:http方法
# ---------------------------------------------------
from flask import request,Flask


app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    return "post method"

def show_the_login_form():
    return "get method"

if __name__ == '__main__':
    app.run()