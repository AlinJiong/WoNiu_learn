from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://xawn.f3322.net:8060/woniusales")


user = driver.find_element_by_id("username")
user.clear()  # 清理输入框
user.send_keys("admin")

pwd = driver.find_element_by_id("password")
pwd.clear()
pwd.send_keys("Milor123")

code = driver.find_element_by_id("verifycode")
code.clear()
code.send_keys("0000")

driver.find_element_by_css_selector("button.form-control.btn-primary").click()

result = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(
"#navbar > ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a"))

print(result.text)
