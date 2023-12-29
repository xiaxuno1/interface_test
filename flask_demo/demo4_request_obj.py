# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: demo4_request_obj
# Author: xiaxu
# DATA: 2023/6/6
# Description:请求对象 文件上传
# ---------------------------------------------------
from flask import request, Flask, render_template

app = Flask(__name__)
@app.route('/',methods = ['POST'])
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/login",methods = ['POST'])
def login():
    error = None
    if request.method == 'POST':
        if vaild_login(request.args['username'],request.args['passwd']): #有效性稽核
            return login_the_user_in(request.args['username'])
        else:
            error = 'Invaild username/passwd'
    return render_template('login.html',error =error)

def vaild_login(username,passwd):#验证
    return True

def login_the_user_in(username):
    return 'welcome %username'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file_upload.txt']
        f.save('/var/www/uploads/uploaded_file.txt')


if __name__ == '__main__':
    app.run(debug=True)