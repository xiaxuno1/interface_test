# --------------------------------------------------
#coding=gbk
# !/usr/bin/python
# PN: interface_test
# FN: yaml_read
# Author: xiaxu
# DATA: 2022/10/9
# Description:��yaml�ļ��Ķ�ȡ
# ---------------------------------------------------
import yaml


def yaml_load(path):
    """��ȡyaml�ļ�������list"""
    stream = open(path,"r",encoding='gbk')
    yaml_data = yaml.load(stream,Loader=yaml.FullLoader)
    return yaml_data

if __name__ == '__main__':
    user_data = yaml_load('./data.yaml')
    print(type(user_data))
    print(user_data[0])