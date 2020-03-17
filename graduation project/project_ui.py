#!/usr/bin/python3 
# -*- coding: utf-8 -*-

# 项目软件的UI界面

import sys
from PyQt5.Qt import *


# 1、需要解决窗口自适应问题：1、固定全屏，只保留最小化和关闭
#                        2、锁定长宽比，所有控件大小，位置随窗口改变重新计算
class Project_ui(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):  # 软件界面初始化
        self.setWindowTitle('Fanuc数控系统HMI')  # 设置窗口界面


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Project_ui()

    window.show()
    sys.exit(app.exec_())
