# encoding: utf-8


import unittest
from selenium import webdriver


class LoginPage(object):

    def __init__(self,driver,username,password):
        self.driver = driver
        self.username = username
        self.passwrod = password

    def login(self):
        self.driver.get('http://39.107.96.138:3000/signin');
        self.driver.find_element_by_id('name').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.passwrod)
        self.driver.find_element_by_css_selector('input[type="submit"]').click()

    def get_login_name(self):
        username = self.driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text
        return username
