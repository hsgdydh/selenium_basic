# encoding: utf-8

'''

    本节练习：unittest 官网文档：https://docs.python.org/3.7/library/unittest.html

    一、 skip  用例跳过,  使用@unittest.skip()...装饰器，实现条件性跳过

        @unittest.skip(reason)   强制跳过，reason为跳过原因
        @unittest.skipIf(condition,reason)     condition为True时跳过
        @unittest.skipUnless(condition,reason)   condition为False时跳过
        @unittest.expectedFailure    如果test失败了，这个test不计入失败的case数目


    二、 用例的批量执行，3种方式

    1. discover命令

    discover   批量执行指定目录下匹配的指定脚本下的所有以test开头的自定义用例（默认加载test开头的模块）

        使用方法1-命令行执行：python3 -m unittest discover -v -s 'start-directory' -p 'test*.py'
        参数：-v   详细输出
             -s   启动目录，默认为当前目录
             -p   匹配加载的测试文件(默认匹配test*.py)
             -t   顶层目录（默认同-s，一般默认即可）

    2. 普通方法将单个用例逐个添加至测试套件中，统一执行

        创建测试套件：suite = unittest.TestSuite()
        添加单个用例至套件中： suite.addTest(case)  单个逐个添加
                            suite.addTests([case1,case2...])  多个逐个添加

    3. TestLoader().discover()将单个用例集合至测试套件中，再统一执行

        创建测试套件：suite = unittest.TestSuite()
        利用discover()集合单个用例统一添加至套件中： loader = unittest.TestLoader().discover(start_dir, pattern ='test *.py', top_level_dir = None )
                                                suite.addTests(loader)

    三、执行套件中的用例  TextTestRunner

        suite = unittest.TestSuite()
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)

        注：1.其中的run(test)会执行TestSuite/TestCase中的run(result)方法。
        测试的结果保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息
           2. 关于verbosity参数
              0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
              1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
              2 (详细模式):测试结果会显示每个测试用例的所有相关的信息


    疑惑：unittest.main()的作用？


'''

import unittest, sys, selenium

from test01.testcase1 import TestCase1

print(selenium.__version__.split('.'))


class TestCase3(unittest.TestCase):

    # 若断言成功，测试结果为expected success；如果断言失败，测试结果为expected failure，但不计入失败（FAIL）中
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(0, 1, 'broken')

    # 强制跳过
    @unittest.skip('demonstrating skipping')
    def test_nothing(self):
        self.fail('shouldn not happen')

    # 不跳过，条件语句为True时跳过
    @unittest.skipIf(int(selenium.__version__.split('.')[0]) < 3, 'not support in this library version')
    def test_format(self):
        pass

    # 跳过，条件语句为False时跳过
    @unittest.skipUnless(sys.platform.startswith('win'), 'require Windows')
    def test_windows_support(self):
        pass

    # 成功的用例
    def test01_upper(self):
        print('脚本3-test01')
        self.assertEqual('foo'.upper(), 'FOO')

    # 失败的用例
    def test02_isupper(self):
        self.assertTrue('fOO'.isupper(), '当前字符不是大写字符')

    def test03_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])


# todo TestSuite()测试套件
def suite():
    suite = unittest.TestSuite()
    suite.addTests([TestCase1('test01_upper'), TestCase3('test01_upper')])
    return suite


def suite2():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader().discover('test01', pattern='test*.py')
    suite.addTests(loader)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite2())
    print(result)   # <unittest.runner.TextTestResult run=3 errors=0 failures=0>
