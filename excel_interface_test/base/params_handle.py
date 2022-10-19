# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: params_handle
# Author: xiaxu
# DATA: 2022/10/13
# Description:定义了参数处理的方式
# ---------------------------------------------------
"""
根据设计：处理分为读入数据和写入数据，接收的为字典
    读入数据：以read作为key，传入value为读取字段，如：token、userid;
        读数据的表定义为params,key-value格式，读数据重新组合为参数
        获取数据后，删除read键值对
        将获取的数据添加到原来数据字典返回
    写入数据：
        写数据先要获取数据，即需要将返回的信息筛选出想要的数据保存
        以write作为key，value为读取字段如：token、userid;
        写的表定义为params,key-value格式；
        在excel 的test_cases中关联数据中配置写关联的关键字
"""
from excel_interface_test.base.excel_op import ExcelOP
from excel_interface_test.key.api_key import ApiKey
import allure


class ParamsHandle():

    def __init__(self):
        self.xl = ExcelOP("test_cases")
        self.xl.open_sheet('params') #重写数据表
        self.rows = self.xl.get_rows()
        self.api = ApiKey()

    def params_read(self,params_dict):
        """
        :param params_dict: 参数为一字典
        :return:
        """
        if params_dict.get('read'):
            for read_key in params_dict['read']:#读入数据，传入的是一个可迭代对象
                # 迭代每行的内容，找出关键字对应的内容
                for row in self.rows:
                    if row[0] == read_key:
                        params_dict[read_key] = row[1] #将获取内容添加到参数中
            #最后删除read键值对,返回需要读取的数据
            del params_dict['read']
        return params_dict

    def params_write(self,params_dict,write_content = None):
        """
        写入关联数据
        :param params_dict:
        :param write_content:
        :return:
        """
        if params_dict.get('write'):
            for write_key in params_dict['write']:
                data = self.api.get_res(write_key,write_content)
                line_num = 1 #记录行号
                for row in self.rows:
                    if row[0] == write_key:
                        self.xl.write_data(line_num,2,data)
                        break
                    else:
                        line_num = line_num + 1
                        if len(self.rows)<line_num:#如果到最后都没有，则在新的line添加
                            self.xl.write_data(line_num,1,write_key)
                            self.xl.write_data(line_num, 2, data)
                        continue
