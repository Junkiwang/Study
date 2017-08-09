#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import os
import configparser
import codecs


class ReadConfig():
    """
    专门读取配置文件的，.ini文件格式
    """

    def __init__(self, filename):
        # configpath = os.path.join(prjDir,filename)
        configpath = filename
        # print(configpath)
        fd = open(configpath)
        data = fd.read()
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:  # 去掉BOM编码的前三位
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()

        self.config = configparser.ConfigParser()
        self.config.read(configpath)

    def getValue(self, env, name):
        """
        [projectConfig]
        project_path=E:/Python-Project/UItestframework
        :param env:[projectConfig]
        :param name:project_path
        :return:E:/Python-Project/UItestframework
        """
        return self.config.get(env, name)


# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]  # 获取配置文件所在路径
read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))  # 实例化
# 项目参数设置
project_path = read_config.getValue('projectConfig', 'project_path')  # 获取配置文件中的项目路径
# 设置测试用例路径
test_case_path = os.path.join(project_path, 'test_case')
# 设置日志路径
log_path = os.path.join(project_path, 'report', 'log')
# 设置截图文件路径
img_path = os.path.join(project_path, 'report', 'image')
# 设置测试报告路径
report_path = os.path.join(project_path, 'report', 'testreport')
# 设置默认浏览器
browser = 'Chrome'
# 设置测试数据路径
data_path = os.path.join(project_path, 'data')
