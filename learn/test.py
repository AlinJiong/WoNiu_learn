from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://hotel.jd.com/")

driver.execute_script('document.getElementById("dateStart").readOnly=false;')
driver.find_element_by_id("dateStart").send_keys(Keys.BACKSPACE)
driver.find_element_by_id("dateStart").send_keys(Keys.BACKSPACE)
driver.find_element_by_id("dateStart").send_keys(Keys.BACKSPACE)
driver.find_element_by_id("dateStart").send_keys(Keys.BACKSPACE)
driver.find_element_by_id("dateStart").send_keys("2021-05-01")


driver.find_element_by_id("dateEnd").click()
