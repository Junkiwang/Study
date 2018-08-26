#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Junki
# coding:utf-8

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class FormulaDemo(QWidget):
    def __init__(self, parent=None):
        super(FormulaDemo, self).__init__(parent)
        self.setWindowTitle('一元一次方程式计算器')
        self.setWindowIcon(QIcon('./images/cartoon1.ico'))

        layout = QGridLayout()
        self.doublevalidator = QDoubleValidator()  # 设置浮点数验证器
        self.doublevalidator.setRange(-100, 100)
        self.doublevalidator.setNotation(QDoubleValidator.StandardNotation)
        self.doublevalidator.setDecimals(2)

        self.label = QLabel('在下面输入框输入方程式两个点：')
        layout.addWidget(self.label, 0, 0, 1, 4)

        self.label1 = QLabel('x1:')
        self.input1 = QLineEdit()
        self.input1.setValidator(self.doublevalidator)
        self.label1.setBuddy(self.input1)
        layout.addWidget(self.label1, 1, 0, 1, 1)
        layout.addWidget(self.input1, 1, 1, 1, 1)

        self.label2 = QLabel('y1:')
        self.input2 = QLineEdit()
        self.input2.setValidator(self.doublevalidator)
        self.label2.setBuddy(self.input2)
        layout.addWidget(self.label2, 1, 2, 1, 1)
        layout.addWidget(self.input2, 1, 3, 1, 1)

        self.label3 = QLabel('x2:')
        self.input3 = QLineEdit()
        self.input3.setValidator(self.doublevalidator)
        self.label3.setBuddy(self.input3)
        layout.addWidget(self.label3, 2, 0, 1, 1)
        layout.addWidget(self.input3, 2, 1, 1, 1)

        self.label4 = QLabel('y2:')
        self.input4 = QLineEdit()
        self.input4.setValidator(self.doublevalidator)
        self.label4.setBuddy(self.input4)
        layout.addWidget(self.label4, 2, 2, 1, 1)
        layout.addWidget(self.input4, 2, 3, 1, 1)

        self.btn1 = QPushButton('保存')
        self.btn1.clicked.connect(self._calcformula)
        layout.addWidget(self.btn1, 3, 4, 1, 1)

        self.label5 = QLabel('所得一元一次方程式为：')
        self.label6 = QLabel()
        self.label5.setBuddy(self.label6)
        layout.addWidget(self.label5, 4, 0, 1, 2)
        layout.addWidget(self.label6, 4, 2, 1, 2)

        self.label9 = QLabel()
        layout.addWidget(self.label9, 5, 0, 1, 4)

        self.label10 = QLabel('输入一坐标计算另一坐标:')
        layout.addWidget(self.label10, 6, 0, 1, 2)

        self.label7 = QLabel('x:')
        self.input5 = QLineEdit()
        self.input5.setValidator(self.doublevalidator)
        self.label7.setBuddy(self.input5)
        layout.addWidget(self.label7, 7, 0, 1, 1)
        layout.addWidget(self.input5, 7, 1, 1, 1)

        self.label8 = QLabel('y:')
        self.input6 = QLineEdit()
        self.input6.setValidator(self.doublevalidator)
        self.label8.setBuddy(self.input6)
        layout.addWidget(self.label8, 7, 2, 1, 1)
        layout.addWidget(self.input6, 7, 3, 1, 1)

        self.btn2 = QPushButton('计算')
        self.btn2.clicked.connect(self._calcpoint)
        layout.addWidget(self.btn2, 7, 4, 1, 1)
        self.btn3 = QPushButton('清除')
        self.btn3.clicked.connect(self._clearpoint)
        layout.addWidget(self.btn3, 8, 4, 1, 1)
        self.setLayout(layout)

    def _calcformula(self):
        try:
            x1 = float(self.input1.text())
            y1 = float(self.input2.text())
            x2 = float(self.input3.text())
            y2 = float(self.input4.text())
            if x1 == x2:
                self.label6.setText('x = %0.2f' % x1)
            elif y1 == y2:
                self.label6.setText('y = %0.2f' % y1)
            else:
                global k, b
                k = (y1 - y2) / (x1 - x2)
                b = y1 - (k * x1)
                if b < 0:
                    b1 = abs(b)
                    self.label6.setText('y = %0.2fx - %0.2f' % (k, b1))
                elif b == 0:
                    self.label6.setText('y = %0.2fx' % k)
                else:
                    self.label6.setText('y = %0.2fx + %0.2f' % (k, b))
            return (k, b)
        except:
            reply = QMessageBox.warning(self, '错误提示', '无效输入')
            print(reply)

    def _calcpoint(self):
        try:
            try:
                x = float(self.input5.text())
                # 类似于def f(x)，其中f = lambda x: (k * x) + b),打印出计算的f(x)
                self.input6.setText('%0.2f' % (lambda x: (k * x) + b)(x))
            except:
                y = float(self.input6.text())
                self.input5.setText('%0.2f' % (lambda y: (y - b) / k)(y))
        except:
            reply = QMessageBox.warning(self, '错误提示', '无效输入')
            print(reply)

    def _clearpoint(self):
        self.input5.setText('')
        self.input6.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FormulaDemo()
    win.show()
    sys.exit(app.exec_())
