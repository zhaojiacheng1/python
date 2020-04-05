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
        self.resize(500, 500)  # 界面的初始尺寸
        self.CRT_width = int(self.width() / 2)
        self.CRT_height = int(self.height() / 2)
        self.CRT_wmarign = int(self.CRT_width / 20)
        self.CRT_hmarign = int(self.CRT_height / 20)
        self.Button_width = int(self.width() / 10)
        self.Button_height = int(self.height() / 20)
        self.Button_wmarign = int(self.Button_width / 4)
        self.Button_hmarign = int(self.Button_height / 4)
        self.CRT = QWidget(self)
        self.mode_btn = QPushButton(self)
        self.file_btn = QPushButton(self)
        self.change_btn = QPushButton(self)
        self.setup_ui()

    def setup_ui(self):  # 软件界面初始化
        self.setWindowTitle('Fanuc数控系统HMI')  # 设置窗口界面
        # print(self.width(), self.height())
        self.CRT.resize(self.CRT_width, self.CRT_height)
        self.CRT.setStyleSheet('background-color:balck;')
        self.CRT.move(0, 0)
        self.mode_btn.resize(self.Button_width, self.Button_height)
        self.mode_btn.move(0, self.CRT_height + self.CRT_hmarign)
        self.file_btn.resize(self.Button_width, self.Button_height)
        self.file_btn.move(self.CRT_width + self.CRT_wmarign, 0)
        self.change_btn.resize(self.Button_width, self.Button_height)
        self.change_btn.move(self.file_btn.x() + self.Button_width + self.Button_wmarign, 0)

    def resizeEvent(self, evt):
        # 根据界面尺寸的变化自动重新计算各个控件的大小和位置
        self.CRT_width = int(self.width() / 2)
        self.CRT_height = int(self.height() / 2)
        self.CRT_wmarign = int(self.CRT_width / 20)
        self.CRT_hmarign = int(self.CRT_height / 20)
        self.Button_width = int(self.width() / 10)
        self.Button_height = int(self.height() / 20)
        self.Button_wmarign = int(self.Button_width / 4)
        self.Button_hmarign = int(self.Button_height / 4)
        print(self.CRT_wmarign, self.CRT_hmarign, self.Button_wmarign, self.Button_hmarign)
        self.CRT.resize(self.CRT_width, self.CRT_height)
        self.mode_btn.resize(self.Button_width, self.Button_height)
        self.mode_btn.move(0, self.CRT_height + self.CRT_hmarign)
        self.file_btn.resize(self.Button_width, self.Button_height)
        self.file_btn.move(self.CRT_width + self.CRT_wmarign, 0)
        self.change_btn.resize(self.Button_width, self.Button_height)
        self.change_btn.move(self.file_btn.x() + self.Button_width + self.Button_wmarign, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Project_ui()

    window.show()
    sys.exit(app.exec_())
