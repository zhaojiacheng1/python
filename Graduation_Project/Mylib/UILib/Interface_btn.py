#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.Qt import *
import sys


class InterfaceBtn(QPushButton):
	key_pressed = pyqtSignal(str, str)

	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.clicked.connect(self.btn_clicked)  # 按钮松开时发送信号
		pass

	def btn_clicked(self):
		self.key_pressed.emit(self.property('role'), self.objectName())
		pass

	pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = InterfaceBtn()
	window.show()
	sys.exit(app.exec_())
