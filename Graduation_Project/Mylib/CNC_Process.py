#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from Mylib.CRT_Pos_Abs_Pane import CRTPosAbsPane
from Mylib.CRT_Prog_Base_Pane import CRTProgBasePane
from Mylib.CRT_Prog_Program_Pane import CRTProgProgramPane
from Mylib.CRT_Message_Pane import CRTMessagePane


class CNCProcess(QObject):
	# 信号告诉控制控制面板 用户面板的点击有效了
	ProcessStateDone = pyqtSignal(bool)
	# 传递软按钮按下的信息 按钮对象名 按下的内容
	SoftBtnSignal = pyqtSignal(str, str)
	# 急停信号
	EmergencySTOPSignal = pyqtSignal(bool)
	# CNC模式改变信号
	CNCModeChangeSignal = pyqtSignal(str)
	# 进给倍率设置
	CNCFeedSpeedSignal = pyqtSignal(str)
	# 主轴倍率信号
	CNCSpindleSpeedSignal = pyqtSignal(str)

	def __init__(self, parent, Pane, Data, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		# InterfaceFrameworkPane
		self.InterfacePane = Pane
		self.ProcessData = Data
		pass

	# 轴选信号处理
	def CNCAxisSlot(self, name, state):
		print(name, state)
		self.ProcessStateDone.emit(True)
		pass

	def CNCSpindleSpeedSlot(self, value):
		self.CNCSpindleSpeedSignal.emit(value)
		pass

	def CNCFeedSpeedSlot(self, value):
		self.CNCFeedSpeedSignal.emit(value)
		pass

	def CNCModeChangeSlot(self, mode):
		self.CNCModeChangeSignal.emit(mode)
		pass

	# 筛选出所有的CRT界面 严格说是非CNCData和CNCProcess类
	def CNCCRTWindowList(self, childlist, CNCData):
		window_list = ()
		for i in range(0, len(childlist)):
			if type(childlist[ i ]) != type(CNCData) and type(childlist[ i ]) != type(self):
				window_list += (childlist[ i ],)
		# print(window_list)
		return window_list
		pass

	# 删除所有的CRT界面
	def CRTWindowDel(self, CRTwindowList, CNCData):
		for i in range(0, len(CRTwindowList)):
			CRTwindowList[ i ].setParent(None)
			CNCData.CRTWindowNum -= 1
		pass

	# 参数中有 state CNCData
	def CNCPowerProcess(self, state, CNCData):
		if state != CNCData.CNCPowerState:
			return None
		if state:
			if CNCData.CNCCRTState == 'POS' and CNCData.CRTWindowNum == 0:
				window = CRTPosAbsPane(self.parent(), CNCData, self.InterfacePane)
				window.SignalConnectCNCProcess(self)
				CNCData.CRTWindowNum += 1  # CRT窗口数量加1
				self.ProcessStateDone.emit(True)
			else:
				# 重复点击电源开不处理
				self.ProcessStateDone.emit(True)
		else:
			window = self.parent().children()
			windowlist = ()
			windowlist += self.CNCCRTWindowList(window, CNCData)
			self.CRTWindowDel(windowlist, CNCData)
			self.ProcessStateDone.emit(True)
		pass

	def CNCInputSlot(self, value):

		pass

	def CNCCRTChangeSlot(self, value):
		if self.ProcessData.CNCPowerState:
			# 首先清空所有的CRT界面
			window = self.parent().children()
			windowlist = ()
			windowlist += self.CNCCRTWindowList(window, self.ProcessData)
			self.CRTWindowDel(windowlist, self.ProcessData)
			if value == self.ProcessData.CNCCRTState and value == 'POS' and self.ProcessData.CRTWindowNum == 0:
				window = CRTPosAbsPane(self.parent(), self.ProcessData, self.InterfacePane)
				# 连接CNCProcess类的信号
				window.SignalConnectCNCProcess(self)
				self.ProcessData.CRTWindowNum += 1  # CRT窗口数量加1
				self.ProcessStateDone.emit(True)
			if value == self.ProcessData.CNCCRTState and value == 'PROG' and self.ProcessData.CRTWindowNum == 0:
				window = CRTProgBasePane(self.parent(), self.ProcessData, self.InterfacePane)
				# 连接CNCProcess类的信号
				window.SignalConnectCNCProcess(self)
				# print(window.programwindow.width(), window.programwindow.height())
				self.ProcessData.CRTWindowNum += 1  # CRT窗口数量加1
				self.ProcessStateDone.emit(True)
			# print(window.window_position.width(), window.window_position.height())
			if value == self.ProcessData.CNCCRTState and value == 'PROG_Program' and self.ProcessData.CRTWindowNum == 0:
				window = CRTProgProgramPane(self.parent(), self.ProcessData, self.InterfacePane)
				# 连接CNCProcess类的信号
				window.SignalConnectCNCProcess(self)
				self.ProcessData.CRTWindowNum += 1  # CRT窗口数量加1
				self.ProcessStateDone.emit(True)
			if value == self.ProcessData.CNCCRTState and value == 'Message' and self.ProcessData.CRTWindowNum == 0:
				window = CRTMessagePane(self.parent(), self.ProcessData, self.InterfacePane)
				# 连接CNCProcess类的信号
				window.SignalConnectCNCProcess(self)
				self.ProcessData.CRTWindowNum += 1  # CRT窗口数量加1
				self.ProcessStateDone.emit(True)
		# print(window.window_message.width(), window.window_message.height())
		pass

	def CRTSoftBtnProcess(self, name, value):
		# 将软信号传递到CRT界面中去
		self.SoftBtnSignal.emit(name, value)
		pass

	def EmergencySTOPSlot(self, state):
		self.EmergencySTOPSignal.emit(state)
		pass

	def SignalConnectCNCPane(self, InterfaceFrameworkPane):
		self.ProcessStateDone.connect(InterfaceFrameworkPane.InfoTransStateSlot)
		pass

	pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = CNCProcess()
	window.show()
	sys.exit(app.exec_())
