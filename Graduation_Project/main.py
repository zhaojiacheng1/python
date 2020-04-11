#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from Mylib.Interface_framework_pane import InterfaceFrameworkPane
from Mylib.CNC_Data import CNCData
from Mylib.CRT_Pos_Abs_Pane import CRTPosAbsPane

if __name__ == '__main__':
	app = QApplication(sys.argv)
	Main_Pane = InterfaceFrameworkPane()
	Main_Pane.show()
	CNCPaneDate = CNCData()
	window = Main_Pane.main_window  # 左右都是类
	CNCPaneDate.PowerOffInit(Main_Pane)
	CRTWindow = CRTPosAbsPane(window)
	CRTWindow.show()
	sys.exit(app.exec_())
