'''
    dubbo尝试封装版：基于通用逻辑，实现更为灵活的调用
'''

import telnetlib


class Dubbo:

    # 构造函数:创建telnet对象是，进行dubbo服务端的连接
    def __init__(self, ip):
        self.con = telnetlib.Telnet()
        self.con.open(ip, 20880)

    # 指令的执行:接口的调用与结果的接收
    def command(self, method):
        # 通过invoke指令调用指定接口
        self.con.write('invoke {}\n'.format(method).encode())
        # 通过read_until接收运行后的返回结果
        data = self.con.read_until('dubbo>'.encode()).decode().split('\r\n')[1]
        return data


# Dubbo服务的接口调用
if __name__ == '__main__':
    dubbo = Dubbo('127.0.0.1')
    result = dubbo.command('com.zhouyu.api.ProviderServiceInterface.getUser()')
    print(result)
