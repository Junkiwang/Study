#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki

import time
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


class PID:
    def __init__(self):
        self.Kp = 0
        self.Kd = 0
        self.Ki = 0
        self.Initialize()

    def SetKp(self, invar):
        self.Kp = invar

    def SetKd(self, invar):
        self.Kd = invar

    def SetKi(self, invar):
        self.Ki = invar

    def SetPrevErr(self, preverr):
        self.prev_err = preverr

    def Initialize(self):
        self.currtm = time.time()
        self.prevtm = self.currtm

        self.prev_err = 0

        self.Cp = 0
        self.Cd = 0
        self.Ci = 0

    def Genout(self, error):
        self.currtm = time.time()
        dt = self.currtm - self.prevtm
        de = error - self.prev_err

        self.Cp = self.Kp * error
        self.Ci += error * dt

        self.Cd = 0
        if dt > 0:
            self.Cd = de / dt

        self.prevtm = self.currtm
        self.prev_err = error
        return self.Cp + (self.Ki * self.Ci) + (self.Kd * self.Cd)


def PIDPlot(Kp=1.0, Ki=0.0, Kd=0.0, L=100):
    pid = PID()
    pid.SetKp(Kp)
    pid.SetKi(Ki)
    pid.SetKd(Kd)

    time.sleep(0.1)
    setpoint = 0
    feedback = 0
    outv = 0

    # print('Kp: %2.3f Ki: %2.3f Kd: %2.3f' % (pid.Kp, pid.Ki, pid.Kd))
    feedback_list = []
    time_list = []
    setpoint_list = []

    for i in range(0, L):
        # 求和节点，目标值和反馈值求和
        err = setpoint - feedback
        outv = pid.Genout(err)
        if setpoint > 0:
            # 控制反馈函数
            feedback += (outv - (1 / i))
        # 从 setpoint=0 开始，在t(10)模拟一个阶跃输入
        if i > 2:
            setpoint = 1
        # print('%d %2.3f %2.3f %2.3f %2.3f' % (i, setpoint, feedback, err, outv))
        time.sleep(0.05)
        feedback_list.append(feedback)
        setpoint_list.append(setpoint)
        time_list.append(i)
        # print(feedback_list, setpoint_list, time_list)

    # 曲线数据处理
    time_sm = np.array(time_list)
    time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)  # 从大小到大生成300个线性等差数列，绘制的曲线将更加平滑
    feedback_sm = make_interp_spline(time_list, feedback_list)
    feedback_smooth = feedback_sm(time_smooth)  # 对应时间轴上的300个点对应生成300个纵轴上的数据点，曲线将更加平滑

    # 画曲线
    plt.figure(0)
    plt.plot(time_smooth, feedback_smooth)  # 建立横坐标和纵坐标的参数画PID控制曲线，横轴和纵轴的样本个数要一致
    plt.plot(time_list, setpoint_list)  # 画阶跃输入曲线
    plt.xlim((0, L))  # 设置横轴刻度范围
    plt.ylim((min(feedback_list) - 0.5, max(feedback_list) + 0.5))  # 设置纵轴刻度范围
    plt.xlabel('time (s)')  # 设置横轴标签名称
    plt.ylabel('PID (PV)')  # 设置纵轴标签名称
    plt.title('TEST PID')  # 设置图表标题名称
    # plt.ylim((1 - 0.5, 1 + 0.5))
    plt.grid(True)  # 显示网格
    plt.show()


if __name__ == '__main__':
    PIDPlot(1.2, 1, 0.01, 50)
