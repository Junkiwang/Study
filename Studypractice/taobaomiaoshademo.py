#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
# python3.6.5
# coding:utf-8

'''
@time:2019-02-16 16:50
@原作者author: 李铭
@2019-11-08 10:35
@改写：saul
程序利用自动测试工具模拟用户下单操作，完成商品的抢购
仅作为学习过程中的实践，无商业用途
'''

from selenium import webdriver
import datetime
import time


def login(url, mall):
    '''
    登陆函数

    url:商品的链接
    mall：商城类别
    '''
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)
    # 淘宝和天猫的登陆链接文字不同
    if mall == '1':
        # 找到并点击淘宝的登陆按钮
        driver.find_element_by_link_text("亲，请登录").click()
    else:
        # 找到并点击天猫的登陆按钮
        driver.find_element_by_link_text("请登录").click()
    print("请在15秒内完成登录!")
    # 用户扫码登陆
    time.sleep(15)


def buy(buy_time, mall):
    '''
    购买函数

    buy_time:购买时间
    mall:商城类别

    获取页面元素的方法有很多，获取得快速准确又是程序的关键
    在写代码的时候运行测试了很多次，css_selector的方式表现最佳
    '''
    if mall == '1':
        # "立即购买"的css_selector
        btn_buy = '#J_juValid > div.tb-btn-buy > a'
        # "立即下单"的css_selector
        btn_order = '#submitOrderPC_1 > div.wrapper > a'
        # 提交订单按钮有变化,增加了'PC'
    else:
        btn_buy = '#J_LinkBuy'
        btn_order = '#submitOrderPC_1 > div > a'
        # 提交订单按钮有变化,增加了'PC'
    while True:
        # 现在时间大于预设时间则开售抢购
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > buy_time:
            driver.refresh()
            try:
                # 找到“立即购买”，点击
                if driver.find_element_by_css_selector(btn_buy):
                    driver.find_element_by_css_selector(btn_buy).click()
                    # print('预售时间到，可以购买，生成订单')
                    break
                time.sleep(0.01)
                # 等待时间缩短至10ms，下同
            except:
                # print("预售时间到，但没发现'立即购买'控件")
                time.sleep(0.01)
        # else:
        #     print('预售时间没到')

    while True:
        try:
            # 找到“提交订单”，点击，
            if driver.find_element_by_css_selector(btn_order):
                driver.find_element_by_css_selector(btn_order).click()
                # 下单成功，跳转至支付页面
                print("下单成功，请支付")
                break
        except:
            time.sleep(0.01)


if __name__ == "__main__":
    # url=input("请输入商品链接:")
    # mall=input("请选择商城（淘宝 1  天猫 2  输入数字即可）： ")
    # bt=input("请输入开售时间【2019-02-15（空格）12:55:50】")
    url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.20.411b21b7musUQW&id=529408043334&ns=1&abbucket=20&skuId=3154155972259'
    # 命令行粘贴不便，还是在源代码直接输入吧
    mall = '2'
    # 同上，2是天猫，1是淘宝
    bt = '2020-02-13 00:00:00'
    # 同上，时间自己改
    bt_dt = datetime.datetime.strptime(bt, '%Y-%m-%d %H:%M:%S')
    now_dt = datetime.datetime.now()
    print("距预售时间还有%.1f秒" % ((bt_dt - now_dt).seconds))
    a = input('是否启动，Y/N？:')
    if a:
        # 创建浏览器对象
        driver = webdriver.Chrome()
        # 窗口最大化显示
        driver.maximize_window()

        login(url, mall)
        buy(bt, mall)
