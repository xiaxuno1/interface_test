# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: test_login
# Author: xiaxu
# DATA: 2022/10/8
# Description:使用pytest测试登陆接口登陆接口,使用pytest的参数化配置数据
# ---------------------------------------------------
from pytest_interface_test.key import api_key
from pytest_interface_test.base import yaml_read
import pytest,allure


class TestLogin():
    @pytest.mark.parametrize("user_data",yaml_read.yaml_load('../data/user.yaml'))
    def test_login(self,user_data):
        self.api = api_key.ApiKey()
        """测试登陆接口功能"""
        url = 'http://39.98.138.157:5000/api/login'
        userinfo = {
            "username": user_data["user"]["username"],
            "password": user_data["user"]["password"]
        }
        #print(userinfo)
        res = self.api.post(url=url,json = userinfo)
        #print(res.text)
        msg_rec = self.api.get_res("msg",res.text)
        #print(msg_rec,msg)
        assert msg_rec == user_data["msg"]

if __name__ == '__main__':
    pytest.main(['-s','test_login02.py'])