# encoding: utf-8

'''

    本节练习：测试报告生成 HTMLReport库


'''

import unittest, sys, selenium, HTMLReport

from test01.testcase1 import TestCase1


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

def suite3():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    loader2 = unittest.TestLoader().loadTestsFromTestCase(TestCase3)
    suite.addTests(loader)
    suite.addTests(loader2)
    return suite

if __name__ == '__main__':
    suite = suite3()
    runner = HTMLReport.TestRunner(report_file_name='report_test01',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                   output_path='report',  # 保存文件夹名，默认“report”
                                   title='测试报告',  # 报告标题，默认“测试报告”
                                   description='无测试描述',  # 报告描述，默认“测试描述”
                                   thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                   thread_start_wait=0,  # 各线程启动延迟，默认 0 s
                                   sequential_execution=False,  # 是否按照套件添加(addTests)顺序执行，
                                   # 会等待一个addTests执行完成，再执行下一个，默认 False
                                   # 如果用例中存在 tearDownClass ，建议设置为True，
                                   # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                   # lang='en'
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
    runner.run(suite)
