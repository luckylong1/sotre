from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By

#弹框
# driver = webdriver.Chrome()
# driver.get(r"D:/测试项目/PythonProject/day15 【打开网页】/练习的html/练习的html/弹框的验证/dialogs.html")
# driver.find_element_by_id("confirm").click()
# time.sleep(1)
# # driver.switch_to.alert.accept()    点击弹框的确定
# driver.switch_to.alert.dismiss()
# time.sleep(1)


#滑动
# driver = webdriver.Chrome()
# driver.get(r"D:/测试项目/PythonProject/day15 【打开网页】/练习的html/练习的html/滑动验证/mousedrag.html")
# try:
#     a=driver.find_element_by_xpath("/html/body/div/div[3]")
#     # a=driver.find_element(By.XPATH,'/html/body/div/div[3]')
#     ac=ActionChains(driver)
#     ac.click_and_hold(a).move_by_offset(300,0).perform()
#     # ac.drag_and_drop_by_offset(a,248,0).perform()
# except EOFError as err:
#     print("错了，",err)
# else:
#     print("成功解锁")
#
# time.sleep(3)
# driver.quit()

#跳转
# driver = webdriver.Chrome()
# driver.get(r"D:/测试项目/PythonProject/day15 【打开网页】/练习的html/练习的html/跳转页面/pop.html")
# driver.find_element_by_id("goo").click()
# time.sleep(1)
# a =driver.window_handles
# driver.switch_to.window(a[-1])
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys("盖亚！")
# time.sleep(1)
# driver.find_element_by_id("su").click()
# time.sleep(2)
# driver.quit()

#上传文件、下拉框
driver = webdriver.Chrome()
driver.get(r"D:/测试项目/PythonProject/day15 【打开网页】/练习的html/练习的html/上传文件和下拉列表/autotest.html")
try:
    driver.find_element_by_id("accountID").send_keys("user")
    time.sleep(1)
    driver.find_element_by_id("passwordID").send_keys("password")
    time.sleep(1)
    driver.find_element_by_id("areaID").send_keys("北京市")
    time.sleep(1)
    driver.find_element_by_id("sexID1").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr[5]/td/input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr[7]/td/input").send_keys(r"D:/测试项目/建筑材料库房管理系统考核题目/综合考核题目(1).docx")
    time.sleep(1)
    driver.find_element_by_id("buttonID").click()
    driver.switch_to.alert.accept()

except EOFError as err:
    print(err)

else:
    print("成功")
finally:
    print("本次执行结束")

