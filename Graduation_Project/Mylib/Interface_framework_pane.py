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

	def get_keys(self, role, name):
		print(role, name)
		pass

	def get_check_keys(self, role, name, state):
		print(role, name, state)
		pass

	def get_dial_value(self, role, name, value):
		print(role, name, value)
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = InterfaceFrameworkPane()
	window.show()
	sys.exit(app.exec_())
