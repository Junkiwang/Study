#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re

# 引入HTMLTestRunner包
import HTMLTestRunner


class Baidu(unittest.TestCase):
    # 初始化设置
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_text(self):
        u'文本存在用例'  # 中文解释-测试报告
        driver = self.driver
        driver.get(self.base_url)
        locator = ("name", "tj_trnews")
        text = u"新闻"
        result = EC.text_to_be_present_in_element(locator, text)(driver)
        self.assertTrue(result)

    # 百度搜索用例
    def test_baidu(self):
        u'百度搜索用例'  # 中文解释-测试报告
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("Selenium Webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    # 定义一个测试容器
    test = unittest.TestSuite()

    # 将测试用例，加入到测试容器中
    test.addTest(Baidu("test_text"))
    test.addTest(Baidu("test_baidu"))

    # 读取当前时间，将时间加到测试报告名称中去,文件名规定不许有”\/:?*“等符号
    now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
    print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time())))
    # 定义个报告存放的路径，支持相对路径
    file_path = "E:\\Python_simple\SC501Testcase\TestReports\\" + now + "result.html"
    file_result = open(file_path, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title=u"测试报告", description=u"用例执行情况")

    # 运行测试用例
    runner.run(test)
    file_result.close()  # 关闭文件
