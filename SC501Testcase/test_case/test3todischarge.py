#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import url


# import HTMLTestRunner

class Webtodischarge(unittest.TestCase):
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

    def is_discharge(self):  # 放电状态判断函数
        try:
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('head')
            time.sleep(0.5)
            text = self.driver.find_element_by_id('battstatus').text
            if text != 'Discharge':
                print('正在充电')
                return False
            print('正在放电')
            return True
        except Exception as msg:
            print('%s' % msg)
            return False

    def adjustvolt(self):  # 模块输出电压大于电池电压时调压函数
        try:
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame('head')
            time.sleep(0.5)
            text = self.driver.find_element_by_id('battstatus').text
            time.sleep(1)
            if text == 'Float':
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
                while (floatVolt + 0.5) > battVolt:
                    time.sleep(0.5)
                    self.driver.switch_to.parent_frame()
                    self.driver.switch_to.frame('sidebar')
                    self.driver.find_element_by_xpath('//a[contains(text(), "Quick Setting")]').click()
                    time.sleep(0.5)
                    self.driver.switch_to.parent_frame()
                    self.driver.switch_to.frame('main')
                    time.sleep(0.5)
                    self.driver.find_element_by_id('floatVolt').clear()
                    self.driver.find_element_by_id('floatVolt').send_keys(str(battVolt - 1))
                    self.driver.find_element_by_id('saveOutput').click()
                    time.sleep(0.5)
                    self.driver.switch_to.alert.accept()
                    time.sleep(5)
                    self.driver.switch_to.parent_frame()
                    self.driver.switch_to.frame('sidebar')
                    self.driver.find_element_by_xpath('//a[contains(text(), "Quick Setting")]').click()
                    time.sleep(0.5)
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
                print('调低浮充电压成功')
                return True
            else:
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('sidebar')
                self.driver.find_element_by_xpath('//a[contains(text(), "Battery Info")]').click()
                time.sleep(1)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('main')
                time.sleep(0.5)
                Capacity = float(self.driver.find_element_by_xpath('//*[@id="tr1"]/td[4]').text)
                time.sleep(0.5)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('sidebar')
                self.driver.find_element_by_xpath('//a[contains(text(), "Battery Setting")]').click()
                time.sleep(0.5)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('main')
                time.sleep(0.5)
                self.driver.find_element_by_xpath('//a[contains(text(), "Charge management")]').click()
                time.sleep(0.5)
                startCap = float(self.driver.find_element_by_id('startCap').get_attribute('value'))
                if Capacity <= startCap:  # 改电池1容量
                    self.driver.find_element_by_xpath('//a[contains(text(), "Basic Param Setting")]').click()
                    time.sleep(0.5)
                    self.driver.find_element_by_id('batt1SulCap').clear()
                    self.driver.find_element_by_id('batt1SulCap').send_keys(str(startCap + 1))
                    self.driver.find_element_by_id('confbutt').click()
                    time.sleep(1)
                    self.driver.switch_to.alert.accept()
                    time.sleep(1)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('sidebar')
                self.driver.find_element_by_xpath('//span[contains(text(), "System Control")]').click()
                time.sleep(1)
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('main')
                time.sleep(0.5)
                sysModeTxt = self.driver.find_element_by_id('sysModeTxt').text
                if sysModeTxt == 'Auto':
                    self.driver.find_element_by_id('ManualBt').click()  # 转手动模式
                    self.driver.switch_to.alert.accept()
                    time.sleep(0.5)
                    self.driver.switch_to.alert.accept()
                try:
                    self.driver.find_element_by_id('FloatBt').click()  # 转浮充（自动转均充的转手动模式就能自动转浮充，若手动转均充的，需要手动转浮充才行）
                    self.driver.switch_to.alert.accept()
                    time.sleep(0.5)
                    self.driver.switch_to.alert.accept()
                except:
                    pass
                self.driver.find_element_by_id('AutoBt').click()  # 转自动模式
                self.driver.switch_to.alert.accept()
                time.sleep(0.5)
                self.driver.switch_to.alert.accept()
                time.sleep(1)
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
                while (floatVolt + 0.5) > battVolt:  # 调低浮充电压
                    time.sleep(1)
                    self.driver.switch_to.parent_frame()
                    self.driver.switch_to.frame('sidebar')
                    self.driver.find_element_by_xpath('//a[contains(text(), "Quick Setting")]').click()
                    time.sleep(0.5)
                    self.driver.switch_to.parent_frame()
                    self.driver.switch_to.frame('main')
                    time.sleep(0.5)
                    self.driver.find_element_by_id('floatVolt').clear()
                    self.driver.find_element_by_id('floatVolt').send_keys(str(battVolt - 1))
                    self.driver.find_element_by_id('saveOutput').click()
                    time.sleep(0.5)
                    self.driver.switch_to.alert.accept()
                    time.sleep(5)
                    self.driver.switch_to.parent_frame()
                    self.driver.switch_to.frame('sidebar')
                    self.driver.find_element_by_xpath('//a[contains(text(), "Quick Setting")]').click()
                    time.sleep(0.5)
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
                print('调低浮充电压成功')
                return True
        except Exception as msg:
            print('%s' % msg)
            return False

    def test_todischarge(self):
        "转放电测试用例"
        self.login()  # 登录
        result = self.is_discharge()  # 判断是否放电状态
        if result == False:
            result = self.adjustvolt()  # 读取均浮充状态再调压
            if result == False:
                print('调压失败,测试不通过')
                self.assertTrue(result)
            time.sleep(4)
            result = self.is_discharge()  # 判断是否放电状态
            if result:
                print('转放电成功，测试通过')
            else:
                print('仍是充电状态，测试不通过')
            self.assertTrue(result)
        else:
            print('正在放电状态，不用转换')
            self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()  # 单个运行时不注释，还要将下面两行注释掉；作为多个py文件运行时，要注释掉，下面两行不注释
    suite = unittest.TestSuite()
    suite.addTest(Webtodischarge("test_todischarge"))  # 在单个py文件中导入用（类名（"方法名"））
