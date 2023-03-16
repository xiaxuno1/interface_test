# 导入md5加密库
#coding=utf-8
import hashlib



# md5加密的封装函数
def hashmd5(arg):
    return hashlib.md5(arg.encode('utf-8')).hexdigest()

