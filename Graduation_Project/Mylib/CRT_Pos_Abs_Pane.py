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


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = CRTPosAbsPane()
	window.show()
	sys.exit(app.exec_())
