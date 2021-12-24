from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/ul/li[1]/a[1]").click()
time.sleep(1)
a = driver.window_handles
driver.switch_to.window(a[-1])
driver.find_element_by_xpath("/html/body/div[6]/div[2]/ul/li[1]/a/img").click()
time.sleep(1)
b = driver.window_handles
driver.switch_to.window(b[-1])
time.sleep(1)
driver.find_element_by_id("addCart").click()
time.sleep(3)
driver.quit()

