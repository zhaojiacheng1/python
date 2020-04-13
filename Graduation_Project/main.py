#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from Mylib.Interface_framework_pane import InterfaceFrameworkPane
from Mylib.CNC_Data import CNCData
from Mylib.CRT_Pos_Abs_Pane import CRTPosAbsPane
from Mylib.CNC_Process import CNCProcess

if __name__ == '__main__':
	app = QApplication(sys.argv)
	# CNC控制面板创建
	Main_Pane = InterfaceFrameworkPane()
	Main_Pane.show()
	# 取出CRT界面容器对象 之后创建的显示界面都应当挂载在这个对象上
	CRTWindow = Main_Pane.main_window  # 左右都是类
	# 创建机床存储数据对象
	CNCPaneDate = CNCData(CRTWindow)
	# 创建机床后台处理类
	CNCPaneProcess = CNCProcess(CRTWindow)
	# 上电前控制面板初始化
	CNCPaneDate.PowerOffInit(Main_Pane)

	# 将控制面板的信号传递到后台数据类中
	Main_Pane.SignalConnectCNCData(CNCPaneDate)
	# 将CNCData中的信号连接到处理类CNCProcess中
	CNCPaneDate.SignalConnectCNCProcess(CNCPaneProcess)
	# 将CNCProcess中的信号传递到控制面板类中
	CNCPaneProcess.SignalConnectCNCPane(Main_Pane)
	sys.exit(app.exec_())
