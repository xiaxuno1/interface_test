# --------------------------------------------------
#coding=utf-8
# !/usr/bin/python
# PN: interface_test
# FN: test_login
# Author: xiaxu
# DATA: 2022/10/8
# Description:excel驱动数据基本实现，特殊情况（为空）解决方法二
# ---------------------------------------------------
from excel_interface_test.key import api_key
from excel_interface_test.base import excel_op


def run():
    testcases_sheet = excel_op.ExcelOP('test_cases')
    testcases_line = testcases_sheet.get_rows()
    #print(testcases_line)
    num = 0 #行计数器
    api = api_key.ApiKey()
    for line in testcases_line:
        if num ==0:
            num = num+1
            continue
        test_num = line[0]
        url = line[1]+line[2]
        method = line[3] #请求方法，不为空
        headers = line[4] #请求头
        params = line[5] #请求参数,直接将str转换为dict
        params_type = line[6] #参数类型
        assert_param = line[7] #校验字段，不为空
        assert_result = line[8] #预期结果
        test_title = line[11] #测试标题
        req = getattr(api,method)
        print("测试编号：{0}，用例名：{1}".format(test_num,test_title))
        print("反射请求方式：",req)
        """将数据打包传递，否则会出现参数名称无法作为变量传递的情况：
        params_type = params；params_type被认为是关键字
        这里eval(headers)是将其转换为dict;因为headers：要求的是dict
        """
        data = {}
        try:
            data['headers'] = eval(headers)
        except Exception as e:
            print(e)
        try:
            data[params_type]=eval(params)
        except Exception as e:
            print(e)
        if len(data)== 0: #考虑data键值对为空的情况
            res = req(url)
        else:
            print("传递的数据为：", data)
            res = req(url = url,**data)
        #校验结果
        print('响应结果：',res)
        try:
            verify_result = api.get_res(assert_param,res.text)  #如果没有正确响应则会出错，如响应400
            #校验结果写入单元格
            print("响应字段内容：",verify_result)
            testcases_sheet.write_data(num+1,10,verify_result)
            if verify_result == assert_result:
                print("断言通过")
                testcases_sheet.write_result(num+1,11,1)
            else:
                print('断言失败')
                testcases_sheet.write_result(num+1,11,2)
        except Exception as ex:
            testcases_sheet.write_result(num+1,11,5)
            print("测试错误：",ex)

        num = num+1

if __name__ == '__main__':
    run()