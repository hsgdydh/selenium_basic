# encoding: utf-8

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://0.0.0.0:5000/')
# driver.get('https://www.baidu.com')
driver.find_element_by_xpath("//a[text()='登录']").click()
# driver.find_element_by_xpath("//input[@name='username']").send_keys('15902127953')
# driver.find_element_by_xpath("//input[@name='password']").send_keys('123456')
# driver.find_element_by_xpath("//button[@type='submit']").click()

import time

# time.sleep(2)
# driver.refresh()
# time.sleep(2)
# num = driver.window_handles
# print(num)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.close()

# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains

# 双击
# driver.find_element_by_xpath("//a[text()='登录']").click()
# username = driver.find_element_by_name('username')
# username.send_keys('123456')
# time.sleep(2)
# ActionChains(driver).double_click(username).perform()

# 移动
# element = driver.find_element_by_xpath("//*[text()='练习一下鼠标移动']")
# time.sleep(2)
# ActionChains(driver).move_to_element(element).perform()

# 拖拽
# driver.find_element_by_xpath("//a[text()='登录']").click()
driver.find_element_by_xpath("//*[text()='练习鼠标拖拽']").click()
time.sleep(2)
element1 = driver.find_element_by_id('dragger')
element2 = driver.find_element_by_xpath("//*[@id='dragger']/../*[text()='Item 2']")
ActionChains(driver).drag_and_drop(element1,element2).perform()

# 拖拽（模拟）：左键单击不放 & 移动到目标元素 & 松开左键
time.sleep(2)
element3 = driver.find_element_by_xpath("//*[@id='dragger']/../*[text()='Item 3']")
ActionChains(driver).click_and_hold(element1).move_to_element(element3).release(element1).perform()

# 查找svg元素
# driver.find_element_by_xpath("//*[name()='svg']")





