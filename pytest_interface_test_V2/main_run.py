# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: main_run
# Author: xiaxu
# DATA: 2022/10/9
# Description:运行allure
# ---------------------------------------------------
import os,pytest


def run():
    #::TestAPI::test_createorder
    pytest.main(['-s','./test_case/test_login05.py','--alluredir','./allure_result','--clean-alluredir'])
    #os.system('allure serve allure_result') #生成serve
    os.system('allure generate --clean ./allure_result')

if __name__ == '__main__':
    run()