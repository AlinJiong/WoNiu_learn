from selenium import webdriver
import unittest

class WoniuSalesTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.set_page_load_timeout(20)
        cls.driver.implicitly_wait(20)
        cls.driver.get("http://xawn.f3322.net:8060/woniusales")
        cls.action = UIAction(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    # def test_login(cls):
