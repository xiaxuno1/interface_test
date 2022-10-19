# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: test_login
# Author: xiaxu
# DATA: 2022/10/8
# Description:使用pytest测试登陆接口登陆接口,通过fixture传递token,allure生成测试报告
# ---------------------------------------------------
from pytest_interface_test.key import api_key
from pytest_interface_test.base import yaml_read
import pytest,allure

@allure.epic("用户接口测试")
class TestLogin():
    @allure.story("测试登陆接口")
    @pytest.mark.parametrize("user_data",yaml_read.yaml_load('d:/interface_test/pytest_interface_test/data/user.yaml'),
                             ids = ['用户名错误，密码正确','用户名正确，密码错误','用户名正确，密码为空','用户名正确，密码正确'])
    def test_login(self,user_data):
        self.api = api_key.ApiKey()
        """测试登陆接口功能"""
        url = 'http://39.98.138.157:5000/api/login'
        userinfo = {
            "username": user_data["user"]["username"],
            "password": user_data["user"]["password"]
        }
        #print(userinfo)
        with allure.step('校验响应结果：'):
            res = self.api.post(url=url,json = userinfo)
            #print(res.text)
            msg_rec = self.api.get_res("msg",res.text)
            #print(msg_rec)
            assert msg_rec == user_data["msg"]

    @allure.story('用户信息接口测试')
    def test_userinfo(self,token):
        self.api = api_key.ApiKey()
        url = 'http://39.98.138.157:5000/api/getuserinfo'
        headers = {
            'token': token
        }
        res = self.api.get(url=url,headers=headers)
        with allure.step('返回结果校验'):
            data = self.api.get_res('data',res.text)
            #print(data[0]['nikename'])
            #nikename = data[]
            assert data[0]['nikename'] == '风清扬'



if __name__ == '__main__':
    pytest.main(['-s','test_login04.py'])