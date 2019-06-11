#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
# coding:utf-8

# 从wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数
from helloweb import application

# 创建一个服务器，IP地址为本机地址192.168.1.100，端口是8000，处理函数是application
httpd = make_server('192.168.1.100', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
