from selenium import webdriver
import time

# driver = webdriver.Chrome(
#     executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")

# 将webdriver放入Script下,就不用加路径

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# driver.find_element_by_name("wd").send_keys("蜗牛学院")
# driver.find_element_by_id("su").click()

# inputs = driver.find_elements_by_tag_name("input")
# for i in inputs:
#     if i.get_property("autocomplete") == "off":
#         i.send_keys("蜗牛学院")
#         break
# for i in inputs:
#     if i.get_attribute("type") == "submit":
#         i.click()
#         break

# time.sleep(3)

# driver.find_element_by_link_text("...Java|软件测试|Web前端|网络安全|UI设计培训...").click()
# driver.find_element_by_partial_link_text("软件测试").click()


driver.find_element_by_css_selector("#kw").send_keys("蜗牛学院")
driver.find_element_by_css_selector("#su").click()
