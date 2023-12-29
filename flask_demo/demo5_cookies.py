# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: demo5_cookies
# Author: xiaxu
# DATA: 2023/6/8
# Description:cookie
# ---------------------------------------------------
from flask import make_response, render_template, Flask

app = Flask(__name__)
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp


if __name__ == '__main__':
    app.run(debug = True)