#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from datetime import datetime
from PyQt5.Qt import *
from UILib.CRT_Pos_Absolute import Ui_Form
from Mylib.CNC_Data import CNCData
from Mylib.Window_Pos_Abs import WindowPosAbs
from Mylib.Window_Pos_Rel import WindowPosRel
from Mylib.Window_Pos_Comp import WindowPosComp


class CRTPosAbsPane(QWidget, Ui_Form):
	# 信号告诉控制控制面板 用户面板的点击有效了
	CRTProcessStateDone = pyqtSignal(bool)

	def __init__(self, parent, PaneData, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		# CNCData
		self.PaneData = PaneData
		self.InterfacePane = Pane
		# 初始化时间显示
		self.Lab_Date.setText(datetime.now().strftime('%H:%M:%S'))
		# 设置1s定时器
		self.timerinit()
		# 软按钮初始化
		self.CNCSoftBtnSet(PaneData, PaneData.CRTPageState)
		# 显示软按钮内容
		self.CRTSoftBtnShow(PaneData, '坐标')
		self.PosPaneInit(PaneData)
		# 连接到控制面板的信号
		self.CRTSignalConnectCNCPane(self.InterfacePane)
		# 报警显示初始化
		self.CRTALMshow(self.PaneData)
		self.show()
		self.PaneData.CRTSoftBtnMenu = '坐标'
		# 在创建界面前清空界面
		self.CRTPosWindowDel(self.window_position.children())
		if PaneData.CRTPageState == '绝对':
			windowposition = WindowPosAbs(self.window_position, PaneData)
			windowposition.show()
		if PaneData.CRTPageState == '相对':
			windowposition = WindowPosRel(self.window_position, PaneData)
			windowposition.show()
		if PaneData.CRTPageState == '综合':
			windowposition = WindowPosComp(self.window_position, self.PaneData)
			windowposition.show()
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
				""")
			if self.timernum == 2:
				self.Lab_EMG.setStyleSheet("""
					background-color: rgb(192,192,192);
				""")
		if self.timernum == 2:
			self.timernum = 0
		self.Lab_Date.setText(datetime.now().strftime('%H:%M:%S'))
		# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		pass

	def CRTBtnCheckDel(self, PaneData):
		PaneData.SoftBtnCheckedInfo[ 'Btn_One' ] = False
		PaneData.SoftBtnCheckedInfo[ 'Btn_Two' ] = False
		PaneData.SoftBtnCheckedInfo[ 'Btn_Three' ] = False
		PaneData.SoftBtnCheckedInfo[ 'Btn_Four' ] = False
		PaneData.SoftBtnCheckedInfo[ 'Btn_Five' ] = False
		PaneData.SoftBtnCheckedInfo[ 'Btn_Six' ] = False
		PaneData.SoftBtnCheckedInfo[ 'Btn_Seven' ] = False
		PaneData.SoftBtnCheckedInfo[ 'Btn_Eight' ] = False
		PaneData.SoftBtnCheckedInfo[ 'Btn_Nine' ] = False
		PaneData.SoftBtnCheckedInfo[ 'Btn_Ten' ] = False
		pass

	# 删除所有的CRTPos界面
	def CRTPosWindowDel(self, CRTPoswindowList):
		for i in range(0, len(CRTPoswindowList)):
			CRTPoswindowList[ i ].setParent(None)
		pass

	# 将CNCProcess中的信号传递到CRT界面中
	def SignalConnectCNCProcess(self, CNCProcess):
		CNCProcess.SoftBtnSignal.connect(self.SoftBtnProcess)
		CNCProcess.EmergencySTOPSignal.connect(self.CRTEmergencySTOPSlot)
		CNCProcess.CNCModeChangeSignal.connect(self.CNCModeChangeSlot)
		pass

	def CNCModeChangeSlot(self, state):
		self.Lab_Mode.setText(state)
		self.CRTProcessStateDone.emit(True)
		pass

	def CRTEmergencySTOPSlot(self, state):
		if state == self.PaneData.CNCEmergencySTOP:
			if state:
				self.Lab_EMG.setText('EMG')
			else:
				self.Lab_EMG.setText('***')
				self.Lab_EMG.setStyleSheet("""
					background-color: rgb(192,192,192);
				""")
		self.CRTProcessStateDone.emit(True)
		pass

	def SoftBtnProcess(self, name, value):
		print(name, value)
		if self.PaneData.CRTSoftBtnMenu == '坐标':
			if value == self.PaneData.CRTPageState:
				if value == '绝对':
					self.SoftBtnSetCheck(self.PaneData, value, True)
					self.SoftBtnSetCheck(self.PaneData, '相对', False)
					self.SoftBtnSetCheck(self.PaneData, '综合', False)
					self.CRTPosWindowDel(self.window_position.children())
					windowposition = WindowPosAbs(self.window_position, self.PaneData)
					windowposition.show()
					self.CRTProcessStateDone.emit(True)
				if value == '相对':
					self.SoftBtnSetCheck(self.PaneData, value, True)
					self.SoftBtnSetCheck(self.PaneData, '绝对', False)
					self.SoftBtnSetCheck(self.PaneData, '综合', False)
					self.CRTPosWindowDel(self.window_position.children())
					windowposition = WindowPosRel(self.window_position, self.PaneData)
					windowposition.show()
					self.CRTProcessStateDone.emit(True)
				if value == '综合':
					self.SoftBtnSetCheck(self.PaneData, value, True)
					self.SoftBtnSetCheck(self.PaneData, '相对', False)
					self.SoftBtnSetCheck(self.PaneData, '绝对', False)
					self.CRTPosWindowDel(self.window_position.children())
					windowposition = WindowPosComp(self.window_position, self.PaneData)
					windowposition.show()
					self.CRTProcessStateDone.emit(True)
			if value == 'HNDL':
				# 不处理
				self.CRTProcessStateDone.emit(True)
			if value == '(操作)':
				# 软按钮界面切换 菜单向下进了一级 记录软件状态
				self.PaneData.CRTSoftBtnMenu = '操作'
				# 保存软按键信息 包括显示信息和点击信息
				self.CRTSoftBtnBack(self.PaneData)
				self.CNCSoftBtnSet(self.PaneData, value)
				self.CRTSoftBtnShow(self.PaneData, value)
				self.CRTProcessStateDone.emit(True)
			if value == '':
				self.CRTProcessStateDone.emit(True)
			if value == 'Btn_GO':
				self.CRTProcessStateDone.emit(True)
			if value == 'Btn_BACK':
				self.CRTProcessStateDone.emit(True)
		if self.PaneData.CRTSoftBtnMenu == '操作':
			if value == '':
				self.CRTProcessStateDone.emit(True)
			if value == '预定':
				self.CRTProcessStateDone.emit(True)
			if value == '起源':
				self.CRTProcessStateDone.emit(True)
			if value == '元件:0':
				self.CRTProcessStateDone.emit(True)
			if value == '运行:0':
				self.CRTProcessStateDone.emit(True)
			if value == 'Btn_BACK':
				self.PaneData.CRTSoftBtnMenu = '坐标'
				self.CRTSoftBtnFromBack(self.PaneData)
				self.CRTSoftBtnShow(self.PaneData, '坐标')
				self.CRTProcessStateDone.emit(True)
			if value == 'Btn_GO':
				self.CRTProcessStateDone.emit(True)
		pass

	def PosPaneInit(self, CNCData):
		value = list(CNCData.SoftButtonTempInfo.keys())[ list(CNCData.SoftButtonTempInfo.values()).index(CNCData.CRTPageState) ]
		if value == 'Btn_Six':
			self.Btn_Six.setChecked(True)
			CNCData.SoftBtnCheckedInfo[ value ] = True
		pass

	def CRTSoftBtnFromBack(self, Data):
		# 将当前值赋值保存
		self.CRTSoftBtnGo(Data)
		# 将过去软按钮信息赋值到当前
		Data.SoftButtonTempInfo[ 'Btn_One' ] = Data.SoftButtonTempInfoBack[ 'Btn_One' ]
		Data.SoftButtonTempInfo[ 'Btn_Two' ] = Data.SoftButtonTempInfoBack[ 'Btn_Two' ]
		Data.SoftButtonTempInfo[ 'Btn_Three' ] = Data.SoftButtonTempInfoBack[ 'Btn_Three' ]
		Data.SoftButtonTempInfo[ 'Btn_Four' ] = Data.SoftButtonTempInfoBack[ 'Btn_Four' ]
		Data.SoftButtonTempInfo[ 'Btn_Five' ] = Data.SoftButtonTempInfoBack[ 'Btn_Five' ]
		Data.SoftButtonTempInfo[ 'Btn_Six' ] = Data.SoftButtonTempInfoBack[ 'Btn_Six' ]
		Data.SoftButtonTempInfo[ 'Btn_Seven' ] = Data.SoftButtonTempInfoBack[ 'Btn_Seven' ]
		Data.SoftButtonTempInfo[ 'Btn_Eight' ] = Data.SoftButtonTempInfoBack[ 'Btn_Eight' ]
		Data.SoftButtonTempInfo[ 'Btn_Nine' ] = Data.SoftButtonTempInfoBack[ 'Btn_Nine' ]
		Data.SoftButtonTempInfo[ 'Btn_Ten' ] = Data.SoftButtonTempInfoBack[ 'Btn_Ten' ]
		# 恢复按键点击状况
		Data.SoftBtnCheckedInfo[ 'Btn_One' ] = Data.SoftBtnCheckedInfoBack[ 'Btn_One' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Two' ] = Data.SoftBtnCheckedInfoBack[ 'Btn_Two' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Three' ] = Data.SoftBtnCheckedInfoBack[ 'Btn_Three' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Four' ] = Data.SoftBtnCheckedInfoBack[ 'Btn_Four' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Five' ] = Data.SoftBtnCheckedInfoBack[ 'Btn_Five' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Six' ] = Data.SoftBtnCheckedInfoBack[ 'Btn_Six' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Seven' ] = Data.SoftBtnCheckedInfoBack[ 'Btn_Seven' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Eight' ] = Data.SoftBtnCheckedInfoBack[ 'Btn_Eight' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Nine' ] = Data.SoftBtnCheckedInfoBack[ 'Btn_Nine' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Ten' ] = Data.SoftBtnCheckedInfoBack[ 'Btn_Ten' ]
		self.CRTSoftBtnCheckFromData(Data)
		pass

	def CRTSoftBtnFromGo(self, Data):
		# 将当前值赋值保存
		self.CRTSoftBtnBack(Data)
		# 将前进软按钮信息赋值到当前
		Data.SoftButtonTempInfo[ 'Btn_One' ] = Data.SoftButtonTempInfoGo[ 'Btn_One' ]
		Data.SoftButtonTempInfo[ 'Btn_Two' ] = Data.SoftButtonTempInfoGo[ 'Btn_Two' ]
		Data.SoftButtonTempInfo[ 'Btn_Three' ] = Data.SoftButtonTempInfoGo[ 'Btn_Three' ]
		Data.SoftButtonTempInfo[ 'Btn_Four' ] = Data.SoftButtonTempInfoGo[ 'Btn_Four' ]
		Data.SoftButtonTempInfo[ 'Btn_Five' ] = Data.SoftButtonTempInfoGo[ 'Btn_Five' ]
		Data.SoftButtonTempInfo[ 'Btn_Six' ] = Data.SoftButtonTempInfoGo[ 'Btn_Six' ]
		Data.SoftButtonTempInfo[ 'Btn_Seven' ] = Data.SoftButtonTempInfoGo[ 'Btn_Seven' ]
		Data.SoftButtonTempInfo[ 'Btn_Eight' ] = Data.SoftButtonTempInfoGo[ 'Btn_Eight' ]
		Data.SoftButtonTempInfo[ 'Btn_Nine' ] = Data.SoftButtonTempInfoGo[ 'Btn_Nine' ]
		Data.SoftButtonTempInfo[ 'Btn_Ten' ] = Data.SoftButtonTempInfoGo[ 'Btn_Ten' ]
		# 恢复按键点击状况
		Data.SoftBtnCheckedInfo[ 'Btn_One' ] = Data.SoftButtonTempInfoGo[ 'Btn_One' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Two' ] = Data.SoftButtonTempInfoGo[ 'Btn_Two' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Three' ] = Data.SoftButtonTempInfoGo[ 'Btn_Three' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Four' ] = Data.SoftButtonTempInfoGo[ 'Btn_Four' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Five' ] = Data.SoftButtonTempInfoGo[ 'Btn_Five' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Six' ] = Data.SoftButtonTempInfoGo[ 'Btn_Six' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Seven' ] = Data.SoftButtonTempInfoGo[ 'Btn_Seven' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Eight' ] = Data.SoftButtonTempInfoGo[ 'Btn_Eight' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Nine' ] = Data.SoftButtonTempInfoGo[ 'Btn_Nine' ]
		Data.SoftBtnCheckedInfo[ 'Btn_Ten' ] = Data.SoftButtonTempInfoGo[ 'Btn_Ten' ]
		self.CRTSoftBtnCheckFromData(Data)
		pass

	# 参数 数据对象 想要设置的按键str 想要设置的状态bool
	def SoftBtnSetCheck(self, CNCData, p_str, btncheck):
		value = list(CNCData.SoftButtonTempInfo.keys())[ list(CNCData.SoftButtonTempInfo.values()).index(p_str) ]
		if value == 'Btn_One':
			self.Btn_One.setChecked(btncheck)
			CNCData.SoftBtnCheckedInfo[ value ] = btncheck
		if value == 'Btn_Two':
			self.Btn_Two.setChecked(btncheck)
			CNCData.SoftBtnCheckedInfo[ value ] = btncheck
		if value == 'Btn_Three':
			self.Btn_Three.setChecked(btncheck)
			CNCData.SoftBtnCheckedInfo[ value ] = btncheck
		if value == 'Btn_Four':
			self.Btn_Four.setChecked(btncheck)
			CNCData.SoftBtnCheckedInfo[ value ] = btncheck
		if value == 'Btn_Five':
			self.Btn_Five.setChecked(btncheck)
			CNCData.SoftBtnCheckedInfo[ value ] = btncheck
		if value == 'Btn_Six':
			self.Btn_Six.setChecked(btncheck)
			CNCData.SoftBtnCheckedInfo[ value ] = btncheck
		if value == 'Btn_Seven':
			self.Btn_Seven.setChecked(btncheck)
			CNCData.SoftBtnCheckedInfo[ value ] = btncheck
		if value == 'Btn_Eight':
			self.Btn_Eight.setChecked(btncheck)
			CNCData.SoftBtnCheckedInfo[ value ] = btncheck
		if value == 'Btn_Nine':
			self.Btn_Nine.setChecked(btncheck)
			CNCData.SoftBtnCheckedInfo[ value ] = btncheck
		if value == 'Btn_Ten':
			self.Btn_Ten.setChecked(btncheck)
			CNCData.SoftBtnCheckedInfo[ value ] = btncheck
		pass

	def CNCSoftBtnSet(self, CNCData, p_str):
		if CNCData.CNCCRTState == 'POS':
			if p_str == '绝对' or p_str == '相对' or p_str == '综合':
				CNCData.SoftButtonTempInfo[ 'Btn_One' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Two' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Three' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Four' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Five' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Six' ] = '绝对'
				CNCData.SoftButtonTempInfo[ 'Btn_Seven' ] = '相对'
				CNCData.SoftButtonTempInfo[ 'Btn_Eight' ] = '综合'
				CNCData.SoftButtonTempInfo[ 'Btn_Nine' ] = 'HNDL'
				CNCData.SoftButtonTempInfo[ 'Btn_Ten' ] = '(操作)'
			if p_str == '(操作)':
				CNCData.SoftButtonTempInfo[ 'Btn_One' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Two' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Three' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Four' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Five' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Six' ] = '预定'
				CNCData.SoftButtonTempInfo[ 'Btn_Seven' ] = '起源'
				CNCData.SoftButtonTempInfo[ 'Btn_Eight' ] = ''
				CNCData.SoftButtonTempInfo[ 'Btn_Nine' ] = '元件:0'
				CNCData.SoftButtonTempInfo[ 'Btn_Ten' ] = '运行:0'
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
		if p_str == '坐标':
			self.Btn_BACK.setText('')
			self.Btn_GO.setText('')
		if p_str == '(操作)':
			self.Btn_BACK.setText('<')
			self.Btn_GO.setText('>')
		pass

	# 软按键后退时记录
	def CRTSoftBtnGo(self, Data):
		# 保存按键显示信息
		Data.SoftButtonTempInfoGo[ 'Btn_One' ] = Data.SoftButtonTempInfo[ 'Btn_One' ]
		Data.SoftButtonTempInfoGo[ 'Btn_Two' ] = Data.SoftButtonTempInfo[ 'Btn_Two' ]
		Data.SoftButtonTempInfoGo[ 'Btn_Three' ] = Data.SoftButtonTempInfo[ 'Btn_Three' ]
		Data.SoftButtonTempInfoGo[ 'Btn_Four' ] = Data.SoftButtonTempInfo[ 'Btn_Four' ]
		Data.SoftButtonTempInfoGo[ 'Btn_Five' ] = Data.SoftButtonTempInfo[ 'Btn_Five' ]
		Data.SoftButtonTempInfoGo[ 'Btn_Six' ] = Data.SoftButtonTempInfo[ 'Btn_Six' ]
		Data.SoftButtonTempInfoGo[ 'Btn_Seven' ] = Data.SoftButtonTempInfo[ 'Btn_Seven' ]
		Data.SoftButtonTempInfoGo[ 'Btn_Eight' ] = Data.SoftButtonTempInfo[ 'Btn_Eight' ]
		Data.SoftButtonTempInfoGo[ 'Btn_Nine' ] = Data.SoftButtonTempInfo[ 'Btn_Nine' ]
		Data.SoftButtonTempInfoGo[ 'Btn_Ten' ] = Data.SoftButtonTempInfo[ 'Btn_Ten' ]
		# 保存按键点击状况
		Data.SoftBtnCheckedInfoGo[ 'Btn_One' ] = Data.SoftBtnCheckedInfo[ 'Btn_One' ]
		Data.SoftBtnCheckedInfoGo[ 'Btn_Two' ] = Data.SoftBtnCheckedInfo[ 'Btn_Two' ]
		Data.SoftBtnCheckedInfoGo[ 'Btn_Three' ] = Data.SoftBtnCheckedInfo[ 'Btn_Three' ]
		Data.SoftBtnCheckedInfoGo[ 'Btn_Four' ] = Data.SoftBtnCheckedInfo[ 'Btn_Four' ]
		Data.SoftBtnCheckedInfoGo[ 'Btn_Five' ] = Data.SoftBtnCheckedInfo[ 'Btn_Five' ]
		Data.SoftBtnCheckedInfoGo[ 'Btn_Six' ] = Data.SoftBtnCheckedInfo[ 'Btn_Six' ]
		Data.SoftBtnCheckedInfoGo[ 'Btn_Seven' ] = Data.SoftBtnCheckedInfo[ 'Btn_Seven' ]
		Data.SoftBtnCheckedInfoGo[ 'Btn_Eight' ] = Data.SoftBtnCheckedInfo[ 'Btn_Eight' ]
		Data.SoftBtnCheckedInfoGo[ 'Btn_Nine' ] = Data.SoftBtnCheckedInfo[ 'Btn_Nine' ]
		Data.SoftBtnCheckedInfoGo[ 'Btn_Ten' ] = Data.SoftBtnCheckedInfo[ 'Btn_Ten' ]
		# 清空当前的软按钮点击状态
		Data.SoftBtnCheckedInfo[ 'Btn_One' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Two' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Three' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Four' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Five' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Six' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Seven' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Eight' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Nine' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Ten' ] = False
		# 按照存储数据设置软按钮状态
		self.CRTSoftBtnCheckFromData(Data)
		pass

	# 软按键前进时记录
	def CRTSoftBtnBack(self, Data):
		# 保存按键显示信息
		Data.SoftButtonTempInfoBack[ 'Btn_One' ] = Data.SoftButtonTempInfo[ 'Btn_One' ]
		Data.SoftButtonTempInfoBack[ 'Btn_Two' ] = Data.SoftButtonTempInfo[ 'Btn_Two' ]
		Data.SoftButtonTempInfoBack[ 'Btn_Three' ] = Data.SoftButtonTempInfo[ 'Btn_Three' ]
		Data.SoftButtonTempInfoBack[ 'Btn_Four' ] = Data.SoftButtonTempInfo[ 'Btn_Four' ]
		Data.SoftButtonTempInfoBack[ 'Btn_Five' ] = Data.SoftButtonTempInfo[ 'Btn_Five' ]
		Data.SoftButtonTempInfoBack[ 'Btn_Six' ] = Data.SoftButtonTempInfo[ 'Btn_Six' ]
		Data.SoftButtonTempInfoBack[ 'Btn_Seven' ] = Data.SoftButtonTempInfo[ 'Btn_Seven' ]
		Data.SoftButtonTempInfoBack[ 'Btn_Eight' ] = Data.SoftButtonTempInfo[ 'Btn_Eight' ]
		Data.SoftButtonTempInfoBack[ 'Btn_Nine' ] = Data.SoftButtonTempInfo[ 'Btn_Nine' ]
		Data.SoftButtonTempInfoBack[ 'Btn_Ten' ] = Data.SoftButtonTempInfo[ 'Btn_Ten' ]
		# 保存按键点击状况
		Data.SoftBtnCheckedInfoBack[ 'Btn_One' ] = Data.SoftBtnCheckedInfo[ 'Btn_One' ]
		Data.SoftBtnCheckedInfoBack[ 'Btn_Two' ] = Data.SoftBtnCheckedInfo[ 'Btn_Two' ]
		Data.SoftBtnCheckedInfoBack[ 'Btn_Three' ] = Data.SoftBtnCheckedInfo[ 'Btn_Three' ]
		Data.SoftBtnCheckedInfoBack[ 'Btn_Four' ] = Data.SoftBtnCheckedInfo[ 'Btn_Four' ]
		Data.SoftBtnCheckedInfoBack[ 'Btn_Five' ] = Data.SoftBtnCheckedInfo[ 'Btn_Five' ]
		Data.SoftBtnCheckedInfoBack[ 'Btn_Six' ] = Data.SoftBtnCheckedInfo[ 'Btn_Six' ]
		Data.SoftBtnCheckedInfoBack[ 'Btn_Seven' ] = Data.SoftBtnCheckedInfo[ 'Btn_Seven' ]
		Data.SoftBtnCheckedInfoBack[ 'Btn_Eight' ] = Data.SoftBtnCheckedInfo[ 'Btn_Eight' ]
		Data.SoftBtnCheckedInfoBack[ 'Btn_Nine' ] = Data.SoftBtnCheckedInfo[ 'Btn_Nine' ]
		Data.SoftBtnCheckedInfoBack[ 'Btn_Ten' ] = Data.SoftBtnCheckedInfo[ 'Btn_Ten' ]
		# 清空当前的软按钮点击状态
		Data.SoftBtnCheckedInfo[ 'Btn_One' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Two' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Three' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Four' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Five' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Six' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Seven' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Eight' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Nine' ] = False
		Data.SoftBtnCheckedInfo[ 'Btn_Ten' ] = False
		# 按照存储数据设置软按钮状态
		self.CRTSoftBtnCheckFromData(Data)
		pass

	def CRTSoftBtnCheckFromData(self, Panedata):
		self.Btn_One.setChecked(Panedata.SoftBtnCheckedInfo[ 'Btn_One' ])
		self.Btn_Two.setChecked(Panedata.SoftBtnCheckedInfo[ 'Btn_Two' ])
		self.Btn_Three.setChecked(Panedata.SoftBtnCheckedInfo[ 'Btn_Three' ])
		self.Btn_Four.setChecked(Panedata.SoftBtnCheckedInfo[ 'Btn_Four' ])
		self.Btn_Five.setChecked(Panedata.SoftBtnCheckedInfo[ 'Btn_Five' ])
		self.Btn_Six.setChecked(Panedata.SoftBtnCheckedInfo[ 'Btn_Six' ])
		self.Btn_Seven.setChecked(Panedata.SoftBtnCheckedInfo[ 'Btn_Seven' ])
		self.Btn_Eight.setChecked(Panedata.SoftBtnCheckedInfo[ 'Btn_Eight' ])
		self.Btn_Nine.setChecked(Panedata.SoftBtnCheckedInfo[ 'Btn_Nine' ])
		self.Btn_Ten.setChecked(Panedata.SoftBtnCheckedInfo[ 'Btn_Ten' ])
		pass

	def CRTSignalConnectCNCPane(self, Pane):
		self.CRTProcessStateDone.connect(Pane.InfoTransStateSlot)
		pass

	def CRTALMshow(self, PaneData):
		if PaneData.CNCALMState:
			self.Lab_ALM.setText('ALM')
			self.Lab_ALM.setStyleSheet("""
				background-color:red;
			""")
		else:
			self.Lab_ALM.setText('***')
			self.Lab_ALM.setStyleSheet("""
				background-color:rgb(192,192,192);
			""")
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = CRTPosAbsPane()
	window.show()
	print(window.Lab_Mode.width(), window.Lab_Date.height())
	print(window.widget_9.width(), window.widget_9.height())

	# window.Btn_One.setChecked(True)
	sys.exit(app.exec_())
