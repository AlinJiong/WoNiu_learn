from selenium import webdriver
import unittest

from selenium.webdriver.support.wait import WebDriverWait
from frame.action.ui_action import UIAction


class WoniuSales(unittest.TestCase):
    '''首页登录模块'''

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.set_page_load_timeout(20)
        cls.driver.implicitly_wait(20)
        cls.driver.get('http://xawn.f3322.net:8060/woniusales')
        cls.action = UIAction(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        '''系统登录测试'''
        user = 'admin'
        password = 'Milor123'
        vcode = '0000'
        self.action.login(user, password, vcode)
        WebDriverWait(self.driver, 20). \
            until(lambda dr:
                  user in dr.find_element_by_css_selector(
                      'div#navbar>ul:nth-child(2)>'
                      'li:first-child>a').text)
        welcome = self.driver.find_element_by_css_selector(
            'div#navbar>ul:nth-child(2)>li:first-child>a')
        self.assertIn(user, welcome.text)
