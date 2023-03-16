# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: test_login
# Author: xiaxu
# DATA: 2022/10/8
# Description:excel+Pytest+Allure
# ---------------------------------------------------
import os

from excel_interface_test.key import api_key
from excel_interface_test.base import excel_op,params_handle
import pytest,allure


api = api_key.ApiKey()
testcases_sheet = excel_op.ExcelOP('test_cases')
def excel_testcases():
    testcases_line = testcases_sheet.get_rows()
    #print(testcases_line)
    return testcases_line[1:] #返回的数据将首行排除

@allure.epic("执行excel中定义的测试用例")
@pytest.mark.parametrize('line',excel_testcases())
def test_excel_testcases(line):
    #print(line)
    param = params_handle.ParamsHandle()
    test_num = line[0]
    url = line[1]+line[2]
    method = line[3] #请求方法，不为空
    headers = line[4] #请求头
    params = line[5] #请求参数,直接将str转换为dict
    params_type = line[6] #参数类型
    assert_param = line[7] #校验字段，不为空
    assert_result = line[8] #预期结果
    test_title = line[11] #测试标题
    content_key = line[12] #关联数据
    req = getattr(api,method)
    allure.dynamic.title(test_title)
    #print("反射请求方式：",req)
    """将数据打包传递，否则会出现参数名称无法作为变量传递的情况：
    params_type = params；params_type被认为是关键字
    这里eval(headers)是将其转换为dict;因为headers：要求的是dict
    """
    data = {}
    if headers is not None:
        data['headers'] = param.params_read(eval(headers))
    if params is not None:
        data[params] = param.params_read(eval(params)) #读取param中关联的数据
    if len(data) == 0:  # 考虑data键值对为空的情况
        res = req(url)
    if len(data)== 0: #考虑data键值对为空的情况
        with allure.step("传递接口测试数据"):
            res = req(url)
    else:
        with allure.step("传递接口测试数据"):
            res = req(url = url,**data)
    if content_key is not None:
        param.params_write(eval(content_key),res.text)
    try:
        with allure.step("执行断言"):
            #校验结果
            verify_result = api.get_res(assert_param,res.text)  #如果没有正确响应则会出错，如响应400
            #校验结果写入单元格
            assert verify_result == assert_result
    except Exception as e:
        with allure.step("获取校验结果失败"):
            assert False ,'没有获取到校验字段，请看断言内容'

if __name__ == '__main__':
    #excel_testcases()
    pytest.main(['-s', 'test_excel_pytest_allure.py',
                 '--alluredir', './pytest_results', '--clean-alluredir'])
    os.system('allure generate --clean ./allure_report pytest_results')