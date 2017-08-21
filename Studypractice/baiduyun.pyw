#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Junki

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future.builtins import *

import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QDialog, QLineEdit, QTextBrowser,
                             QVBoxLayout)
import fmovice


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("输入关键词并按Enter键,等待10秒")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.lineedit)
        layout.addWidget(self.browser)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("百度云资源搜索")

    def search_(self, txt):
        result = fmovice.Search_Movice(txt)
        return result

    def updateUi(self):
        text = self.lineedit.text()
        try:
            self.browser.append("{0}".format(self.search_(text)))
        except:
            self.browser.append("<font color=red>{0} is invalid!</font>".format(text))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
