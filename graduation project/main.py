#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from Mylib.Interface_framework_pane import InterfaceFrameworkPane

if __name__ == '__main__':
	app = QApplication(sys.argv)
	Main_Pane = InterfaceFrameworkPane()
	Main_Pane.show()
	window = Main_Pane.main_window  # 左右都是类
	sys.exit(app.exec_())
