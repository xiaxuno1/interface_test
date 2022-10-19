# --------------------------------------------------
# -*- coding: utf-8 -*-
# !/usr/bin/python
# PN: interface_test
# FN: tcp_client
# Author: xiaxu
# DATA: 2022/9/29
# Description:创建tcp client
# ---------------------------------------------------
import time,base,base64
from socket import *


tcpclient = socket(AF_INET,SOCK_STREAM)
tcpclient.bind(("0.0.0.0",6060))  #这里指定了client绑定的port
host = '172.16.30.105'
port = 7778
tcpclient.connect((host,port))
while True:
    time.sleep(1)
    #recv_size = tcpclient.recv(1024)
    #print(recv_size)
    #data1 = '01038C03E2035E065F17D713861386138659A65999595B4DB74D754D3F177F17771758094809340958014C0148014E0119011F01250220021B022217DD17C117E8000000000000598900ED022802A700C800FC597A00E30263021F00BB00BC594500BE0276026500B100A3076E005B04' \
    #       'A4000000340067077B0065049A00000039006607A10065049200000037005C88D5'
    #data2 = '02038C000000000000271013861386138658F8591658E94D174CE84CFC177A1760177400030001000100000000000000000000000000000000000027102710271000000000000058E200BD00F600770098011B59140113019A00BF006800F658DC00690100004F0078010B00000000000000000000000000000000000000' \
    #       '00000000000000000000000000000000005EAD'
    #tcpclient.send(bytes.fromhex(data1))
    #tcpclient.send(bytes.fromhex(data2))
    data = 'hello ..你好'
    data1 = '68656C6C6F202E2EE4BDA0E5A5BD'
    print(base64.b16decode(data1)) #解码 Base16 编码的类似字节的对象或 ASCII 字符串。
    tcpclient.send(base64.b16decode(data1)) #编码
    rec = tcpclient.recv(1024)
    print(rec)
    print(rec.decode('utf8'))
    print(base64.b16encode(rec).decode())
