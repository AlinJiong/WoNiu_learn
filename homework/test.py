from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_name('wd').send_keys('京东')
driver.find_element_by_id('su').click()
time.sleep(3)
driver.find_element_by_partial_link_text('官网 多快好省 只为品质生活').click()
# driver.get("https://www.jd.com/")
time.sleep(3)
driver.find_element_by_xpath("(//a[@href='//hotel.jd.com/']//span)[2]").click()
time.sleep(3)
