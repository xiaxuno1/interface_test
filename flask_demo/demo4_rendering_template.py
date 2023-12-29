# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: demo3_rendering_template
# Author: xiaxu
# DATA: 2023/6/5
# Description:渲染模板
# ---------------------------------------------------
from flask import render_template, Flask


app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()