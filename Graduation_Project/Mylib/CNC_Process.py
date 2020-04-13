#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from Mylib.CRT_Pos_Abs_Pane import CRTPosAbsPane


class CNCProcess(QObject):
	# 信号告诉控制控制面板 用户面板的点击有效了
	ProcessStateDone = pyqtSignal(bool)

	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
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

	# 参数中有 state CNCData
	def CNCPowerProcess(self, state, CNCData):
		if state != CNCData.CNCPowerState:
			return None
		if state:
			if CNCData.CNCCRTState == 'POS':
				window = CRTPosAbsPane(self.parent())
				self.CNCSoftBtnSet(CNCData)
				window.CRTSoftBtnShow(CNCData)
				window.PosPaneInit(CNCData)
				window.show()
				self.ProcessStateDone.emit(True)
		else:
			window = self.parent().children()
			# print(window)
			window_list = ()
			# print(type(window[ 0 ]), type(window[ 1 ]), type(window[ 2 ]))
			for i in range(0, len(window)):
				if type(window[ i ]) != type(CNCData) and type(window[ i ]) != CNCProcess:
					window_list += (window[ i ],)
			crtwindow = window_list[ 0 ]
			crtwindow.setParent(None)
			self.ProcessStateDone.emit(True)
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
