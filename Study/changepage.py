#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import os
from selenium import webdriver
import time

chrome = 'C:\\Users\Administrator.ZX-201703081201\AppData\Local\Google\Chrome\Application\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chrome
driver = webdriver.Chrome(chrome)

driver.get('http://www.baidu.com')

# 获取当前窗口的句柄
currentWin = driver.current_window_handle

# 跳转到另一个新页面
driver.find_element_by_link_text('把百度设为主页').click()
time.sleep(1)
# 获取所有窗口的句柄
handles = driver.window_handles
for i in handles:
    if currentWin == i:
        continue
    else:
        # 将driver与新的页面绑定起来
        driver.switch_to.window(i)
# 在新的页面定位元素
driver.find_element_by_link_text('百度首页').click()
time.sleep(1)
driver.quit()
driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = driver.find_element_by_id('file')
upload.send_keys('E:\\资料\Python_simple\Study\class0.py')  # send_keys
driver.find_element_by_xpath('/html/body/form[1]/input[3]').click()
#print(upload.get_attribute('value'))  # check value
