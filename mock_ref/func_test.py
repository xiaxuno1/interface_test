#coding=utf-8
#测试用例
import unittest
from mock_ref import function

class MyTestCase(unittest.TestCase):

    #测试用例
    def test_add_and_chen(self):
        x = 3
        y = 5
        addition, chenji = function.add_and_multiply(x,y)
        self.assertEqual(8,addition)
        self.assertEqual(15,chenji)

if __name__ == '__main__':
    unittest.main()