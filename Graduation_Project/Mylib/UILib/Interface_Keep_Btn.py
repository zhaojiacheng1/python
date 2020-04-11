#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.Qt import *
import sys


class InterfaceKeepBtn(QPushButton):
	key_keep_pressed = pyqtSignal(str, str, bool)

	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.pressed.connect(self.btn_pressed)  # 按钮按下时发送信号
		self.released.connect(self.btn_released)  # 按钮松开时发送信号
		pass

	def btn_pressed(self):
		self.key_keep_pressed.emit(self.property('role'), self.objectName(), True)
		pass

	def btn_released(self):
		self.key_keep_pressed.emit(self.property('role'), self.objectName(), False)
		pass

	pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = InterfaceBtn()
	window.show()
	sys.exit(app.exec_())
