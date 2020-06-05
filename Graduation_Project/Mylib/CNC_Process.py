#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from Mylib.CRT_Pos_Abs_Pane import CRTPosAbsPane
from Mylib.CRT_Prog_Base_Pane import CRTProgBasePane
from Mylib.CRT_Prog_Program_Pane import CRTProgProgramPane
from Mylib.CRT_Message_Pane import CRTMessagePane
from Mylib.CRT_Prog_DIR_Pane import CRTProgDIRPane
from Mylib.CRT_Parameter_Tool_Pane import CRTParameterToolPane


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
	# input输入信号 参数为按下的键值 主要是指几个操作的值 ALTER INSERT DELETE INPUT
	CRTInputSignal = pyqtSignal(str)
	# 输入的临时数据发生变化的信号 包括CAN 和 其他的输入键值 用于显示 参数为bool值 True表示为发生更改
	CRTTemporaryInputDataChange = pyqtSignal(bool)
	# 光标操作信号 参数为对象id名称
	CRTCursorMoveSignal = pyqtSignal(str)
	# 翻页操作信号 参数为对象ID名称
	CNCPageChangeSignal = pyqtSignal(str)

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
	def CRTWindowDel(self, CRTWindowList, CNCData):
		for i in range(0, len(CRTWindowList)):
			CRTWindowList[ i ].SignalDisconnectCNCProcess(self)
			CRTWindowList[ i ].setParent(None)
			CNCData.CRTWindowNum -= 1
		pass

	# 参数中有 state CNCData
	def CNCPowerProcessSlot(self, state, CNCData):
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
		if self.ProcessData.CNCNowMode == 'EDIT' or self.ProcessData.CNCCRTState == 'Parameter':
			if value == 'INPUT' or value == 'DELETE' or value == 'ALTER' or value == 'INSERT':
				# 程序内容改变操作 只负责信号传递 具体操作在对应的程序显示类中
				self.CRTInputSignal.emit(value)
			else:  # 关于单行文本输入框的操作 在CNCProcess中操作，和具体的类分离
				p_str = self.ProcessData.CRTTemporaryInputData
				# 删除单行输入文本框最后一个字符
				if value == 'CAN':
					if len(p_str):
						p_str = p_str[ :-1 ]
				else:
					p_str += value  # 将输入的字符保存在临时字符串中
				# 将临时数据的改变添加到临时字符串中
				self.ProcessData.CRTTemporaryInputData = p_str
				# 临时文本改变信号 用于刷新显示
				self.CRTTemporaryInputDataChange.emit(True)
		pass

	# 处理光标的操作
	def CNCCRTCursorMoveSlot(self, name):
		# 判断当前所处的CRT界面是否有光标可以操作
		if self.ProcessData.CNCCRTState == 'PROG' or self.ProcessData.CNCCRTState == 'PROG_Program' or self.ProcessData.CNCCRTState == 'PROG_DIR' or self.ProcessData.CNCCRTState == 'Parameter':
			self.CRTCursorMoveSignal.emit(name)
		else:
			self.ProcessStateDone.emit(True)
		pass

	# 处理CRT界面翻页操作
	def CNCCRTPageChangeSlot(self, name):
		# print(name)
		# 判断当前所处的CRT界面是否有翻页操作
		if self.ProcessData.CNCCRTState == 'Parameter':
			self.CNCPageChangeSignal.emit(name)
		else:
			self.ProcessStateDone.emit(True)
		pass

	# CRT界面变化
	def CNCCRTChangeSlot(self, value):
		if self.ProcessData.CNCPowerState:
			# 首先清空所有的CRT界面
			window = self.parent().children()
			windowlist = ()
			windowlist += self.CNCCRTWindowList(window, self.ProcessData)
			self.CRTWindowDel(windowlist, self.ProcessData)
			# self.CRTWindowSignalDel()
			# print('CRT界面:', self.parent().children())
			if value == self.ProcessData.CNCCRTState and value == 'POS' and self.ProcessData.CRTWindowNum == 0:
				# 创建POS位置界面
				window = CRTPosAbsPane(self.parent(), self.ProcessData, self.InterfacePane)
				# 连接CNCProcess类的信号
				window.SignalConnectCNCProcess(self)
				self.ProcessData.CRTWindowNum += 1  # CRT窗口数量加1
				self.ProcessStateDone.emit(True)
			if value == self.ProcessData.CNCCRTState and value == 'PROG' and self.ProcessData.CRTWindowNum == 0:
				# 创建PROG G代码编辑器界面
				window = CRTProgBasePane(self.parent(), self.ProcessData, self.InterfacePane)
				# 连接CNCProcess类的信号
				window.SignalConnectCNCProcess(self)
				# print(window.programwindow.width(), window.programwindow.height())
				self.ProcessData.CRTWindowNum += 1  # CRT窗口数量加1
				self.ProcessStateDone.emit(True)
			# print(window.window_position.width(), window.window_position.height())
			if value == self.ProcessData.CNCCRTState and value == 'PROG_Program' and self.ProcessData.CRTWindowNum == 0:
				# 创建PROG Program G代码编辑器界面
				window = CRTProgProgramPane(self.parent(), self.ProcessData, self.InterfacePane)
				# 连接CNCProcess类的信号
				window.SignalConnectCNCProcess(self)
				self.ProcessData.CRTWindowNum += 1  # CRT窗口数量加1
				self.ProcessStateDone.emit(True)
				print(window.programwindow.width(), window.programwindow.height())
			if value == self.ProcessData.CNCCRTState and value == 'Message' and self.ProcessData.CRTWindowNum == 0:
				# 创建Message 消息显示界面
				window = CRTMessagePane(self.parent(), self.ProcessData, self.InterfacePane)
				# 连接CNCProcess类的信号
				window.SignalConnectCNCProcess(self)
				self.ProcessData.CRTWindowNum += 1  # CRT窗口数量加1
				self.ProcessStateDone.emit(True)
			# print(window.window_message.width(), window.window_message.height())
			if value == self.ProcessData.CNCCRTState and value == 'PROG_DIR' and self.ProcessData.CRTWindowNum == 0:
				# 创建DIR界面 程序文件界面
				window = CRTProgDIRPane(self.parent(), self.ProcessData, self.InterfacePane)
				# 连接CNCProcess类的信号
				window.SignalConnectCNCProcess(self)
				self.ProcessData.CRTWindowNum += 1
				self.ProcessStateDone.emit(True)
			# print(window.programdirwindow.width(), window.programdirwindow.height())
			if value == self.ProcessData.CNCCRTState and value == 'Parameter' and self.ProcessData.CRTWindowNum == 0:
				# 创建刀补参数设置界面
				window = CRTParameterToolPane(self.parent(), self.ProcessData, self.InterfacePane)
				# 连接CNCProcess类信号
				window.SignalConnectCNCProcess(self)
				self.ProcessData.CRTWindowNum += 1
				self.ProcessStateDone.emit(True)
		pass

	def CRTSoftBtnProcessSlot(self, name, value):
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
