#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki

from selenium import webdriver
import datetime
import time


def login(url):
    '''
    登陆函数
    url:商品的链接
    mall：商城类别
    '''
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)
    # 找到并点击京东的登陆按钮
    driver.find_element_by_link_text("你好，请登录").click()
    print("请在20秒内完成登录!")
    # 用户扫码登陆
    time.sleep(20)


def buy(buy_time, buytype):
    '''
    购买函数
    buy_time:购买时间
    buytype:抢购类型
    获取页面元素的方法有很多，获取得快速准确又是程序的关键
    在写代码的时候运行测试了很多次，css_selector的方式表现最佳
    '''
    if buytype == '1':
        # '立即抢购'的css_selector
        btn_buy = '#btn-reservation'
        # '加入购物车'的css_selector
        # btn_buy = '#InitCartUrl'
        # '去结算'的css_selector
        btn_order1 = '#cart-floatbar > div > div > div > div.options-box > div.toolbar-right.toolbar-right-new > div.normal > div > div.btn-area > a'
        # '提交订单'的css_selector
        btn_order2 = '# order-submit'

        while True:
            # 现在时间大于预设时间则开售抢购
            if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > buy_time:
                driver.refresh()  # 商品网页到点自动刷新则不用刷新
                try:
                    # 找到“立即抢购”，点击
                    if driver.find_element_by_css_selector(btn_buy):
                        driver.find_element_by_css_selector(btn_buy).click()
                        time.sleep(0.02)
                        driver.find_element_by_css_selector(btn_order1).click()
                        # print('预售时间到，可以购买，生成订单')
                        break
                    time.sleep(0.01)
                    # 等待时间缩短至10ms，下同
                except:
                    # print("预售时间到，但没发现'立即抢购'控件")
                    time.sleep(0.01)
            # else:
            #     print('预售时间没到')

        while True:
            try:
                # 找到“提交订单”，点击，
                if driver.find_element_by_css_selector(btn_order2):
                    driver.find_element_by_css_selector(btn_order2).click()
                    # 下单成功，跳转至支付页面
                    print("下单成功，请支付")
                    break
            except:
                print("已抢购，但没发现'提交订单'控件")
                time.sleep(0.01)
    else:
        # "立即预约"的css_selector
        btn_buy = '#btn-reservation'
        while True:
            # 现在时间大于预设时间则预约
            if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > buy_time:
                # driver.refresh()  # 商品网页到点自动刷新则不用刷新
                try:
                    # 找到“立即预约”，点击
                    if driver.find_element_by_css_selector(btn_buy):
                        driver.find_element_by_css_selector(btn_buy).click()
                        # print('预约时间到，预约成功')
                        break
                    time.sleep(0.01)
                    # 等待时间缩短至10ms，下同
                except:
                    # print("预约时间到，但没发现'立即预约'控件")
                    time.sleep(0.01)
            # else:
            #     print('预约时间没到')



if __name__ == "__main__":
    # url=input("请输入商品链接:")
    # buytype=input("请选择购买类型（1是立即购买，2是立即预约  输入数字即可）： ")
    # bt=input("请输入开售时间【2019-02-15（空格）12:55:50】")
    url = 'https://item.jd.com/100011385146.html#none'
    # url = 'https://item.jd.com/11403981.html'
    buytype = '1'
    # 1是立即购买，2是立即预约
    # 命令行粘贴不便，还是在源代码直接输入吧
    bt = '2020-02-16 20:00:00'
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

        login(url)
        buy(bt, '1')
