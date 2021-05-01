import unittest
import HTMLTestRunner
from lesson import *


class CalTestCase(unittest.TestCase):

    def test_1(self):
        s1 = Student("张三", 12, '男', '计算机', 1)
        t1 = Teacher("李六", 42, '男', '计算机', '通信工程')
        res = s1.study(t1, "自动化")
        expect = "我是张三,老师,今天学习了自动化，我终于学会了!"
        self.assertEquals(res, expect)

    def test_2(self):
        s1 = Student("张三", 12, '男', '计算机', 1)
        t1 = Teacher("李六", 42, '男', '计算机', '通信工程')
        res = s1.study(t1, "集成开发")
        expect = "我是张三,老师,今天学习了集成开发，我终于学会了!"
        self.assertEquals(res, expect)


if __name__ == '__main__':
    suit = unittest.TestLoader().loadTestsFromTestCase(CalTestCase)
    file = open('report.html', 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(file, title="测试报告", verbosity=2)
    runner.run(suit)
    file.close()
