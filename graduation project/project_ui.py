#!/usr/bin/python3 
# -*- coding: utf-8 -*-

'''
项目软件的UI界面
'''

import sys
#导入系统
from PyQt5.Qt import *

class project_ui(QWidget):
    def __init__(self):
        super.__init__()
    def setup_ui(self):  #软件界面初始化
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)

    sys.exit(app.exec_())
