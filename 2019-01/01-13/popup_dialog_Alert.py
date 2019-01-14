# encoding: utf-8

'''
 今日练习：

        一、selenium  处理弹出对话框，包括 提示框：alert()，确认框：confirm()，提示输入框：prompt()

        拿到对话框的方式有两种：

        1. Alert库  selenium.webdriver.common.alert.Alert
        2. webdriver.switch_to_alert() 方法

        对话框操作属性和方法有：

        text   提示文本
        accept()    确定
        dismiss()   取消
        send_keys()   prompt提示输入框中输入内容

        二、selenium 执行js

        driver.execute_script(js_expression)，  参数js_expression是要执行的js代码表达式字符串


 demo：打开测试环境cnode社区，登录 -> 发帖 -> markdown上传图片

'''

import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

def dialog_alert():
    js_expression = "alert('这是alert提示框')"
    driver.execute_script(js_expression)

    time.sleep(2)
    Alert(driver).dismiss()

def dialog_confirm():
    js_expression = "confirm('这是confirm确认框')"
    driver.execute_script(js_expression)

    time.sleep(2)
    print(Alert(driver).text)
    Alert(driver).accept()

def dialog_prompt():
    js_expression = "prompt('请输入你的姓名')"
    driver.execute_script(js_expression)

    time.sleep(1)
    prompt_dialog = driver.switch_to.alert

    time.sleep(1)
    prompt_dialog.send_keys('flying')

    time.sleep(1)
    print(prompt_dialog.text)
    prompt_dialog.accept()

# dialog_alert()
# time.sleep(2)
#
# dialog_confirm()
# time.sleep(2)

dialog_prompt()
time.sleep(2)

driver.quit()


