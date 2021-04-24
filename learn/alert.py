from selenium import webdriver
import time

driver = webdriver.Chrome()
# 获取alert
# alert = driver.switch_to_alert()

driver.get("https://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("蜗牛学院")
driver.find_element_by_css_selector("#su").click()
time.sleep(3)
driver.find_element_by_link_text("...Java|软件测试|Web前端|网络安全|UI设计培训...").click()

#获取当前窗口
cur_window = driver.current_window_handle

#获取所有窗口
for window in driver.window_handles:
    driver.switch_to_window(window)


driver.switch_to_window(cur_window)
