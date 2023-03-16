# 导入md5加密库
#coding=utf-8

import hashlib

arg = '10月9日开会议定事项.docx'
print(arg)
#MD5 加密的实现形式
se = hashlib.md5(arg.encode('utf-8'))
# 获取变量的内存地址
print(se)
# 获取加密后的密文值
print(se.hexdigest())

# md5加密的封装函数
def hashmd5(string):
    return hashlib.md5(arg.encode('utf-8')).hexdigest()

se2 = hashmd5(arg)
print(se2)