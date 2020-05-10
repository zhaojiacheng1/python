#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from datetime import datetime
from PyQt5.Qt import *
from UILib.CRT_PROG_DIR import Ui_Form
from Mylib.CNC_Data import CNCData
from Mylib.Window_ProgramTextEdit import WindowProgramTextEdit
from Mylib.Window_Prog_ProgramDir import WindowProgProgramDir


class CRTProgDIRPane(QWidget, Ui_Form):
	# 信号告诉控制控制面板 用户面板的点击有效了
	CRTProcessStateDone = pyqtSignal(bool)
	# 输入文本框文本变换信号 参数为bool型数据 True时表示数据发生改变
	CRTTemporaryInputDataSignal = pyqtSignal(bool)
	# 程序数据变化信号 参数为str型数据 表示是具体的操作
	CRTProgramTextChange = pyqtSignal(str)
	# 程序界面的光标移动操作信号 参数为对象的id名称
	CRTProgramCursorMoveSignal = pyqtSignal(str)
	# 程序界面内部不同的界面之间传递信息的信号 该信号用于界面之间的信息回环 参数为str数据
	CRTWindowMessageExchangeSignal = pyqtSignal(str)
	# CRT界面软件back 和 go的点击情况
	SoftBtnCheckedInfoBack = { 'Btn_One': False, 'Btn_Two': False, 'Btn_Three': False, 'Btn_Four': False, 'Btn_Five': False,
	                           'Btn_Six': False, 'Btn_Seven': False, 'Btn_Eight': False, 'Btn_Nine': False, 'Btn_Ten': False }
	SoftBtnCheckedInfoGo = { 'Btn_One': False, 'Btn_Two': False, 'Btn_Three': False, 'Btn_Four': False, 'Btn_Five': False,
	                         'Btn_Six': False, 'Btn_Seven': False, 'Btn_Eight': False, 'Btn_Nine': False, 'Btn_Ten': False }
	# CNC的CRT界面软按键信息的back和go 方便两边操作
	SoftButtonTempInfoBack = { 'Btn_One': '', 'Btn_Two': '', 'Btn_Three': '', 'Btn_Four': '', 'Btn_Five': '',
	                           'Btn_Six': '', 'Btn_Seven': '', 'Btn_Eight': '', 'Btn_Nine': '', 'Btn_Ten': '' }
	SoftButtonTempInfoGo = { 'Btn_One': '', 'Btn_Two': '', 'Btn_Three': '', 'Btn_Four': '', 'Btn_Five': '',
	                         'Btn_Six': '', 'Btn_Seven': '', 'Btn_Eight': '', 'Btn_Nine': '', 'Btn_Ten': '' }

	def __init__(self, parent, PaneData, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		# CNCData
		self.PaneData = PaneData
		self.InterfacePane = Pane
		self.PaneInit(PaneData)
		self.show()
		pass

	def PaneInit(self, PaneData):
		# 初始化时间显示
		self.Lab_Date.setText(datetime.now().strftime('%H:%M:%S'))
		# 设置1s定时器
		self.timerinit()
		# 软按键初始化
		self.CNCSoftBtnSet(PaneData, 'DIR')
		# 显示软按钮内容
		self.CRTSoftBtnShow(PaneData, 'DIR')
		value = list(PaneData.SoftButtonTempInfo.keys())[ list(PaneData.SoftButtonTempInfo.values()).index('DIR') ]
		if value == 'Btn_Seven':
			self.Btn_Seven.setChecked(True)
			PaneData.SoftBtnCheckedInfo[ value ] = True
		# 连接到控制面板的信号
		self.CRTSignalConnectCNCPane(self.InterfacePane)
		# 报警显示初始化
		self.CRTALMshow(self.PaneData)
		self.PaneData.CRTSoftBtnMenu = 'DIR'
		# 初始化模式选择信息
		self.Lab_Mode.setText(PaneData.CNCNowMode)
		# 挂在文件信息显示窗口
		windowprogramdir = WindowProgProgramDir(self.programdirwindow, self.PaneData, self)
		windowprogramdir.show()
		# 判断当前机床是所处的模式 然后创建编辑框
		if self.PaneData.CNCNowMode == 'EDIT':
			windowprogramedit = WindowProgramTextEdit(self.Lab_ProgramEdit, self.PaneData, self)
			windowprogramedit.show()
		pass

	def timerinit(self):
		self.timer_id = self.startTimer(1000)  # 设置1s定时器
		self.timernum = 0
		pass

	def timerEvent(self, evt):
		self.timernum += 1
		if self.PaneData.CNCEmergencySTOP:
			if self.timernum == 1:
				self.Lab_EMG.setStyleSheet("""
					background-color: red;
					border-top: 2px solid white;
					border-left: 2px solid white;
					border-right: 2px solid black;
					border-bottom: 2px solid rgb(140,140,140);
				""")
			if self.timernum == 2:
				self.Lab_EMG.setStyleSheet("""
					background-color: rgb(192,192,192);
					border-top: 2px solid white;
					border-left: 2px solid white;
					border-right: 2px solid black;
					border-bottom: 2px solid rgb(140,140,140);
				""")
		if self.timernum == 2:
			self.timernum = 0
		self.Lab_Date.setText(datetime.now().strftime('%H:%M:%S'))
		pass

	def WindowMessageExchangeSlot(self, value):
		if self.PaneData.CNCCRTState != 'PROG_DIR':
			return None
		print('信息总站接受到的数据:', value)
		pass

	def CRTSpindleSpeedSlot(self, value):
		if self.PaneData.CNCCRTState != 'PROG_DIR':
			return None
		if value == self.PaneData.CNCSpindSpeed:
			self.CRTProcessStateDone.emit(True)
		pass

	def CRTFeedSpeedSlot(self, value):
		if self.PaneData.CNCCRTState != 'PROG_DIR':
			return None
		if value == self.PaneData.CNCFeedSpeed:
			self.CRTProcessStateDone.emit(True)
		pass

	# 将CNCProcess中的信号传递到CRT界面中
	def SignalConnectCNCProcess(self, CNCProcess):
		CNCProcess.SoftBtnSignal.connect(self.SoftBtnProcessSlot)
		CNCProcess.EmergencySTOPSignal.connect(self.CRTEmergencySTOPSlot)
		CNCProcess.CNCModeChangeSignal.connect(self.CNCModeChangeSlot)
		CNCProcess.CNCFeedSpeedSignal.connect(self.CRTFeedSpeedSlot)
		CNCProcess.CNCSpindleSpeedSignal.connect(self.CRTSpindleSpeedSlot)
		CNCProcess.CRTInputSignal.connect(self.CRTInputSlot)
		CNCProcess.CRTTemporaryInputDataChange.connect(self.CRTTemporaryInputDataSlot)
		CNCProcess.CRTCursorMoveSignal.connect(self.CRTCursorMoveSlot)
		pass

	def SignalDisconnectCNCProcess(self, CNCProcess):
		CNCProcess.SoftBtnSignal.disconnect(self.SoftBtnProcessSlot)
		CNCProcess.EmergencySTOPSignal.disconnect(self.CRTEmergencySTOPSlot)
		CNCProcess.CNCModeChangeSignal.disconnect(self.CNCModeChangeSlot)
		CNCProcess.CNCFeedSpeedSignal.disconnect(self.CRTFeedSpeedSlot)
		CNCProcess.CNCSpindleSpeedSignal.disconnect(self.CRTSpindleSpeedSlot)
		CNCProcess.CRTInputSignal.disconnect(self.CRTInputSlot)
		CNCProcess.CRTTemporaryInputDataChange.disconnect(self.CRTTemporaryInputDataSlot)
		CNCProcess.CRTCursorMoveSignal.disconnect(self.CRTCursorMoveSlot)
		self.CRTSignalDisconnectCNCPane(self.InterfacePane)
		pass

	# 界面光标信号处理
	def CRTCursorMoveSlot(self, name):
		if self.PaneData.CNCCRTState != 'PROG_DIR':
			return None
		self.CRTProgramCursorMoveSignal.emit(name)
		self.CRTProcessStateDone.emit(True)
		pass

	# 当行输入文本框的数据发生改变 相应的界面应该调整文本显示
	def CRTTemporaryInputDataSlot(self, state):
		if self.PaneData.CNCCRTState != 'PROG_DIR':
			return None
		if state:
			self.CRTTemporaryInputDataSignal.emit(True)
		pass

	def CRTInputSlot(self, value):
		if self.PaneData.CNCCRTState != 'PROG_DIR':
			return None
		self.CRTProgramTextChange.emit(value)
		pass

	def CNCModeChangeSlot(self, state):
		if self.PaneData.CNCCRTState != 'PROG_DIR':
			return None
		self.Lab_Mode.setText(state)
		if state == 'EDIT':
			self.CRTProgEditWindowDel(self.Lab_ProgramEdit.children())
			windowprogramedit = WindowProgramTextEdit(self.Lab_ProgramEdit, self.PaneData, self)
			windowprogramedit.show()
		elif state == 'MDI':
			self.CRTProgEditWindowDel(self.Lab_ProgramEdit.children())
		else:
			self.CRTProgEditWindowDel(self.Lab_ProgramEdit.children())
		self.CRTProcessStateDone.emit(True)
		pass

	# 删除所有的CRTProgramEdit界面
	def CRTProgEditWindowDel(self, CRTProgWindowList):
		for i in range(0, len(CRTProgWindowList)):
			CRTProgWindowList[ i ].SignalDisconnectSlot(self)
			CRTProgWindowList[ i ].setParent(None)
		pass

	def CRTEmergencySTOPSlot(self, state):
		if self.PaneData.CNCCRTState != 'PROG_DIR':
			return None
		if state == self.PaneData.CNCEmergencySTOP:
			if state:
				self.Lab_EMG.setText('EMG')
			else:
				self.Lab_EMG.setText('***')
				self.Lab_EMG.setStyleSheet("""
					background-color: rgb(192,192,192);
					border-top: 2px solid white:
					border-left: 2px solid white;
					border-right: 2px solid black;
					border-bottom: 2px solid rgb(140,140,140);
				""")
		self.CRTProcessStateDone.emit(True)
		pass

	def SoftBtnProcessSlot(self, name, value):
		if self.PaneData.CNCCRTState != 'PROG_DIR':
			return None
		print(name, value)
		if self.PaneData.CRTSoftBtnMenu == 'DIR':
			if value == '操作':
				# 不处理
				self.CRTProcessStateDone.emit(True)
			if value == 'DIR':
				self.CRTProcessStateDone.emit(True)
			if value == '':
				self.CRTProcessStateDone.emit(True)
			if value == 'Btn_BACK':
				self.CRTProcessStateDone.emit(True)
			if value == 'Btn_GO':
				self.CRTProcessStateDone.emit(True)
		pass

	def CNCSoftBtnSet(self, CNCData, p_str):
		if CNCData.CNCCRTState == 'PROG_DIR':
			if p_str == 'DIR':
				CNCData.SoftButtonTempInfo[ 'Btn_One' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Two' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Three' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Four' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Five' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Six' ] = '程序'
				CNCData.SoftButtonTempInfo[ 'Btn_Seven' ] = 'DIR'
				CNCData.SoftButtonTempInfo[ 'Btn_Eight' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Nine' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Ten' ] = '操作'
		pass

	def CRTSoftBtnShow(self, CNCData, p_str):
		self.Btn_One.setText(CNCData.SoftButtonTempInfo[ 'Btn_One' ])
		self.Btn_Two.setText(CNCData.SoftButtonTempInfo[ 'Btn_Two' ])
		self.Btn_Three.setText(CNCData.SoftButtonTempInfo[ 'Btn_Three' ])
		self.Btn_Four.setText(CNCData.SoftButtonTempInfo[ 'Btn_Four' ])
		self.Btn_Five.setText(CNCData.SoftButtonTempInfo[ 'Btn_Five' ])
		self.Btn_Six.setText(CNCData.SoftButtonTempInfo[ 'Btn_Six' ])
		self.Btn_Seven.setText(CNCData.SoftButtonTempInfo[ 'Btn_Seven' ])
		self.Btn_Eight.setText(CNCData.SoftButtonTempInfo[ 'Btn_Eight' ])
		self.Btn_Nine.setText(CNCData.SoftButtonTempInfo[ 'Btn_Nine' ])
		self.Btn_Ten.setText(CNCData.SoftButtonTempInfo[ 'Btn_Ten' ])
		if p_str == 'DIR':
			self.Btn_BACK.setText('')
			self.Btn_GO.setText('')
		pass

	def CRTSignalConnectCNCPane(self, Pane):
		self.CRTProcessStateDone.connect(Pane.InfoTransStateSlot)
		pass

	def CRTSignalDisconnectCNCPane(self, Pane):
		self.CRTProcessStateDone.disconnect(Pane.InfoTransStateSlot)
		pass

	def CRTALMshow(self, PaneData):
		if PaneData.CNCALMState:
			self.Lab_ALM.setText('ALM')
			self.Lab_ALM.setStyleSheet("""
				background-color: red;
				border-left: 2px sloid white;
				border-top: 2px solid white;
				border-right: 2px solid black;
				border-bottom: 2px solid rgb(140,140,140);
			""")
		else:
			self.Lab_ALM.setText('***')
			self.Lab_ALM.setStyleSheet("""
				background-color: rgb(192,192,192);
				border-left: 2px solid white;
				border-top: 2px solid white;
				border-right: 2px solid black;
				border-bottom: 2px solid rgb(140,140,140);
			""")
		pass
