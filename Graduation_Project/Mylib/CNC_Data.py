#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from Mylib.Interface_framework_pane import InterfaceFrameworkPane


class CNCData(QObject):  # 继承QObject类 可以使用信号与槽机制
	""" CNC数据类：存储CNC重要的临时数据"""
	# 数据处理结束信号 主要是指无效数据
	DataStateDone = pyqtSignal(bool)
	# CNC的电源信号传递 参数有电源状态 数据对象,界面对象(父对象)(可以不传递 应为CNCProcess类的父对象与CNCData的父对象一致)
	CNCPowerSignal = pyqtSignal(bool, object)
	# CRT界面的软按键信号 参数为 按钮对象名 按钮内容 数据对象(可不必)
	CRTSoftBtnSignal = pyqtSignal(str, str)
	# CNC急停信号
	CNCEmergencySTOPSignal = pyqtSignal(bool)
	# CNC模式选择信号
	CNCModeChangeSignal = pyqtSignal(str)
	# CNC具有的模式
	CNCModeAll = { 0: 'EDIT', 1: 'MDI', 2: 'MDI', 3: 'JOG',
	               4: 'INC', 5: 'INC', 6: 'INC', 7: 'INC', 8: 'INC',
	               9: 'MDI', 10: 'MEM', 11: 'MEM', 12: 'REF' }  # 其中 4：1，5：10，6：100，7：1000，8：10000
	# CNC在INC模式下的增量倍率
	CNCINCSpeedAll = { 4: '1', 5: '10', 6: '100', 7: '1000', 8: '10000' }
	# CNC具有的进给倍率
	CNCFeedSpeedAll = { 0: '0', 1: '2', 2: '6', 3: '10', 4: '20',
	                    5: '40', 6: '60', 7: '70', 8: '80', 9: '90', 10: '100', 11: '110', 12: '120' }
	# CNC具有的主轴倍率
	CNCSpindleSpeedAll = { 0: '50', 1: '60', 2: '70', 3: '80', 4: '90', 5: '100', 6: '110', 7: '120' }
	# CNC具有的主轴状态 on属于正转 cow属于反转
	CNCSpindleStateAll = { 'Btn_STOP': 'STOP', 'Btn_ON': 'SpindleOn', 'Btn_COW': 'SpindleCOW' }
	# CNC自动加工的所有状态
	CNCAutoProcessStateAll = { 'Btn_Auto_Start': 'Start', 'Btn_Auto_End': 'STOP' }

	# CNC当前的电源按钮状态 默认为False 即电源关闭
	CNCPowerState = False
	# CNC当前的急停按钮状态 默认为True 即急停打开
	CNCEmergencySTOP = True
	# CNC的回零状态 False未回零，True回零
	CNCZeroState = False
	# CNC当前的模式 默认为REF
	CNCNowMode = 'REF'
	# CNC当前的主轴倍率 默认为100 %
	CNCSpindleSpeed = '100'
	# CNC当前的进给倍率 默认为100%
	CNCFeedSpeed = '100'
	# CNC当前INC模式下的速度 默认为0
	CNCINCSpeed = '0'
	# CNC当前机械锁的位置 默认True 即机床锁住
	CNCDRIVEState = True
	# CNC当前程序保护的状态 默认True 即开启程序保护
	CNCPROTECTState = True
	# CNC当前快速进给的状态 默认False 即关闭快速进给
	CNCRAPIDState = False
	# CMC当前的主轴状态 默认为STOP 即主轴停止转动
	CNCSpindleState = 'STOP'
	# CNC当前的空运行状态 默认False 即不空运行
	CNCDRNState = False
	# CNC当前的冷却液状态 默认False 即冷却液关
	CNCCOOLState = False
	# CNC当前的MST状态 默认False 即关闭MST锁
	CNCMSTLOCKState = False
	# CNC当前的SBK单步运行状态 默认False 即关闭单步运行
	CNCSBKState = False
	# CNC当前的SKIP跳步运行状态 默认False 即关闭跳步运行
	CNCSKIPState = False
	# CNC当前M01选择停状态 默认False 即关闭M01选择停
	CNCM01State = False
	# CNC当前的自动换到状态 默认False 即自动换刀停 按下才能打开 松开即False
	CNCTOOLState = False
	# CNC轴选状态 默认False 即未选中 按下才能选中 松开即False
	CNCAxisAPState = False  # A轴正向
	CNCAxisANState = False  # A轴反向
	CNCAxisXPState = False  # x轴正向
	CNCAxisXNState = False  # X轴反向
	CNCAxisYPState = False  # Y轴正向
	CNCAxisYNState = False  # Y轴反向
	CNCAxisZPState = False  # Z轴正向
	CNCAxisZNState = False  # Z轴反向

	# CNC的手轮模式 默认False 即不使用手轮
	CNCMPGState = False
	# CNC的shift状态 默认False 即并未按下shift键
	CNCShiftState = False
	# CNC的CRT界面显示分支 为了简化程序 当切换完全不同的界面时将放弃原界面未保存的修改
	CNCCRTState = 'POS'
	# CRT界面的数量 默认为0 即无界面 但是其值最大为1
	CRTWindowNum = 0
	# CNC的CRT界面软按键信息
	SoftButtonTempInfo = { 'Btn_One': '', 'Btn_Two': '', 'Btn_Three': '', 'Btn_Four': '', 'Btn_Five': '',
	                       'Btn_Six': '', 'Btn_Seven': '', 'Btn_Eight': '', 'Btn_Nine': '', 'Btn_Ten': '' }
	# CRT软按键当前按下的按键 默认没有按下的
	SoftBtnCheckedInfo = { 'Btn_One': False, 'Btn_Two': False, 'Btn_Three': False, 'Btn_Four': False, 'Btn_Five': False,
	                       'Btn_Six': False, 'Btn_Seven': False, 'Btn_Eight': False, 'Btn_Nine': False, 'Btn_Ten': False }
	SoftBtnCheckedInfoBack = { 'Btn_One': False, 'Btn_Two': False, 'Btn_Three': False, 'Btn_Four': False, 'Btn_Five': False,
	                           'Btn_Six': False, 'Btn_Seven': False, 'Btn_Eight': False, 'Btn_Nine': False, 'Btn_Ten': False }
	SoftBtnCheckedInfoGo = { 'Btn_One': False, 'Btn_Two': False, 'Btn_Three': False, 'Btn_Four': False, 'Btn_Five': False,
	                         'Btn_Six': False, 'Btn_Seven': False, 'Btn_Eight': False, 'Btn_Nine': False, 'Btn_Ten': False }
	# CNC的CRT界面软按键信息的back和go 方便两边操作
	SoftButtonTempInfoBack = { 'Btn_One': '', 'Btn_Two': '', 'Btn_Three': '', 'Btn_Four': '', 'Btn_Five': '',
	                           'Btn_Six': '', 'Btn_Seven': '', 'Btn_Eight': '', 'Btn_Nine': '', 'Btn_Ten': '' }
	SoftButtonTempInfoGo = { 'Btn_One': '', 'Btn_Two': '', 'Btn_Three': '', 'Btn_Four': '', 'Btn_Five': '',
	                         'Btn_Six': '', 'Btn_Seven': '', 'Btn_Eight': '', 'Btn_Nine': '', 'Btn_Ten': '' }
	# CRT软按键的按下造成的界面分支
	CRTPageState = ''
	# CRT软按键本身的状态分支 用于back go的软按键的翻页操作 默认空白
	CRTSoftBtnMenu = ''
	# CNC的绝对坐标位置
	CNCPosAbs = { 'X': 1.000, 'Y': 2.000, 'Z': 3.000 }
	# CNC的相对坐标位置
	CNCPosRelative = { 'X': 4.000, 'Y': 5.000, 'Z': 6.000 }
	# CNC的机械坐标位置
	CNCPosMechanical = { 'X': 7.000, 'Y': 8.000, 'Z': 9.000 }
	# CNC报警信息显示 默认False 即无报警信息
	CNCALMState = False

	def __init__(self, parent, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		# InterfaceFrameworkPane
		self.InterfacePane = Pane
		pass

	# 在上电前将控制面板固定按钮 如急停按钮，模式选择，主轴、进给倍率
	def PowerOffInit(self, Pane):
		"""	PowerOffInit(self, InterfaceFrameworkPane)-> None """
		# 设置急停按钮
		Pane.Btn_Emergency_STOP.blockSignals(True)
		Pane.Btn_Emergency_STOP.setChecked(self.CNCEmergencySTOP)
		Pane.Btn_Emergency_STOP.blockSignals(False)
		# 设置模式值 根据默认的模式推断字典相应的键然后设置
		value = list(self.CNCModeAll.keys())[ list(self.CNCModeAll.values()).index(self.CNCNowMode) ]
		Pane.Btn_Mode.blockSignals(True)
		Pane.Btn_Mode.setValue(value)
		Pane.Btn_Mode.blockSignals(False)
		# 设置进给倍率和主轴倍率
		value = list(self.CNCFeedSpeedAll.keys())[ list(self.CNCFeedSpeedAll.values()).index(self.CNCFeedSpeed) ]
		Pane.Btn_Speed.blockSignals(True)
		Pane.Btn_Speed.setValue(value)
		Pane.Btn_Speed.blockSignals(False)
		value = list(self.CNCSpindleSpeedAll.keys())[ list(self.CNCSpindleSpeedAll.values()).index(self.CNCSpindleSpeed) ]
		Pane.Btn_Spindle_Speed.blockSignals(True)
		Pane.Btn_Spindle_Speed.setValue(value)
		Pane.Btn_Spindle_Speed.blockSignals(False)

		Pane.Btn_SHIFT.blockSignals(True)
		Pane.Btn_SHIFT.setChecked(self.CNCShiftState)
		Pane.Btn_SHIFT.blockSignals(False)

		Pane.Btn_RAPID.blockSignals(True)
		Pane.Btn_RAPID.setChecked(self.CNCRAPIDState)
		Pane.Btn_RAPID.blockSignals(False)

		Pane.Btn_COOL.blockSignals(True)
		Pane.Btn_COOL.setChecked(self.CNCCOOLState)
		Pane.Btn_COOL.blockSignals(False)

		Pane.Btn_DRIVE.blockSignals(True)
		Pane.Btn_DRIVE.setChecked(self.CNCDRIVEState)
		Pane.Btn_DRIVE.blockSignals(False)

		Pane.Btn_PROTECT.blockSignals(True)
		Pane.Btn_PROTECT.setChecked(self.CNCPROTECTState)
		Pane.Btn_PROTECT.blockSignals(False)

		Pane.Btn_DRN.blockSignals(True)
		Pane.Btn_DRN.setChecked(self.CNCDRNState)
		Pane.Btn_DRN.blockSignals(False)

		Pane.Btn_MSTLOCK.blockSignals(True)
		Pane.Btn_MSTLOCK.setChecked(self.CNCMSTLOCKState)
		Pane.Btn_MSTLOCK.blockSignals(False)

		Pane.Btn_SBK.blockSignals(True)
		Pane.Btn_SBK.setChecked(self.CNCSBKState)
		Pane.Btn_SBK.blockSignals(False)

		Pane.Btn_SKIP.blockSignals(True)
		Pane.Btn_SKIP.setChecked(self.CNCSKIPState)
		Pane.Btn_SKIP.blockSignals(False)

		Pane.Btn_M01.blockSignals(True)
		Pane.Btn_M01.setChecked(self.CNCM01State)
		Pane.Btn_M01.blockSignals(False)
		pass

	# 在上电后将控制面板的部分按键初始化
	def PowerOnInit(self, Pane):
		# 设置主轴停止按钮按下
		Pane.Btn_STOP.setChecked(True)
		pass

	# control角色类处理,并发送信号
	def CNCDataControl(self, *args):
		Data = args
		# 电源状态处理
		if Data[ 1 ] == 'Btn_Power_ON':
			self.CNCPowerState = True
			self.CRTPageState = '绝对'
			self.CNCPowerSignal.emit(self.CNCPowerState, self)
		if Data[ 1 ] == 'Btn_Power_OFF':
			self.CNCPowerState = False
			self.CNCPowerSignal.emit(self.CNCPowerState, self)
		# 急停按钮处理
		if Data[ 1 ] == 'Btn_Emergency_STOP':
			self.CNCEmergencySTOP = Data[ 2 ]
			self.CNCEmergencySTOPSignal.emit(Data[ 2 ])
		# 模式选择处理
		if Data[ 1 ] == 'Btn_Mode':
			self.CNCNowMode = self.CNCModeAll[ Data[ 2 ] ]
			if self.CNCNowMode == 'INC':
				self.CNCINCSpeed = self.CNCINCSpeedAll[ Data[ 2 ] ]
			else:
				self.CNCINCSpeed = '0'
			self.CNCModeChangeSignal.emit(self.CNCNowMode)
		pass

	# view角色类按键处理，并发送信号
	def CNCDataView(self, *args):
		pass

	# position back go 角色类软按键处理 多用于CRT本身界面切换，并发送信号 role name
	def CNCDataPosition(self, *args):
		if self.CNCCRTState == 'POS':
			if args[ 1 ] != 'Btn_BACK' and args[ 1 ] != 'Btn_GO':
				value = self.SoftButtonTempInfo[ args[ 1 ] ]
				if value == '绝对' or value == '相对' or value == '综合':
					self.CRTPageState = value
				self.CRTSoftBtnSignal.emit(args[ 1 ], value)
			if args[ 1 ] == 'Btn_BACK':
				self.CRTSoftBtnSignal.emit(args[ 0 ], args[ 1 ])
			if args[ 1 ] == 'Btn_GO':
				self.CRTSoftBtnSignal.emit(args[ 0 ], args[ 1 ])
		pass

	# input 角色类按键处理 多是编辑、输入、修改之类的操作，并发送信号
	def CNCDataInput(self, *args):
		pass

	# 该函数负责将传递的参数修改到CNCData类中 如果电源未开 所有信号均不处理
	def CNCDataProcess(self, *args):
		Data = args
		if self.CNCPowerState:
			# 先分角色处理 先处理 control 之后处理 view 再处理position back go 最后处理input角色
			if Data[ 0 ] == 'control':
				self.CNCDataControl(*args)
			if Data[ 0 ] == 'view':
				self.CNCDataView(*args)
			if Data[ 0 ] == 'back' or Data[ 0 ] == 'go' or Data[ 0 ] == 'position':
				self.CNCDataPosition(*args)
			if Data[ 0 ] == 'input':
				self.CNCDataInput(*args)
		elif Data[ 1 ] == 'Btn_Power_ON':
			# 先分角色处理 先处理 control 之后处理 view 再处理position back go 最后处理input角色
			if Data[ 0 ] == 'control':
				self.CNCDataControl(*args)
			if Data[ 0 ] == 'view':
				self.CNCDataView(*args)
			if Data[ 0 ] == 'back' or Data[ 0 ] == 'go' or Data[ 0 ] == 'position':
				self.CNCDataPosition(*args)
			if Data[ 0 ] == 'input':
				self.CNCDataInput(*args)
		else:
			if Data[1] == 'Btn_Emergency_STOP':
				self.CNCEmergencySTOP = Data[ 2 ]
			self.DataStateDone.emit(True)
		pass

	# 接受信号传递过来的参数
	def CNCDataSignalAccept(self, *args):
		# DataAccept = args
		self.CNCDataProcess(*args)
		pass

	def SignalConnectCNCProcess(self, CNCProcess):
		self.CNCPowerSignal.connect(CNCProcess.CNCPowerProcess)
		self.CRTSoftBtnSignal.connect(CNCProcess.CRTSoftBtnProcess)
		self.CNCEmergencySTOPSignal.connect(CNCProcess.EmergencySTOPSlot)
		self.CNCModeChangeSignal.connect(CNCProcess.CNCModeChangeSlot)
		pass

	def SignalConnectCNCPane(self, CNCPane):
		self.DataStateDone.connect(CNCPane.InfoTransStateSlot)
		pass

	pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	window.show()
	test = CNCData()
	# print(test.CNCFeedSpeed)
	# test.CNCFeedSpeed = test.CNCFeedSpeedAll[0]
	# print(test.CNCFeedSpeed)
	sys.exit(app.exec_())
