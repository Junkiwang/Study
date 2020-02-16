#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Junki
import os
from selenium import webdriver
import datetime
import time
from os import path

driver = webdriver.Chrome()


# driver.create_options().add_argument('--log-level=3')
# driver.maximize_window()

def login():
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    now = datetime.datetime.now()
    print("login success:", now.strftime("%Y-%m-%d %H:%M:%S"))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(buytime)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            # driver.refresh()  # 商品网页到点自动刷新则不用刷新
            try:
                if driver.find_element_by_id("J_SelectAll1"):
                    # driver.find_element_by_xpath('//label[@for="J_CheckBox_1350404472046"]').click()  # 勾选某个商品
                    driver.find_element_by_id("J_SelectAll1").click()  # 勾选全部商品
                # if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()  # 结算
                    driver.find_element_by_link_text("提交订单").click()
                    break
            except:
                time.sleep(0.01)
        # print(now)
        time.sleep(0.01)


if __name__ == "__main__":
    times = '2020-02-14 00:00:00'  # input("请输入抢购时间(例如格式：2019-07-23 15:30:00):")
    login()
    buy(times)
