# coding: utf-8

import  time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://0.0.0.0:5000')


login = browser.find_element_by_xpath("//a[text()='登录']")
# login.send_keys(Keys.ENTER)
time.sleep(2)

login.send_keys(Keys.CONTROL,'a')

# browser.find_element_by_xpath("//input[@name='username']").send_keys('15902127953')
# browser.find_element_by_xpath("//input[@name='password']").send_keys('123456')
# browser.find_element_by_xpath("//button[@type='submit']").click()


# browser.switch_to.window()



time.sleep(2)

# browser.quit()




