# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: conftest
# Author: xiaxu
# DATA: 2022/10/9
# Description:pytest的配置
# ---------------------------------------------------
from pytest_interface_test.key import api_key
import pytest


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

@pytest.fixture(scope='session')
#项目级别的作用域整个项目指挥执行一次，conftest会自动作用于所在目录及其子目录
def token():
    api = api_key.ApiKey()
    url = 'http://39.98.138.157:5000/api/login'
    userinfo = {
        "username": "admin",
        "password": "123456"
    }
    res = api.post(url=url, json=userinfo)
    token = api.get_res('token',res.text)
    return token
