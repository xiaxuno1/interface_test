# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: shopingApi
# Author: xiaxu
# DATA: 2022/10/10
# Description:购物这一流程的具体实现
# ---------------------------------------------------
import allure
import pytest

from pytest_interface_test_V2.key.api_key import ApiKey
from pytest_interface_test_V2.data.url_conf import *


class ApiCase():
    def login(self,user_data):
        """登陆接口的封装实现"""
        #动态获取标题
        allure.dynamic.title(user_data['title'])
        api= ApiKey()
        url = URL + PORT +'/api/login'
        #print(url)
        #请求的参数，从文件中获取
        userinfo = {
            'username': user_data['user']['username'],
            'password': user_data['user']['password']
        }
        res = api.post(url = url,json = userinfo)
        with allure.step('接口返回信息校验及打印'):
            #print('/api/login登陆请求返回信息')
            #print(res.text)
            msg = api.get_res('msg',res.text)
            assert msg== user_data['msg']

    def getuserinfo(self,token):
        """获取用户信息接口的封装，调用fixture的token实现"""
        api,res,token=token  #获取每个对象的数据
        url = URL +PORT +'/api/getuserinfo'
        headers = {
            'token': token
        }
        res_userinfo = api.get(url = url, headers = headers)
        with allure.step('接口返回信息校验及打印'):
            print('/api/getuserinfo查询个人信息接口的响应结果')
            #print(res_userinfo.text)
            nickname = api.get_res('data',res_userinfo.text)
            assert '风清扬' == nickname[0]['nikename']
        return res_userinfo

    def addcart(self,token):
        """
        添加购物车Request Header:token:23657DGYUSGD126731638712GE18271H
        Request Example:
        {"openid": "UEHUXUXU78272SDSassDD","productid": 8888,"userid": 17890}
        """
        api, res, token_str = token
        with allure.step("调用getuserinfo接口获取userid openid信息"):
            res_userinfo = self.getuserinfo(token)
            print(res_userinfo)
        with allure.step('发送添加购物车请求'):
            url = URL + PORT + '/api/addcart'
            headers = {
                'token': token_str
            }
            data = {
                "openid": api.get_res('data',res_userinfo.text)[0]['openid'], #获取用户信息内的openid
                "productid":8888,
                "userid": api.get_res('data',res_userinfo.text)[0]["userid"]
            }
            res_cart = api.post(url=url,headers = headers,json = data)
        with allure.step("添加购物车接口返回并断言"):
            print("api/addcert添加购物车响应信息")
            print(res_cart)
            print("断言result关键字")
            assert "success" == api.get_res('result',res_cart.text)
        return res_cart

    def createorder(self,token):
        # 从fix中获取预置的工具类和token
        # 所有返回都要获取，不然会报错
        api, res, token_str = token
        with allure.step("调用addcart接口获取返回信息"):
            res_addcart = self.addcart(token)
        with allure.step("发送下单请求"):
            url = URL + PORT + '/api/createorder'
            hd = {
                "token": token_str
            }
            # 从添加商品到购物车接口中，获取userid、openid、cartid
            data = {
                "userid": api.get_res('data',res_addcart.text)[0]['userid'],
                "openid": api.get_res('data',res_addcart.text)[0]['openid'],
                "productid": 8888,
                "cartid": api.get_res('data',res_addcart.text)[0]['cartid']
            }
            # 发送请求
            #print(data)
            res_order = api.post(url=url, headers=hd, json=data)
        with allure.step("接口返回信息打印"):
            print("/api/createorder下单请求响应信息")
            print(res_order)
        with allure.step('断言接口返回result'):
            print('断言result关键字')
            result = api.get_res('result',res_order.text)
            assert 'success' == result

if __name__ == '__main__':
    pytest.main(['-s','test_case05.py'])


