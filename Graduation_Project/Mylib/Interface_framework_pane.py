#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from UILib.Interface_framework import Ui_Form


# from Mylib.CNC_Data import CNCData


class InterfaceFrameworkPane(QWidget, Ui_Form):
	# 普通信息传递信号，只包含role name两部分
	InfoTransBtnClick = pyqtSignal(str, str)
	# 可以实现自保持状态的按钮，包含role，name，state（按钮处于的状态）
	InfoTransBtnCheck = pyqtSignal(str, str, bool)
	# 不能自保持，但是需要实现用户长按的功能，包含role，name，state（按钮是否处于按下的状态）
	InfoTransBtnKeepState = pyqtSignal(str, str, bool)
	# 旋转开关选择的键值传递 包含role，name，value（键值）
	InfoTransDial = pyqtSignal(str, str, int)

	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		# 设置面板可以发送信号状态位，默认值为True 即可以发送信号 当其值为False时不可发送信号 用户点击按钮无效
		self.InfoTransState = True
		pass

	# 普通按钮的点击信号
	def get_keys(self, role, name):
		"""
		:param role: str
		:param name: str
		:return: None
		"""
		# print(role, name)
		# 信号先发送role，后发送name
		if self.InfoTransState:
			# 这行代码必须放在发送信号之前 信号的发送时间太久，如果放在之后会发生 置True在置False之前
			self.InfoTransState = False
			print(self.InfoTransState, '1')
			self.InfoTransBtnClick.emit(role, name)
		pass

	# 点击状态保存的按钮
	def get_check_keys(self, role, name, state):
		"""
		:param role: str
		:param name: str
		:param state: bool
		:return: None
		"""
		# print(role, name, state)
		if self.InfoTransState:
			self.InfoTransState = False
			print(self.InfoTransState, '1')
			self.InfoTransBtnCheck.emit(role, name, state)
		pass

	# 表盘控件的信号
	def get_dial_value(self, role, name, value):
		"""
		:param role: str
		:param name: str
		:param value: int
		:return: None
		"""
		# print(role, name, value)
		if self.InfoTransState:
			self.InfoTransState = False
			print(self.InfoTransState, '1')
			self.InfoTransDial.emit(role, name, value)
		pass

	# 支持长按的按钮
	def get_keep_keys(self, role, name, state):
		"""
		:param role: str
		:param name: str
		:param state: bool
		:return: None
		"""
		# print(role, name, state)
		if self.InfoTransState:
			self.InfoTransState = False
			print(self.InfoTransState, '1')
			self.InfoTransBtnKeepState.emit(role, name, state)
		pass

	def SignalConnectCNCData(self, CNCData):
		self.InfoTransBtnClick.connect(CNCData.CNCDataSignalAccept)
		self.InfoTransBtnCheck.connect(CNCData.CNCDataSignalAccept)
		self.InfoTransBtnKeepState.connect(CNCData.CNCDataSignalAccept)
		self.InfoTransDial.connect(CNCData.CNCDataSignalAccept)
		pass

	def InfoTransStateSlot(self, state):
		self.InfoTransState = state
		print(self.InfoTransState, '2')
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = InterfaceFrameworkPane()
	window.show()
	# cb = CNCData(window)

	sys.exit(app.exec_())
