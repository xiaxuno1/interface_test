# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: test_login
# Author: xiaxu
# DATA: 2022/10/8
# Description:测试登陆接口
# ---------------------------------------------------
from unittest_intface_test.key import api_key
import unittest
from ddt import ddt,file_data


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """初始化关键字类"""
        cls.api = api_key.ApiKey()

    @classmethod
    def tearDownClass(cls) -> None:
        """程序结束的操作"""
        pass

    @file_data("../data/user.yaml")
    def test_login(self,user,msg):
        """测试登陆接口功能"""
        url = 'http://39.98.138.157:5000/api/login'
        userinfo = {
            "username": user["username"],
            "password": user["password"]
        }
        #print(userinfo)
        res = self.api.post(url=url,json = userinfo)
        #print(res.text)
        msg_rec = self.api.get_res("msg",res.text)
        #print(msg_rec,msg)
        self.assertEqual(msg,msg_rec,msg = "断言不相等异常")

if __name__ == '__main__':
    unittest.main()