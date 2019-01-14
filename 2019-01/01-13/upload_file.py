# encoding: utf-8

'''
 今日练习：selenium 文件上传

         找到文件上传控件（input[type='file']），直接传入文件url（send_keys()）即可

 demo：打开测试环境cnode社区，登录 -> 发帖 -> markdown上传图片

'''

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
