# --------------------------------------------------
# -*- coding: utf-8 -*-
# !/usr/bin/python
# PN: interface_test
# FN: ApiKey
# Author: xiaxu
# DATA: 2022/9/30
# Description:封装请求
# ---------------------------------------------------
import jsonpath,json,requests


class ApiKey():
    """封装请求，使用jsonpath处理响应返回list"""
    def get(self,url,params=None,**kwargs):
        return requests.get(url=url,params=params,**kwargs)

    def post(self,url,data = None,**kwargs):
        return requests.post(url=url,data=data,**kwargs)

    def get_res(self,key,data):
        """
        使用jsonpath处理响应的数据，最后返回的是关键字key对应的原始内容
        对于有多层的数据需要进一步处理
        """
        dict_data = json.loads(data) #将数据处理成dict
        key_data = jsonpath.jsonpath(dict_data,'$..{key}'.format(key=key))
        return key_data[0]

if __name__ == '__main__':
     #测试get请求
     url = 'http://39.98.138.157:5000/api/demo'
     params = '1'
     api = ApiKey()
     res = api.get(url=url,params=params)
     res_text = res.text
     print(res.text,type(res.text))
     #测试返回数据
     data = api.get_res('data',res_text)
     print(data)
