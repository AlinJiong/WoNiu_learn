import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
# driver.get("https://hotel.jd.com/")

driver.get("https://www.jd.com/")
time.sleep(1)
driver.find_element_by_xpath("(//a[@href='//hotel.jd.com/']//span)[2]").click()

# 保留当前页面
cur_window = driver.current_window_handle

for window in driver.window_handles:
    driver.switch_to_window(window)

time.sleep(1)
driver.maximize_window()
# 关闭广告
driver.find_element_by_class_name("close").click()
driver.find_element_by_id("city").click()
driver.find_element_by_xpath("//a[@quan='chengdu']").click()
# 下拉整个页面
driver.find_element_by_id("city").send_keys(Keys.DOWN)


# 下拉整个页面
driver.find_element_by_id("dateStart").click()
driver.find_element_by_xpath("//div[text()='25']").click()
driver.find_element_by_id("dateStart").send_keys(Keys.DOWN)
time.sleep(1)
driver.find_element_by_id("dateEnd").click()
time.sleep(1)
driver.find_element_by_xpath("(//div[text()='26'])[3]").click()
time.sleep(1)


driver.find_element_by_id("hotelKeys").click()
driver.find_element_by_id("hotelKeys").send_keys("春熙路/太古里商业区")
time.sleep(1)
# 输入回车键
driver.find_element_by_id("hotelKeys").send_keys(u'\ue007')

driver.find_element_by_css_selector("#searchBtn").click()

names = driver.find_elements_by_class_name("p-name")
prices = driver.find_elements_by_class_name("p-price")

re1 = []
re2 = []
for name in names:
    re1.append(name.text)

for price in prices:
    re2.append(price.text)

for i in range(len(re1)):
    print(re1[i], end=' ')
    print(re2[i])

time.sleep(3)
