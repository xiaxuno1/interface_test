# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: test_login
# Author: xiaxu
# DATA: 2022/10/8
# Description:使用pytest测试登陆接口登陆接口,通过fixture传递token,allure生成测试报告
# ---------------------------------------------------
from pytest_interface_test_V2.key import api_key
from pytest_interface_test_V2.base import yaml_read
from pytest_interface_test_V2.test_logic import shopingApi
import pytest,allure

@allure.epic("用户接口测试")
class TestAPI():
    api_case = shopingApi.ApiCase()
    @allure.feature("测试登陆接口")
    @pytest.mark.parametrize("user_data",yaml_read.yaml_load('d:/interface_test/pytest_interface_test_V2/data/user.yaml'),
                             ids = ['用户名错误，密码正确','用户名正确，密码错误','用户名正确，密码为空','用户名正确，密码正确'])
    @allure.story("一般场景story")
    @allure.title("测试登陆场景title")
    def test_login(self,user_data):
        self.api_case.login(user_data)

    @allure.feature("测试个人信息接口")
    @allure.story("典型场景")
    def test_userinfo(self,token):
        self.api_case.getuserinfo(token=token)

    @allure.feature("测试添加购物车接口")
    @allure.title("测试添加id 8888至购物车接口")
    def test_addcert(self,token):
        self.api_case.addcart(token)

    @allure.feature("测试提交订单接口")
    def test_createorder(self,token):
        self.api_case.createorder(token)


if __name__ == '__main__':
    pytest.main(['-s','test_login05.py'])