
# encoding: utf-8

#  http://39.107.96.138:3000/signup

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

        ActionChains(driver).move_to_element(ele_textarea).send_keys('xxxxxx').perform()

    def tearDown(self):

        self.driver.save_screenshot('./postTopic.png')  # ？：这里的路径是以什么为基准的，./不是当前文件夹下吗？

        # ？？ 没有以下这行代码浏览器也会自动关闭，这行代码是否是必要的？
        self.driver.quit()  # 答：本行代码是为了减少内存消耗，推荐加上


if __name__ == '__main__':
    unittest.main()

