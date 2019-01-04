# encoding: utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BaiDuSearch(unittest.TestCase):
    # 每个用例执行前执行，函数名非自定义
    def setUp(self):
        self.driver = webdriver.Chrome()

    # 自定义用例，函数名必须以 test 开头，后面自定义
    def test_baidu_search(self):
        driver = self.driver
        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('Hello World')
        driver.find_element_by_id('kw').send_keys(Keys.ENTER)

    def test_bing_search(self):
        driver = self.driver
        driver.get('https://cn.bing.com/')
        driver.find_element_by_id('sb_form_q').send_keys('Hello World')
        driver.find_element_by_id('sb_form_go').click()

    # 每个用例执行后执行，函数名非自定义
    def tearDown(self):
        self.driver.quit()

# 执行所有用例
if __name__ == '__main__':
    unittest.main()