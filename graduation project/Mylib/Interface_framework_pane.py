#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from UILib.Interface_framework import Ui_Form


class InterfaceFrameworkPane(QWidget, Ui_Form):
	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = InterfaceFrameworkPane()
	window.show()
	# print(window.main_window.width())
	# print(window.main_window.height())
	# label = QLabel(window.main_window)
	# label.setText('主机面')
	# label.show()
	sys.exit(app.exec_())
