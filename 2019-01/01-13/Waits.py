# encoding: utf-8

'''
 今日练习：selenium  等待（强制等待、显式等待、隐式等待）

          强制等待：time模块，time.sleep(seconds)，强制等待固定秒数，再继续执行

          显式等待(selenium.webdriver.support.ui.WebDriverWait)：WebDriverWait模块，

          这种方式针对指定元素设置等待，在设定的时间内，WebDriverWait默认情况下每500毫秒调用

          ExpectedCondition一次，直到成功返回。返回值为布尔值。

          隐式等待：webdriver.implicitly_wait(seconds)，这种方式的等待是针对当前脚本中所有dom元素的等待，加入设置等待时间为2s，则所有dom查询后都会等待2s再继续执行

 demo：打开测试环境cnode社区，登录 -> 发帖 -> markdown上传图片

'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# 打开cnode社区首页
driver.get('http://39.107.96.138:3000')

# 登录
driver.find_element_by_css_selector('[href="/signin"]').click()
driver.find_element_by_id('name').send_keys('user1')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_css_selector('input[type="submit"]').click()

# 点击发帖按钮
driver.find_element_by_id('create_topic_btn').click()

# 找到markdown编辑器中的上传图片控件，并上传一张本地图片
driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[1]/a[7]').click()

try:
    element_upload = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.modal.hide.fade.in > div.modal-body > div > div.button.webuploader-container > div:nth-of-type(2) > input[type='file']"))
    )
    element_upload.send_keys('/Users/mac/Desktop/艺术签.gif')
    time.sleep(2)
    element_show = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#create_topic_form > fieldset > div > div > div.editor-toolbar > a.eicon-preview"))
    )
    element_show.click()
    time.sleep(2)
    driver.save_screenshot('./upload.png')

except Exception as e:
    print(e)
finally:
    driver.quit()
