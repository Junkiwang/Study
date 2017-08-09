#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki

import unittest
from selenium import webdriver
import time
import url
from config import globalconfig


# import HTMLTestRunner


class Weblogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url.url())
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
        except Exception as msg:
            print('%s' % msg)
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
        except Exception as msg:
            print('%s' % msg)
            return False

    def is_login_fail(self):  # 登录失败判断函数
        try:
            elem = self.driver.switch_to.alert
            text = elem.text
            elem.accept()
            usename = self.driver.find_element_by_id('user').get_attribute("value")
            password = self.driver.find_element_by_id('password').get_attribute("value")
            print(usename + ':' + password + '--->' + text)
            if text:
                return True
        except Exception as msg:
            print('%s' % msg)
            return False

    def test_login(self):
        "登录测试用例"
        # num = len(open('E:\\Python_simple\\SC501Testcase\\test_case\\accounts.txt').readlines())
        num = len(open(os.path.join(data_path, 'accounts.txt')).readlines())
        L = []
        with open(os.path.join(data_path, 'accounts.txt')) as f:  # 系统会在执行完文件操作后自动关闭文件
            for l in f.readlines():
                L.append(l.strip('\n'))
        print('\n测试数据：%s\n' % L)
        for i in range(num):
            USE = L[i].split(':')
            a = [USE[0], USE[1]]
            b = [['root', '000000'], ['admin', '170313'], ['engineer', '1031'], ['guest', 'guest']]  # 正确的用户名和密码
            if a in b:
                self.login(USE[0], USE[1])
                result = self.is_login_success()
                self.assertTrue(result)
                result = self.is_logout_success()
                self.assertTrue(result)
            else:
                self.login(USE[0], USE[1])
                result = self.is_login_fail()
                self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()  # 单个运行时不注释，还要将下面两行注释掉；作为多个py文件运行时，要注释掉，下面两行不注释
    suite = unittest.TestSuite()
    suite.addTest(Weblogin("test_login"))  # 在单个py文件中导入用（类名（"方法名"））
