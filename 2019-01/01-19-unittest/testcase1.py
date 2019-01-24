# encoding: utf-8

'''

    本节练习：unittest 官网文档：https://docs.python.org/3.7/library/unittest.html

    1. hooks

        setUpClass()  必须使用类装饰器@classmethod，所有用例执行前执行，仅执行一次
        setUp()       每个用例执行前执行，执行多次
        tearDown()    每个用例执行后执行，执行多次
        tearDownClass()   必须使用类装饰器@classmethod，所有用例执行完毕后执行，仅执行一次
        testcase   自定义用例，例如test_login()

        执行顺序：setUpClass --> setUp --> testcase --> tearDown --> tearDownClass

    2. 自定义用例命名： test 开头，否则unittest框架不识别，不会执行。

    3. 自定义用例执行顺序： 从test后一位开始算起，按照ASCII码的排列顺序依次执行，与函数的定义顺序没有关系，例如 test_login() 会优先于 test_register()执行。

    4. command-line(命令行执行): python3 -m unittest -v xxx.py

                            -v:  输出用例名称
                            -f:  快速失败，在遇到第一个报错或失败用例后停止后面用例的执行
                            -h： 帮助，查看unittest可用参数
                            ...

    5. assert: 每个用例中要添加断言以方便查看用例执行结果

        常见断言如 assertEqual()、assertTrue()、assertFalse()、assertRaises()...


'''

import unittest


class TestCase1(unittest.TestCase):  # todo 继承自unittest.TestCase

    @classmethod
    def setUpClass(cls):
        pass
        # print('setUpClass', '\n')

    def setUp(self):
        pass
        # print('setUp')

    def test01_upper(self):
        print('test01')
        self.assertEqual('foo'.upper(), 'FOO')

    def test02_isupper(self):
        print('test02')
        self.assertTrue('FOO'.isupper(),'当前字符不是大写字符')

    def test03_split(self):
        print('test03')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
        pass
        # print('tearDown')

    @classmethod
    def tearDownClass(cls):
        pass
        # print('tearDownClass', '\n')


print('01', '\n')
print('__name__:', __name__, '\n')
if __name__ == '__main__':
    print('02')
    unittest.main()
