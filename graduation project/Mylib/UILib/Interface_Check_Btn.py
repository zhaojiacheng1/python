#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.Qt import *
import sys


class InterfaceCheckBtn(QPushButton):
	key_checked = pyqtSignal(str, str, bool)

	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.toggled.connect(self.check_btn_cao)
		pass

	def check_btn_cao(self):
		self.key_checked.emit(self.property('role'), self.objectName(), self.isChecked())
		pass

	pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = InterfaceCheckBtn()
	window.show()
	sys.exit(app.exec_())
