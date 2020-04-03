#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from test_ui import Ui_Form


class Window(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('ui学习-学习')
		self.resize(640, 480)
		self.setupUi(self)
		pass

	def setup_ui(self):
		pass

	def btn_click(self):
		# print('xxx')
		print(self.lineEdit.text())
		print(self.lineEdit_2.text())
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())