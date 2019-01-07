# coding:utf-8

'''

今日练习：使用百度ocr识别图形验证码（有时候不准，仅供参考）

方法步骤：1. 打开【百度AI开放平台官方网站】，依次找到 【产品服务】 -> 【图像技术】-> 【文字识别】 -> 【通用文字识别】，登录自己的百度账号，创建应用，记录应用

API Key  和 Secret Key，根据百度API通用文字识别API文档创建demo如下

'''


import requests, base64, time
from selenium import webdriver

# AK: 1QVlBInHjWeFqzNB3gANNnWk
# SK: UtaL7EkwknACQeeDD0s0G3s7ulvqEf3B

# 打开上海公积金管理中心官方网站
driver = webdriver.Chrome()
driver.get('https://persons.shgjj.com/')

# 找到图形验证码元素并将图片保存到本地
codeImgEle = driver.find_element_by_id('img1')
codeImgEle.screenshot('./codeImg.png')

# 根据百度API通用文字识别API文档自动识别图形验证码
getAccessTokenUrl = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=1QVlBInHjWeFqzNB3gANNnWk&client_secret=UtaL7EkwknACQeeDD0s0G3s7ulvqEf3B'
res = requests.get(getAccessTokenUrl)
if (res.status_code == 200):
    r = res.json()
    access_token = r['access_token']
    getCodeUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token
    # 二进制方式打开图文件
    f = open(r'./codeImg.png', 'rb')

    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}

    result = requests.post(getCodeUrl, data=params)
    if (result.status_code == 200):
        res = result.json()
        code = res['words_result'][0]['words']
        driver.find_element_by_id('imagecode1').send_keys(code)
time.sleep(2)
driver.quit()