#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.Qt import *
import sys


class InterfaceDial(QDial):
	value_change = pyqtSignal(str, str, int)

	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.valueChanged.connect(self.dial_cao)
		pass

	def dial_cao(self):
		self.value_change.emit(self.property('role'), self.objectName(), self.value())
		pass

	pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	window.show()
	sys.exit(app.exec_())
