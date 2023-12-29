import unittest

import requests
from pact.consumer import Consumer
from pact.provider import Provider
import atexit

# 定义一个pact，明确消费者与生产者，以及契约文件的存放路径
#这是基于消费驱动模型，即从消费者需求出发，根据消费者需求生成契约文件XXXX.json
#参考 http://t.zoukankan.com/heishao-p-10669623.html
pact_demo = Consumer('consumer').has_pact_with(Provider('provider01'), pact_dir='./pacts')
# 启动服务
pact_demo.start_service()
atexit.register(pact_demo.stop_service)


class CaseDemo(unittest.TestCase):
    # 这是消费端的测试，生产端的测试使用pact-verifier
    # 定义契约文件的内容在消费者端创建一个测试，声明它对提供者的期望
    # 创建一个提供者状态，允许契约在针对提供者重放时通过
    def test_pact(self):
        # 在消费者端创建一个测试，声明它对提供者的期望
        expected = {
            "name": "xuzhu",
        }
        # 消费端定义契约文件中的实际内容，包括请求，请求的参数，头部，响应内容等相关具体细则
        (pact_demo
         .given('test service')
         .upon_receiving('for pact')
         .with_request('post', '/provider')  # 向生产者发送请求时，需要注意的请求方法、路径、参数、头部等
         .will_respond_with(200, body=expected))  # 生产者在被请求之后返回的响应结果，可以自定义状态码，响应头，响应体

        # 基于requests向mock发送请求，验证mock生成的结果是否正确，请求的是pact自带的mock服务，端口1234
        with pact_demo:
            res = requests.post('http://localhost:1234/provider').json()
            print(res)

        # 断言校验，判断自定义的预期结果是否与pact内的预期结果相符合
        self.assertEqual(res, expected)


if __name__ == '__main__':
    cd = CaseDemo()
    cd.test_pact()
