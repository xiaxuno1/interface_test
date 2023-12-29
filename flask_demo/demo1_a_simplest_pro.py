# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: demo1_a_simplest_pro
# Author: xiaxu
# DATA: 2023/6/5
# Description:最简单的程序
# ---------------------------------------------------
from flask import Flask
from markupsafe import escape


#实例
app = Flask(__name__)
#路由装饰器
@app.route("/")
def hello_world():
    return "hello,world!"
#url变量
@app.route('/user/<username>')#正常传入url变量
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')#指定url的传入类型
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')#path类型可以/
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')#url尾部是否有/,有没有时添加在后面会报错
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'



if __name__ == '__main__':
    app.run()