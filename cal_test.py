import unittest
import HTMLTestRunner
#from Calculator import *
from Calculator import Calculator


class CalTestCase(unittest.TestCase):
    """计算器类测试样例"""

    # 程序最开始执行一次
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    # 程序最后执行一次
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # setup准备环境
    def setUp(self):
        print('New a Cal')
        self.cal = Calculator()

    # 结束一个测试样例的动作，清理测试造成的影响（清理内存，打印错误啥的）
    def tearDown(self):
        print('End')

    def test_add(self):
        '''测试计算器加法'''
        result = self.cal.add(3, 5)
        expect = 8
        self.assertEquals(result, expect)

    # @unittest.skip('方法未执行')
    @unittest.skipIf(True, "不执行原因")
    def test_div(self):
        '''测试计算器除法'''
        result = self.cal.div(3, 5)
        expect = 0.6
        self.assertEquals(result, expect)


if __name__ == '__main__':
    # suit = unittest.TestLoader().loadTestsFromTestCase(CalTestCase)
    # file = open('report.html', 'w', encoding='utf-8')
    # runner = HTMLTestRunner.HTMLTestRunner(file, title="测试报告", verbosity=2)
    # runner.run(suit)
    # file.close()

    #自动关闭文件操作
    # suit = unittest.TestLoader().loadTestsFromTestCase(CalTestCase)
    # with open('report.html', 'w', encoding='utf-8') as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(f, title="测试报告", verbosity=2)
    #     runner.run(suit)

    #suit = unittest.defaultTestLoader.discover(路径，方法)
    #控制台打印信息
    unittest.main(verbosity=2)
