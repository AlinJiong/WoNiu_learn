from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import unittest
import time
import HTMLTestRunner


class WoniuSalesLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get("http://xawn.f3322.net:8060/woniusales")

    def test_login(self):
        user = self.driver.find_element_by_id("username")
        user.clear()  # 清理输入框
        user.send_keys("admin")

        pwd = self.driver.find_element_by_id("password")
        pwd.clear()
        pwd.send_keys("Milor123")

        code = self.driver.find_element_by_id("verifycode")
        code.clear()
        code.send_keys("0000")

        self.driver.find_element_by_css_selector(
            "button.form-control.btn-primary").click()

        # welcome = self.driver.find_element_by_css_selector(
        #     "#navbar > ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a")

        # print(welcome.text)

        # try:
        #     result = WebDriverWait(self.driver, 10).until(lambda driver: 'admin' in driver.find_element_by_css_selector(
        #         "#navbar > ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a").text)
        #     self.assertTrue(result)
        # except TimeoutException:
        #     self.assertTrue(False)

        # result = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_css_selector(
        # "#navbar > ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a"))
        # self.assertIn("admin", result.text)

        el = self.driver.find_element_by_id("paymethod")
        # obj = Select(el)        
        # obj.select_by_index(1)
        # time.sleep(3)
        # obj.select_by_index(2)

        print(type(el))
        print(el.get_attribute('value'))
        time.sleep(1)

    def TearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(WoniuSalesLoginTest)
    with open("report.html", "w", encoding="utf-8") as f:
        runner = HTMLTestRunner.HTMLTestRunner(f, title="woniu", verbosity=2)
        runner.run(suite)
