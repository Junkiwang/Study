#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import unittest
from selenium import webdriver
import time
import accounts


class Weblogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        url = 'http://172.18.20.253'
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def login(self, username, password):  # 登录函数
        self.driver.find_element_by_id('user').clear()
        self.driver.find_element_by_id('user').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(1)

    def is_login_success(self):  # 登录成功判断函数
        try:
            self.driver.switch_to.frame('head')
            text = self.driver.find_element_by_xpath('//*[@id="accesslevel"]').text
            print(text + '--->登录成功')
            return True
        except:
            return False

    def is_logout_success(self):  # 登出成功判断函数
        try:
            # self.driver.switch_to.frame('head')
            self.driver.find_element_by_xpath("//a[contains(text(), 'Logout')]").click()
            time.sleep(1)
            text = self.driver.find_element_by_xpath("//*[contains(text(), 'Login')]").text
            if text:
                print('已登出')
            return True
        except:
            return False

    def is_login_fail(self):  # 登录失败判断函数
        try:
            elem = self.driver.switch_to.alert
            text = elem.text
            elem.accept()
            usename = self.driver.find_element_by_id('user').get_attribute("value")
            password = self.driver.find_element_by_id('password').get_attribute("value")
            print(text + '>' + usename, password)
            if text:
                return True
        except:
            return False

    def test_login(self):
        "登录测试用例"
        for k, v in accounts.usedict().items():
            a = {k: v}
            b = {'root': '000000', 'admin': '170313', 'engineer': '1031', 'guest': 'guest'}
            if set(a.items()).issubset(b.items()):
                self.login(k, v)
                result = self.is_login_success()
                self.assertTrue(result)
                result = self.is_logout_success()
                self.assertTrue(result)
            else:
                self.login(k, v)
                result = self.is_login_fail()
                self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
