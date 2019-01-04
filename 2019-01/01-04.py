# encoding: utf-8

'''
今日练习：selenium 查找多个元素，excel表格写入

demo：抓取京东商城手机品牌名称和价格列表并输出在excel表中

'''

from selenium import webdriver
import unittest, xlwt, time

class GetJdPhoneData(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getData(self):
        driver = self.driver
        driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=1.def.0.V13&wq=shouji&pvid=0af689b734e840588aa41683582ed4c2')

        price_eles = driver.find_elements_by_css_selector('ul.gl-warp li.gl-item .p-price')
        desc_eles = driver.find_elements_by_css_selector('ul.gl-warp li.gl-item .p-name.p-name-type-2')

        wb = xlwt.Workbook()
        ws = wb.add_sheet('jd手机')

        ws.write(0, 0, '手机')
        ws.write(0, 1, '价格')

        count = len(desc_eles)
        for index in range(count):
            ws.write(index+1, 0, desc_eles[index].text)  # 疑问： 元素的text属性值不是该元素包含的所有子元素的文本值吗？
            ws.write(index+1, 1, price_eles[index].text)

        wb.save('phone.xls')   # 疑问：保存的文件路径不是当前文件夹下吗？

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()