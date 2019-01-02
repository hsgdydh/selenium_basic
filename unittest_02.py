

# encoding: utf-8

import time,unittest, HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException,NoSuchElementException


'''自定义测试类，继承unittest.TestCase'''

class LoginTest001(unittest.TestCase):

    @classmethod
    # 所有test运行前运行一次
    def setUpClass(self):
        self.driver = webdriver.Chrome()

    @classmethod
    # 所有test运行完后运行一次
    def tearDownClass(self):
        self.driver.close()

    def testcase1(self):
            print('用例1，点击左边的按钮，弹出alert，点击接受')
            driver=self.driver
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

if __name__ == '__main__':
    unittest.main()

    '''接入html测试报告'''


    # 第一步，创建一个TestSuite实例
    myLogin = unittest.TestSuite()

    # 第二步，增加测试用例

    '''第一种方法：直接用addtest+方法添加单个。
                传入参数：类名称('用例名称')
                '''
    myLogin.addTest(LoginTest001('testcase2'))

    '''第二种方法：直接用addtests方法添加多个测试用例，而且根据添加是顺序来执行'''

    # testcases.addTests([LoginTest001('testcase2'),LoginTest001('testcase1')])

    '''第三种方法：addtests+TestLoad添加测试类，而不是单个的测试用例
            loadTestsFromTestCase：参数（直接传入类名）
            loadTestsFromName:参数（传入文件模块名.类名）
            loadTestsFromNames:参数：（传入文件模块名.类名的列表）
            '''

    # 例如：
    # testcases.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTest001))

    # testcases.addTests(unittest.TestLoader().loadTestsFromName('login01.LoginTest001'))

    # testcases.addTests(unittest.TestLoader().loadTestsFromNames(['login01.LoginTest01','login01.LoginTest001']))

    # 第三步：HTMLTestRunner来运行所有测试用例
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(now)
    f = open('./test.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='中文1', description='中文2')
    runner.run(myLogin)
    f.close()