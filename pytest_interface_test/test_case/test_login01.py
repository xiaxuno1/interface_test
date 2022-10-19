# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: test_login
# Author: xiaxu
# DATA: 2022/10/8
# Description:使用pytest测试登陆接口登陆接口,直接在程序中输入数据登陆
# ---------------------------------------------------
from pytest_interface_test.key import api_key
import pytest,allure


class TestLogin():
    def test_login(self):
        self.api = api_key.ApiKey()
        """测试登陆接口功能"""
        url = 'http://39.98.138.157:5000/api/login'
        userinfo = {
            "username":'admin',
            "password": '123456'
        }
        #print(userinfo)
        res = self.api.post(url=url,json = userinfo)
        #print(res.text)
        msg_rec = self.api.get_res("msg",res.text)
        #print(msg_rec,msg)
        assert msg_rec == 'success'

if __name__ == '__main__':
    pytest.main(['-s','test_login01.py'])