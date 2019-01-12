# encoding: utf-8

'''
今日练习：selenium 爬虫 + excel表格操作（读写、修改）

demo：搜集web自动化原创微博(前5页)的 发送人，标题，发布时间，来源，收藏数，转发数，评论数，点赞数写入excel表格

'''

import time, xlrd, xlwt
from selenium import webdriver
from xlutils.copy import copy

driver = webdriver.Chrome()

driver.get('https://s.weibo.com/')


def append_data(init_row, sheet, data_list):
    count = init_row
    for ele in data_list:
        count += 1
        userName = ele.find_element_by_css_selector('a.name').text
        title = ele.find_element_by_css_selector('p.txt').text
        time = ele.find_element_by_css_selector('p.from > a:nth-of-type(1)').text
        source = ele.find_element_by_css_selector('p.from > a:nth-of-type(2)').text
        collect = ele.find_element_by_css_selector('div.card-act ul li:nth-of-type(1)').text.split('收藏')[1] or 0
        share = ele.find_element_by_css_selector('div.card-act ul li:nth-of-type(2)').text.split('转发')[1] or 0
        comment = ele.find_element_by_css_selector('div.card-act ul li:nth-of-type(3)').text.split('评论')[1] or 0
        like = ele.find_element_by_css_selector('div.card-act ul li:nth-of-type(4)').text or 0

        sheet.write(count, 0, title)
        sheet.write(count, 1, userName)
        sheet.write(count, 2, time)
        sheet.write(count, 3, source)
        sheet.write(count, 4, collect)
        sheet.write(count, 5, share)
        sheet.write(count, 6, comment)
        sheet.write(count, 7, like)


def create_excel():
    driver.find_element_by_xpath('//*[@id="pl_homepage_search"]/div/div[2]/div/input').send_keys('web自动化')
    driver.find_element_by_xpath('//*[@id="pl_homepage_search"]/div/div[2]/button').click()
    ele_search_high = driver.find_element_by_xpath('//*[@id="pl_feedtop_top"]/div[3]/a')
    if (ele_search_high.is_displayed()):
        ele_search_high.click()
        driver.find_element_by_xpath('//*[@id="radio03"]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[2]/a[1]').click()

        # 建表
        excel = xlwt.Workbook()
        sheet1 = excel.add_sheet('web自动化原创微博基本信息收集')
        sheet1.write(0, 0, '标题')
        sheet1.write(0, 1, '发送人')
        sheet1.write(0, 2, '发布时间')
        sheet1.write(0, 3, '来源')
        sheet1.write(0, 4, '收藏数')
        sheet1.write(0, 5, '转发数')
        sheet1.write(0, 6, '评论数')
        sheet1.write(0, 7, '点赞数')

        # 写入微博第1页列表数据
        list = driver.find_elements_by_css_selector("#pl_feedlist_index div[action-type='feed_list_item']")
        append_data(0, sheet1, list)

        # 保存第1页数据
        excel.save('./weboList.xls')

        # 切换页并将数据追加到已经建好的数据表格中
        eles_page_list = driver.find_elements_by_css_selector('#pl_feedlist_index > div.m-page > div > span > ul > li')
        for i in range(len(eles_page_list)):
            if (i < 4):
                switch_page(i + 2)


def switch_page(pageNum):
    driver.find_element_by_xpath('//*[@id="pl_feedlist_index"]/div[3]/div/span/a').click()

    ele_page = '#pl_feedlist_index > div.m-page > div > span > ul > li:nth-of-type({})'.format(pageNum)

    # 切换到指定页
    driver.find_element_by_css_selector(ele_page).click()

    # 复制已经建好的表将新数据写入再重新保存
    excel = xlrd.open_workbook('./weboList.xls')
    sheet = excel.sheet_by_name('web自动化原创微博基本信息收集')
    rows_old = sheet.nrows
    excel_new = copy(excel)
    sheet_new = excel_new.get_sheet(0)
    list = driver.find_elements_by_css_selector("#pl_feedlist_index div[action-type='feed_list_item']")
    append_data(rows_old - 1, sheet_new, list)
    excel_new.save('./weboList.xls')
    if (pageNum == 5):
        driver.quit()


create_excel()
