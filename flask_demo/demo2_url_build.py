# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: demo2_url_build
# Author: xiaxu
# DATA: 2023/6/5
# Description:url构建,static静态文件
# ---------------------------------------------------
from flask import url_for, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run()