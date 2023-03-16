#导入mock模块
#coding=utf-8
from unittest import mock
import unittest

from mock_base.modular import Count

# 编写计算类的测试用例（功能未开发完成）
class TestCount(unittest.TestCase):
    #定义测试用例
    def test_add(self):
        #1.调用被测试类
        count = Count()
        #2.通过Mock类模拟被调用的add()方法，return_value定义add()方法的返回值
        count.add = mock.Mock(return_value=13)
        # 用例步骤
        result = count.add(8,5)
        # 预期结果
        self.assertEqual(result,13)

if __name__ == '__main__':
    unittest.main()
