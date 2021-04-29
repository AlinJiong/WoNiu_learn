from selenium import webdriver
import unittest
from frame.action.ui_action import UIAction


class Sales(unittest.TestCase):
    '''销售出库模块'''

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.set_page_load_timeout(20)
        cls.driver.implicitly_wait(20)
        cls.driver.get('http://xawn.f3322.net:8060/woniusales')
        cls.action = UIAction(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self):
        self.action.login('admin', 'Milor123', '0000')

    def tearDown(self):
        self.action.logout()

    def test_query_product(self):
        '''录入条码查询商品测试'''
        barcode = '11111111'
        self.action.query_product(barcode)
        product = self.driver.find_element_by_css_selector(
            'tbody#goodslist>tr:first-child>td:first-child')
        self.assertEqual(barcode, product.text)
