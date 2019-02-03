# encoding: utf-8

'''

    本节练习：日志输出 python-logging  https://docs.python.org/3.7/library/logging.html

    常见的logging等级：

        CRITICAL	50
        ERROR	40
        WARNING	30
        INFO	20
        DEBUG	10
        NOTSET	0

    logging库使用方式：

    1.定义日志打印内容及格式

    FORMAT = '%(message)s %(asctime)-10s %(clientip)-10s %(user)s %(action)-10s'

    %s表示字符串匹配，括号中的参数如action可以自定义，-10s表示该项匹配的字符串后添加多少空字符

    2.设置logging基础配置

    logging.basicConfig(format=FORMAT,filename='report/logReport.log',level=logging.INFO)

    参数介绍：

        format      日志格式

        filname     日志输出文件

        level      logging输出的最低等级，只有大于等于设置等级才会被打印出来，
                例如此处level最低等级为INFO，则小于INFO等级的DEBUG级别的就不会被打印出来

    3.调用
    d = {'clientip': '192.168.0.103', 'user': 'flying','action':'test01_upper'}
    logging.debug('log_test_debug', extra=d)


'''

import unittest,logging

FORMAT = '%(message)s %(asctime)-10s %(clientip)-10s %(user)s %(action)-10s'
logging.basicConfig(format=FORMAT,filename='report/logReport.log',level=logging.INFO)
# logger = logging.getLogger('tcpserver')


class TestCase1(unittest.TestCase):


    def test01_upper(self):

        d = {'clientip': '192.168.0.103', 'user': 'flying','action':'test01_upper'}
        logging.debug('log_test_debug', extra=d)
        self.assertEqual('foo'.upper(), 'FOO')

    def test02_isupper(self):
        d = {'clientip': '192.168.0.103', 'user': 'flying', 'action': 'test02_isupper'}
        logging.info('log_test_info', extra=d)
        self.assertTrue('FOO'.isupper(),'当前字符不是大写字符')

    def test03_split(self):
        d = {'clientip': '192.168.0.103', 'user': 'flying', 'action': 'test03_split'}
        logging.warning('log_test_warning', extra=d)
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':

    unittest.main()
