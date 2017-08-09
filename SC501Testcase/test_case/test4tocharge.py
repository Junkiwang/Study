#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import url


# import HTMLTestRunner

class Webtocharge(unittest.TestCase):
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

    def is_charge(self):  # 充电状态判断函数
        try:
            time.sleep(1)
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('head')
            time.sleep(1)
            text = self.driver.find_element_by_id('battstatus').text
            if text == 'Discharge':
                print('正在放电')
                return False
            print('正在充电')
            return True
        except Exception as msg:
            print('%s' % msg)
            return False

    def comparevolt(self):  # 比较模块输出电压和电池电压大小函数
        try:
            self.driver.switch_to.parent_frame()  # 读取电池电压
            self.driver.switch_to.frame('sidebar')
            self.driver.find_element_by_xpath('//a[contains(text(), "Power System")]').click()
            time.sleep(1)
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('main')
            time.sleep(0.5)
            battVolt = float((self.driver.find_element_by_id('battVolt').text).strip('V'))
            time.sleep(1)
            self.driver.switch_to.parent_frame()  # 读取模块输出设置电压
            self.driver.switch_to.frame('sidebar')
            self.driver.find_element_by_xpath('//a[contains(text(), "Quick Setting")]').click()
            time.sleep(1)
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('main')
            time.sleep(0.5)
            modulevolt = float(self.driver.find_element_by_id('floatVolt').get_attribute('value'))
            if modulevolt <= (battVolt + 0.3):
                print('模块输出电压≤电池电压')
                return True
            else:
                print('模块输出电压＞电池电压')
                return False
        except Exception as msg:
            print('%s' % msg)
            return False

    def adjustvolt(self):  # 模块输出电压小于电池电压时调压函数
        try:
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('sidebar')
            self.driver.find_element_by_xpath('//a[contains(text(), "Quick Setting")]').click()
            time.sleep(1)
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('main')
            time.sleep(0.5)
            floatVolt = float(self.driver.find_element_by_id('floatVolt').get_attribute('value'))
            time.sleep(0.5)
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('sidebar')
            self.driver.find_element_by_xpath('//a[contains(text(), "Power System")]').click()
            time.sleep(0.5)
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('main')
            time.sleep(0.5)
            battVolt = float((self.driver.find_element_by_id('battVolt').text).strip('V'))
            while (floatVolt - 0.5) <= battVolt and floatVolt < 53:  # 调高浮充电压
                time.sleep(1)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('sidebar')
                self.driver.find_element_by_xpath('//a[contains(text(), "Quick Setting")]').click()
                time.sleep(1)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('main')
                time.sleep(1)
                self.driver.find_element_by_id('floatVolt').clear()
                self.driver.find_element_by_id('floatVolt').send_keys(str(battVolt + 1))
                self.driver.find_element_by_id('saveOutput').click()
                time.sleep(1)
                self.driver.switch_to.alert.accept()
                time.sleep(5)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('sidebar')
                self.driver.find_element_by_xpath('//a[contains(text(), "Quick Setting")]').click()
                time.sleep(1)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('main')
                time.sleep(0.5)
                floatVolt = float(self.driver.find_element_by_id('floatVolt').get_attribute('value'))
                time.sleep(1)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('sidebar')
                self.driver.find_element_by_xpath('//a[contains(text(), "Power System")]').click()
                time.sleep(0.5)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('main')
                time.sleep(0.5)
                battVolt = float((self.driver.find_element_by_id('battVolt').text).strip('V'))
            print('调高浮充电压成功')
            return True
        except Exception as msg:
            print('%s' % msg)
            return False

    def test_tocharge(self):
        "转充电测试用例"
        self.login()  # 登录
        result = self.is_charge()  # 判断是否充电状态
        if result == False:
            result = self.comparevolt()  # 比较电压大小
            if result == False:
                print('放电状态异常，测试不通过')
                self.assertTrue(result)
            else:
                result = self.adjustvolt()  # 读取浮充电压大小调节直到大于电池电压
                if result == False:
                    print('调压失败,测试不通过')
                    self.assertTrue(result)
                time.sleep(4)
                result = self.is_charge()  # 判断是否充电状态
                if result:
                    print('转充电成功，测试通过')
                else:
                    print('仍是放电状态，测试不通过')
                    self.assertTrue(result)
        else:
            print('正在充电状态，不用转换')
            self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()  # 单个运行时不注释，还要将下面两行注释掉；作为多个py文件运行时，要注释掉，下面两行不注释
    suite = unittest.TestSuite()
    suite.addTest(Webtocharge("test_tocharge"))  # 在单个py文件中导入用（类名（"方法名"））
