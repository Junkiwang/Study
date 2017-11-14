#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki

# driver = webdriver.Chrome()
# driver.implicitly_wait(30)
# base_url = "http://www.baidu.com/"
# driver.get(base_url)
# a= driver.find_element_by_id("kw")
# locator = ("name", "tj_trnews")
# text = u"新闻"
# result = EC.text_to_be_present_in_element(locator, text)(driver)
# print(result)
# print("hello")

#
# for i in range(5):
#     for j in range(5):
#         for k in range(5):
#             if i == j == k == 3:
#                 break
#             else:
#                 print(i, '----', j, '----', k)
#         else:
#             continue
#         break
#     else:
#         continue
#     break

# class Login(unittest.TestCase):
#     def setUp(self):
#         url_login = "https://passport.cnblogs.com/user/signin"
#         self.driver = webdriver.Chrome()
#         self.driver.get(url_login)
#
#     def test_01(self):
#         "前面输入账号密码，让正确运行到assert这一步，断言故意设置为False不成功"
#         try:
#             self.driver.find_element_by_id("input1").send_keys(u"上海-悠悠")
#             self.driver.find_element_by_id("input2").send_keys("xxx")
#             self.driver.find_element_by_id("signin").click() # 登录id是错的，定位会抛异常
#             time.sleep(3)
#
#             # 　判断登录成功页面是否有账号："上海-悠悠"
#             locator = ("id", "lnk_current_user")
#             result = EC.text_to_be_present_in_element(locator, u"上海-悠悠")(self.driver)
#             self.assertFalse(result)
#         except Exception as msg:
#             print("异常原因%s" % msg)
#             nowTime = time.strftime("%Y%m%d.%H.%M.%S")
#             self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
#             raise
#
#     def tearDown(self):
#         self.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()



# 文档测试
# class Dict(dict):
#     '''
#     Simple dict but also support access as x.y style.
#
#     >>> d1 = Dict()
#     >>> d1['x'] = 100
#     >>> d1.x
#     100
#     >>> d1.y = 200
#     >>> d1['y']
#     200
#     >>> d2 = Dict(a=1, b=2, c='3')
#     >>> d2.c
#     '3'
#     >>> d2['empty']
#     Traceback (most recent call last):
#         ...
#     KeyError: 'empty'
#     >>> d2.empty
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'Dict' object has no attribute 'empty'
#     '''
#
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#
# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()

# 操作文件和目录

# from datetime import datetime
# import os
# print(os.name, os.environ)
# pwd = os.path.abspath('.')
# print(pwd)
# print('      Size Last Modified    Name')
# print('-----------------------------------------------------')
# for f in os.listdir(pwd):
#     fsize = os.path.getsize(f)
#     mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#     flag = '/' if os.path.isdir(f) else ''
#     print('%10d %s %s%s' % (fsize, mtime, f, flag))

# 序列化
# dump和load是处理文件对象，dumps和loads是直接在内存上处理

# import pickle
#
# d = dict(name='Bob', age=12, socre=3)
# print(pickle.dumps(d))
# with open('pickle.txt', 'wb') as f:  # bytes序列化，用二进制读写
#     pickle.dump(d, f)
# with open('pickle.txt', 'rb') as f:  # 反序列化
#     d = pickle.load(f)
#     print(d)
#
# import json
#
# d = dict(name='Bob', age=12, socre=88)
# print(json.dumps(d))
# with open('json.txt', 'w') as f:  # str序列化，用字节读写
#     json.dump(d, f)
# with open('json.txt', 'r') as f:  # 反序列化
#     d = json.load(f)
#     print(d)
#
#
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def __str__(self):
#         return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)
#
# s = Student('Bob', 20, 88)
# std_data = json.dumps(s, default=lambda obj: obj.__dict__)
# print('Dump Student:', std_data)
# rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
# print(rebuild)

# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 多进程
# from multiprocessing import Process
# import os
#
#
# def run_proc(name):  # 子进程要执行的代码
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# 进程池
# from multiprocessing import Pool
# import time, os, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(2)
#     for i in range(4):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocess done...')
#     p.close()
#     p.join()
#     print('All subprocess done.')

# 子进程
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

import subprocess  # 用communicate加输入的子进程

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))  # windows的CMD命令窗口默认gbk编码
print('Exit code:', p.returncode)

# 进程间通信
# from multiprocessing import Queue, Process
# import time, os, random
#
#
# def write(q):  # 写数据进程的执行代码
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# def read(q):  # 读数据进程的执行代码
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
#
# if __name__ == '__main__':
#     q = Queue()  # 父进程创建Queue，并传给各个子进程
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()  # 启动写的子进程
#     pr.start()  # 启动读的子进程
#     pw.join()  # 等待pw结束
#     pr.terminate()  # pr进程里是死循环，无法等待其结束，只能强行终止

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time
#
# driver = webdriver.Chrome()
# url = 'http://172.18.20.250'
# driver.get(url)
# driver.implicitly_wait(10)
# driver.find_element_by_id('user').clear()
# driver.find_element_by_id('user').send_keys('root')
# driver.find_element_by_id('password').clear()
# driver.find_element_by_id('password').send_keys('000000')
# driver.find_element_by_xpath('//input[@value="Login"]').click()
# time.sleep(1)
#
# import time
#
# a = time.time()
# time.sleep(1)
# print(time.time() - a)
#
#
# import xlrd
#
# file = 'test.xlsx'
# xls1 = xlrd.open_workbook(file)
# table = xls1.sheet_by_name('Sheet1')
# dataresult = [table.row_values(i) for i in range(0, table.nrows)]
# result = [dict(zip(dataresult[0], dataresult[i])) for i in range(1, len(dataresult))]
# print(result)
#
# def action(button):
#     print('please enter the button %s' % button)
#
#
# def partial(func, arg):
#     def callme():
#         return func(arg)
#
#     return callme()
#
# partial(action, 'one')

# import sys
# from PyQt5 import QtWidgets
# app = QtWidgets.QApplication(sys.argv)
# button = QtWidgets.QPushButton('Hello')
# button.setFixedSize(400, 400)
# button.show()
# app.exec_()


# print("输入坐标")
# xx = input("x's：")
# yy = input("y's：")
# xx = xx.split('/')
# list(map(float, xx))
# yy = yy.split('/')
# list(map(float, yy))
# a = float(list(xx)[0])
# b = float(list(xx)[1])
# c = float(list(yy)[0])
# d = float(list(yy)[1])
#
# print("第一个点是：(" + str(a) + "," + str(c) + ")")
# print("第一个点是：(" + str(b) + "," + str(d) + ")")
#
# x0 = float(a - b)
# y0 = float(c - d)
#
# print("直线方程为：")
# if x0 == 0:
#     print("x=", a)
# else:
#     print("y=%.4f(x-%r)+%.2f" % (y0 / x0, a, c))
