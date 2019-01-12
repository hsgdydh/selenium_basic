# encoding: utf-8

'''
今日练习：selenium 中执行js代码 driver.execute_script()

demo：selenium控制浏览器滚动条滚动至指定位置

'''

import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://news.baidu.com/')

js = "document.querySelector('#local_news > div.column-title-home > div').scrollIntoView(true)"

driver.execute_script(js)

time.sleep(2)

driver.quit()



