# encoding: utf-8

import xlrd, xlwt, time
from selenium import webdriver

# 获取本地excel
excel = xlrd.open_workbook('/Users/mac/Desktop/考勤记录/user.xlsx')
# 获取excel的第一个sheet
sheet = excel.sheet_by_index(0)
# 获取sheet中的行数、列数
print(sheet.nrows,sheet.ncols)


driver = webdriver.Chrome()
def login2(userName, userPwd):
    driver.get('http://0.0.0.0:5000/')
    driver.find_element_by_xpath("//a[text()='登录']").click()
    driver.find_element_by_xpath("//input[@name='username']").send_keys(userName)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(userPwd)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    print('第{0}行,用户名{1},密码{2}'.format(i, username, userpwd))
    time.sleep(3)



for i in range(sheet.nrows):
    if (i > 0):
        username = int(sheet.row_values(i)[0])
        userpwd = int(sheet.row_values(i)[1])
        login2(username,userpwd)