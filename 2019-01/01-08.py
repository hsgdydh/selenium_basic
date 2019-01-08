# encoding: utf-8

'''
今日练习：selenium ActionChains + Keys 组合快捷键使用

demo：使用selenium ActionChains + Keys 实现 Ctrl + B 加粗

'''

import unittest, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Cnode(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://39.107.96.138:3000'
        self.driver.get(self.url);
        self.driver.find_element_by_css_selector('[href="/signin"]').click()
        self.driver.find_element_by_id('name').send_keys('user1')
        self.driver.find_element_by_id('pass').send_keys('123456')
        self.driver.find_element_by_css_selector('input[type="submit"]').click()
        self.driver.find_element_by_id('create_topic_btn').click()

    def test_post_topic(self):
        driver = self.driver
        driver.find_element_by_id('tab-value').click()

        driver.find_element_by_css_selector('option[value="share"]').click()

        driver.find_element_by_id('title').send_keys('哈哈哈')

        ele_textarea = driver.find_element_by_class_name('CodeMirror-scroll')
        ele_textarea.click()

        # ActionChains + Keys 实现 Ctrl + B 加粗
        ActionChains(driver).move_to_element(ele_textarea).send_keys(Keys.COMMAND, 'b').send_keys('哈哈哈').perform()
        time.sleep(2)

    def tearDown(self):

        self.driver.save_screenshot('./组合快捷键使用.png')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()