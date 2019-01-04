# encoding: utf-8

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')

driver.switch_to_frame('login_frame')
driver.find_element_by_xpath("//input[@name='u']").send_keys('2934478660')