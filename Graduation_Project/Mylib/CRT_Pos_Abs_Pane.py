#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
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
		self.CNCSoftBtnSet(PaneData)
		self.CRTSoftBtnShow(PaneData)
		self.PosPaneInit(PaneData)
		self.CRTSignalConnectCNCPane(self.InterfacePane)
		self.CRTALMshow(self.PaneData)
		self.show()
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

	# 删除所有的CRTPos界面
	def CRTPosWindowDel(self, CRTPoswindowList):
		for i in range(0, len(CRTPoswindowList)):
			CRTPoswindowList[ i ].setParent(None)
		pass

	# 将CNCProcess中的信号传递到CRT界面中
	def SignalConnectCNCProcess(self, CNCProcess):
		CNCProcess.SoftBtnSignal.connect(self.SoftBtnProcess)
		pass

	def SoftBtnProcess(self, name, value):
		print(name, value)
		if value == self.PaneData.CRTPageState:
			self.CRTPosWindowDel(self.window_position.children())
			if value == '绝对':
				self.Btn_Six.setChecked(True)
				self.Btn_Seven.setChecked(False)
				self.Btn_Eight.setChecked(False)
				windowposition = WindowPosAbs(self.window_position, self.PaneData)
				windowposition.show()
				self.CRTProcessStateDone.emit(True)
			if value == '相对':
				self.Btn_Six.setChecked(False)
				self.Btn_Seven.setChecked(True)
				self.Btn_Eight.setChecked(False)
				windowposition = WindowPosRel(self.window_position, self.PaneData)
				windowposition.show()
				self.CRTProcessStateDone.emit(True)
			if value == '综合':
				self.Btn_Six.setChecked(False)
				self.Btn_Seven.setChecked(False)
				self.Btn_Eight.setChecked(True)
				windowposition = WindowPosComp(self.window_position, self.PaneData)
				windowposition.show()
				self.CRTProcessStateDone.emit(True)
		pass

	def PosPaneInit(self, CNCData):
		value = list(CNCData.SoftButtonTempInfo.keys())[ list(CNCData.SoftButtonTempInfo.values()).index(CNCData.CRTPageState) ]
		if value == 'Btn_Six':
			self.Btn_Six.setChecked(True)
		pass

	def CNCSoftBtnSet(self, CNCData):
		if CNCData.CNCCRTState == 'POS':
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
		pass

	def CRTSoftBtnShow(self, CNCData):
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
