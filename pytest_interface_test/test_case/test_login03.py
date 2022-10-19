# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: test_login
# Author: xiaxu
# DATA: 2022/10/8
# Description:使用pytest测试登陆接口登陆接口,通过fixture传递token
# ---------------------------------------------------
from pytest_interface_test.key import api_key
from pytest_interface_test.base import yaml_read
import pytest,allure


def login():
    api = api_key.ApiKey()
    url = 'http://39.98.138.157:5000/api/login'
    userinfo = {
        "username": "admin",
        "password": "123456"
    }
    res = api.post(url=url, json=userinfo)
    token = api.get_res('token',res.text)
    return token
@pytest.fixture(scope='module')
def token():
    return login()


class TestLogin():
    def test_userinfo(self,token):
        self.api = api_key.ApiKey()
        url = 'http://39.98.138.157:5000/api/getuserinfo'
        headers = {
            'token': token
        }
        res = self.api.get(url=url,headers=headers)
        print(res.text)



if __name__ == '__main__':
    pytest.main(['-s','test_login03.py'])