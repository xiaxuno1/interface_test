# --------------------------------------------------
# coding=gbk
# !/usr/bin/python
# PN: interface_test
# FN: mock_server
# Author: xiaxu
# DATA: 2022/9/28
# Description:����flaskʵ��mock_server����ʵ����ģ�������
# ---------------------------------------------------
from flask import Flask
from flask import request,jsonify
import json


app = Flask(__name__)
app.config['JSONIFY_MIMETYPE'] ="application/json;charset=utf-8"
@app.route("/FileUpload/services/UploadFile",methods=["POST","GET"])
def upload():
    """��½�ӿ�"""
    # ������Ϣ����ӡ���󷽷�
    print(request.method)
    #��ȡ���ݸ�ʽ��Ϣ
    print(request.headers.get("content-type"))
    # ��ȡ�������ݣ������ݱ�Ϊ�ֵ�
    data = request.args.to_dict()
    # ������Ϣ����ӡ���������
    print(data)
    print(type(data))
    response = {}
    info = [{"filePk":"FILE00002115452"}]


    response["info"]=info
    response["status"] = "false"

    return jsonify(response)


if __name__ == '__main__':
    # debug=True ��������ģʽ
    app.run(host="172.16.30.105",port= 9060,debug=True)