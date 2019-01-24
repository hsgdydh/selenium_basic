# encoding: utf-8

'''
    本节练习：unittest

    关于 if __name__ == '__main__':
             unittest.main()


    python文件（.py文件）有2种使用方法：1. 作为脚本直接执行；2. 被其他脚本import，实现模块重用。

    每个python文件都包含一个内置变量__name__，当该文件作为脚本被直接执行，__name__指向__main__；
    当该文件作为模块被载入，则该文件中的__name__指向模块名（不包含后缀 .py），而__main__始终指向当前执行文件的名称（包含后缀 .py）
    只有python文件直接作为脚本执行__name__才等于__main__，所有直接执行会执行if __name__ == '__main__':后的代码块，import进来的不执行。


    因此，直接执行testcase1脚本文件，会打印出 '01'， '__name__: __main__ ' 和 '02'；而testcase2中载入testcase1脚本，if __name__ == '__main__': 后
    的代码块不执行，只会打印出'01' 和 '__name__: __main__ '


    注意：使用pycharm运行脚本时，要留意是否运行的当前测试类所在脚本，而不是Unittests in xxx.py，pycharm默认运行的是Unittests类的单元，忽略了if __name__ == '__main__':的执行，也就没有执行整个xxx.py文件
    详情见pycharm_unittest.jpg


'''

import unittest,testcase1

