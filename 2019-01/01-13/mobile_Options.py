# encoding: utf-8

'''
 今日练习： selenium  开启移动端调试模式

          方式一： Options库  selenium.webdriver.chrome.options.Options
          方式二： webdriver.ChromeOptions()

          官方文档： http://chromedriver.chromium.org/capabilities

'''

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def options_01():

    mobileEmulation = {'deviceName': 'iPhone 6'}

    options = Options()

    options.add_experimental_option('mobileEmulation', mobileEmulation)

    driver = webdriver.Chrome(options=options)

    driver.get('http://m.baidu.com')

    time.sleep(3)

    driver.quit()



def options_02():

    mobileEmulation = {'deviceName': 'iPhone 4'}

    options = webdriver.ChromeOptions()

    options.add_experimental_option('mobileEmulation', mobileEmulation)

    driver = webdriver.Chrome(options=options)

    driver.get('http://m.baidu.com')

    time.sleep(3)

    driver.quit()

options_01()

# options_02()


