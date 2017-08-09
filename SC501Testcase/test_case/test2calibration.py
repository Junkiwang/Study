#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import url


# import HTMLTestRunner

class Webcalibration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url.url())
        self.driver.implicitly_wait(10)

    def login(self):  # 登录函数
        self.driver.find_element_by_id('user').clear()
        self.driver.find_element_by_id('user').send_keys('root')
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys('000000')
        self.driver.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(1)

    def is_MCB_off(self):  # 断开空开判断函数
        try:
            a = input('请断开所有空开，断开后请输"1":')
            if a:
                print('空开断开成功')
                return True
        except Exception as msg:
            print('%s' % msg)
            return False

    def is_MCB_on(self):  # 合上空开判断函数
        try:
            b = input('请合上所有空开，合上后请输"1":')
            if b:
                print('空开合上成功')
                return True
        except Exception as msg:
            print('%s' % msg)
            return False

    def is_current_zero(self):  # 电流为零判断函数
        try:
            time.sleep(1)
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('sidebar')
            self.driver.find_element_by_xpath('//a[contains(text(),"Calibration Setting")]').click()
            time.sleep(1)
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('main')
            for n in range(3):
                L = ['负载电流', '电池1电流', '电池2电流']
                Select(self.driver.find_element_by_id('caliParam')).select_by_index(n)
                time.sleep(1)
                current = float(self.driver.find_element_by_id('sample').text)
                if abs(current) >= 0.4:  # 误差太大
                    print('%s误差大，需要校准' % L[n])
                    return False
            print('所有电流零点准确，不需要校准')
            return True
        except Exception as msg:
            print('%s' % msg)
            return False

    def Reference_Calibrate(self):
        try:
            print('进行基准校准')
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('main')
            self.driver.find_element_by_id('RefStart').click()
            self.driver.switch_to.alert.accept()
            time.sleep(5)
            self.driver.find_element_by_id('RefEnd').click()
            text = []
            text.append(self.driver.find_element_by_id('loadCurr').text)
            text.append(self.driver.find_element_by_id('battCurr1').text)
            text.append(self.driver.find_element_by_id('battCurr2').text)
            for i in text:
                if i != 'Completed':
                    print('基准校准失败')
                    return False
            print('基准校准完成')
            return True
        except Exception as msg:
            print('%s' % msg)
            return False

    def send_LowPoint(self):
        try:
            print('进行下发低点校准')
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('main')
            for n in range(3):
                Select(self.driver.find_element_by_id('caliParam')).select_by_index(n)
                time.sleep(1)
                self.driver.find_element_by_id('Low').clear()
                self.driver.find_element_by_id('Low').send_keys('0.0')
                time.sleep(1)
                self.driver.find_element_by_xpath('//input[@value="Send" and @onclick="SendLow()"]').click()
            print('下发低点完成')
            return True
        except Exception as msg:
            print('%s' % msg)
            return False

    @unittest.skip('无条件跳过此用例')
    def test_calibration(self):
        "校准功能测试用例"
        self.login()  # 登录
        # self.is_MCB_off()  # 断开空开
        result = self.is_current_zero()  # 判断电流是否为0
        if result == False:
            self.Reference_Calibrate()  # 进行基准校准
            result = self.is_current_zero()  # 判断电流是否为0
            if result == False:
                self.send_LowPoint()  # 进行下发低点校准
                result = self.is_current_zero()  # 判断电流是否为0
                self.assertTrue(result)
            else:
                self.assertTrue(result)
        else:
            self.assertTrue(result)
        # self.is_MCB_on()  # 合上空开

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()  # 单个运行时不注释，还要将下面两行注释掉；作为多个py文件运行时，要注释掉，下面两行不注释
    suite = unittest.TestSuite()
    suite.addTest(Webcalibration("test_calibration"))  # 在单个py文件中导入用（类名（"方法名"））
