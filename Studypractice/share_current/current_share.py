#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Junki
# coding:utf-8

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Sharecurrent(QWidget):
    def __init__(self, parent=None):
        super(Sharecurrent, self).__init__(parent)
        self.setWindowTitle('模块均流不平衡度计算器')
        self.setWindowIcon(QIcon('./images/cartoon1.ico'))

        layout = QFormLayout()
        self.input1 = QLineEdit()
        layout.addRow('输入测试电压(V)：', self.input1)

        self.input2 = QLineEdit()
        layout.addRow('输入单模块额定功率(W)：', self.input2)

        self.label1 = QLabel('输入用“/”间隔的均流电流数据(A)：')
        layout.addRow(self.label1)
        self.input3 = QLineEdit()
        layout.addRow(self.input3)

        self.btn1 = QPushButton('计算')
        layout.addRow(self.btn1)
        layout.setAlignment(self.btn1, Qt.AlignRight)
        self.btn1.clicked.connect(self._calc)

        self.label2 = QLabel()
        layout.addRow('电流平均值(A)：', self.label2)

        self.label3 = QLabel()
        layout.addRow('电流极值(A)：', self.label3)

        self.input4 = QLineEdit()
        layout.addRow('最大均流不平衡度(%)：', self.input4)
        self.setLayout(layout)

    def _calc(self):
        try:
            U = float(self.input1.text())
            P = float(self.input2.text())
            L = self.input3.text()
            L = L.split('/')
            L = list(map(float, L))
            sum = 0
            for n in L:
                sum += n
            average_value = sum / len(L)
            l = []
            for m in L:
                difference_value = abs(m - average_value)
                l.append(difference_value)
            n = l.index(max(l))
            result = (max(l) / (P/U)) * 100
            self.label2.setText('%0.2f' % average_value)
            self.label3.setText('%0.2f' % L[n])
            self.input4.setText('%0.2f' % result)
        except:
            reply = QMessageBox.warning(self, '错误提示', '无效输入')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Sharecurrent()
    win.show()
    sys.exit(app.exec_())
