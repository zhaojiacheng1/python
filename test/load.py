#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *


class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('ui学习-学习')
		self.resize(640, 480)
		self.setup_ui()
		pass

	def setup_ui(self):
		from PyQt5.uic import loadUi
		loadUi('test.ui', self)

		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()


	def click():
		print('xxx')
		account = window.lineEdit.text()
		pwd = window.lineEdit_2.text()
		print(account, pwd)


	window.pushButton.clicked.connect(click)
	sys.exit(app.exec_())
