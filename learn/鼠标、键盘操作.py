from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("http://www.woniuxy.com/")
driver.maximize_window()
el = driver.find_element_by_css_selector(
    '#banner > div.head_left_list > ul > li:nth-child(1) > a')

# 进行鼠标悬停操作，需要注意perfrom方法，所有的鼠标操作只有在调用了它之后才会生效
# 鼠标操作有单击、双击、右键、拖拽等操作
webdriver.ActionChains(driver).click_and_hold(el).perform()


# send_keys模拟键盘操作
driver.find_element_by_id("condition").send_keys(Keys.ENTER)


# 下拉选择框操作，先定位元素
el = driver.find_element_by_id("paythod")
# 构造select对象Select(el)
Select(el).select_by_index(2)
# 三种选择方式
# select_by_index(index)
# select_by_value(value)
# select_by_visible_text(text)


# 窗口操作
driver.maximize_window()
driver.minimize_window()
driver.set_window_size(200, 150)

# 前进、回退、刷新、
driver.forward()
driver.back()
driver.refresh()

# 时间等待
# 强制等待
time.sleep(5)
# 隐式等待
driver.implicitly_wait(5)
# 显示等待
WebDriverWait(driver, 20).until(expected_conditions.
                                presence_of_element_located((By.ID, "submit"))).click()

WebDriverWait(driver, 20).until(
    lambda driver: driver.find_element_by_id("submit").click())


# 利用js操作，解除网页限制
driver.execute_script('document.getElementById("id").readOnly=false;')
