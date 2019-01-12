# encoding: utf-8

# todo 01-12.py简化版

import xlwt

from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://s.weibo.com/')

keyword = 'web自动化'

driver.find_element_by_css_selector('div[class="search-input"] > input[type="text"]').send_keys(keyword)

driver.find_element_by_css_selector('.s-btn-b').click()

driver.find_element_by_link_text('高级搜索').click()

driver.find_element_by_css_selector('label[for="radio03"]').click()

driver.find_element_by_link_text('搜索微博').click()

wb = xlwt.Workbook()

wt = wb.add_sheet(keyword)

wt.write(0, 0, '内容')

wt.write(0, 1, '发送人')

wt.write(0, 2, '发布时间')

wt.write(0, 3, '来源')

wt.write(0, 4, '收藏数')

wt.write(0, 5, '转发数')

wt.write(0, 6, '评论数')

wt.write(0, 7, '点赞数')

couter = 0

#  保存5页的数据

for x in range(5):

    eles = driver.find_elements_by_css_selector('div[action-type="feed_list_item"]')

    for ele in eles:
        couter += 1

        title = ele.find_element_by_css_selector('p[class="txt"]').text

        username = ele.find_element_by_css_selector('a[class="name"]').text

        time = ele.find_element_by_css_selector('p[class="from"]>a:nth-child(1)').text

        source = ele.find_element_by_css_selector('p[class="from"]>a:nth-child(1)').text

        coll = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(1)').text

        coll_num = coll.split('收藏')[1]

        forward = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(2)').text

        forward_num = forward.split('转发')[1]

        comment = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(3)').text

        comment_num = comment.split('评论')[1]

        like = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(4)').text

        # print(title,username,time,coll_num,forward_num,coll_num,like)

        print('counter', couter)

        wt.write(couter, 0, title)

        wt.write(couter, 1, username)

        wt.write(couter, 2, time)

        wt.write(couter, 3, source)

        wt.write(couter, 4, coll_num)

        wt.write(couter, 5, forward_num)

        wt.write(couter, 6, comment_num)

        wt.write(couter, 7, like)

    driver.find_element_by_css_selector('a[action-type="feed_list_page_more"]').click()

    driver.find_element_by_css_selector('ul[class="s-scroll"]>li:nth-child({})'.format(x + 2)).click()

wb.save('weiboList_02.xls')

driver.quit()
