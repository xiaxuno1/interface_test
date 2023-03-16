#coding=utf-8
#测试用例
import unittest
from unittest.mock import patch
from mock_ref import function

class MyTestCase(unittest.TestCase):

    #测试用例
    #1.patch()装饰/上下文管理器可以很容易地模拟类或对象在模块测试
    #在测试过程中，指定的对象将被替换为一个模拟（或其他对象），并在测试结束时还原
    #这里模拟function文件中的chen()函数
    @patch("mock_ref.function.chen")
    #2.在定义测试用例中，将mock的chen()函数重命名为mock_chen对象
    def test_add_and_chen(self,mock_chen):
        x = 3
        y = 5
        #设定mock_chen对象的返回值为固定15
        mock_chen.return_value = 15
        addition, mock_chen = function.add_and_multiply(x,y)
        #检查mock_chen方法的参数是否正确
        #mock_chen.assert_called_once_with(3,5)

        self.assertEqual(8,addition)
        self.assertEqual(15,mock_chen)

if __name__ == '__main__':
    unittest.main()