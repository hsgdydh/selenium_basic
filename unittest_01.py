# encoding: utf-8

import time
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException,NoSuchElementException


class Testcase1():
    '''写一个测试类，未继承unittest'''
    def testcase1(self):
            print('用例1，点击左边的按钮，弹出alert，点击接受')
            driver=webdriver.Chrome()
            driver.get('http://127.0.0.1:5000/')
            try:
                driver.find_element_by_xpath('//*[@id="testid"]').click()
            except NoSuchElementException as e:
                print(e)
            time.sleep(2)
            text=driver.switch_to.alert.text
            print(text)
            driver.switch_to.alert.accept()
    def testcase2(self):
        print('用例2，点击登录网站进入练习页面')
        username='15902127953'
        driver=webdriver.Chrome()
        driver.get('http://127.0.0.1:5000/')
        driver.find_element_by_xpath('/html/body/a').click()
        driver.find_element_by_xpath('/html/body/form/p[1]/input').send_keys(username)
        driver.find_element_by_xpath('/html/body/form/p[2]/input').send_keys('123456')
        driver.find_element_by_xpath('/html/body/form/p[3]/button').click()
        print('case2')

Testcase1().testcase1()
Testcase1().testcase2()