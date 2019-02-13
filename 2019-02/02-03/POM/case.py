# encoding: utf-8

'''



'''


import unittest
from selenium import webdriver
from page import LoginPage

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login(self):
        username = 'user1'
        password = '123456'

        lg = LoginPage(self.driver,username,password)
        lg.login()

        result_username = lg.get_login_name()
        self.assertEqual(result_username,username)

    def tearDown(self):
        pass