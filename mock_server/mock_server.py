# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: interface_test
# FN: mock_server
# Author: xiaxu
# DATA: 2022/9/28
# Description:����flaskʵ��mock_server����ʵ����ģ�������
# ---------------------------------------------------
from flask import Flask
from flask import request,jsonify


app = Flask(__name__)
app.config['JSONIFY_MIMETYPE'] ="application/json;charset=utf-8"
@app.route("api/login",methods=["POST"])
def login():
    """��½�ӿ�"""
    # ������Ϣ����ӡ���󷽷�
    print(request.method)
    # ��ȡ�������ݣ������ݱ�Ϊ�ֵ�
    data = request.get_json()
    # ������Ϣ����ӡ���������
    print(data)
    print(type(data))

    # �����û����������������data��ȡֵ
    username = data['username']
    pwd = data['password']
    """
        ���Գ������
        1)  ����Ϊ��
        2���û���������ȷ
        3���û��������
    """
    if username == '' or pwd == '':
        # Flask ���������� jsonify ���� json ����,
        # ʹ�� jsonify ʱ�����ص� http response �� Content-Type�� application/json
        # �������Ƿ��� HTTP Э��Ĺ涨�ģ������ʹ�� jsonify ��ԭ��֮һ��
        #��ʼjsonify������jison.dump���ܣ����ҽ�����һЩ��ǿ
        return jsonify({
            "code": "001",
            "msg": "username or password can not be null"
            # "msg": "�û��������벻����Ϊ��"
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
    # debug=True ��������ģʽ
    app.run(debug=True)