#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from UILib.CRT_Pos_Absolute import Ui_Form


class CRTPosAbsPane(QWidget, Ui_Form):
	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		pass

	def PosPaneInit(self, CNCData):
		value = list(CNCData.SoftButtonTempInfo.keys())[ list(CNCData.SoftButtonTempInfo.values()).index(CNCData.CRTPageState) ]
		if value == 'Btn_Six':
			self.Btn_Six.setChecked(True)
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


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = CRTPosAbsPane()
	window.show()
	print(window.Lab_Mode.width(), window.Lab_Date.height())
	print(window.widget_9.width(), window.widget_9.height())

	# window.Btn_One.setChecked(True)
	sys.exit(app.exec_())
