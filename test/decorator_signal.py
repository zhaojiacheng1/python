#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *


class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('装饰器-学习')
		self.resize(640, 480)
		self.setup_ui()
		pass

	def setup_ui(self):
		btn = QPushButton('测试按钮', self)
		btn.setObjectName('btn')
		btn.resize(200, 200)
		btn.move(100, 100)

		btn2 = QPushButton('测试按钮2', self)
		btn2.setObjectName('btn')
		btn2.resize(200, 200)
		btn2.move(100, 300)
		QMetaObject.connectSlotsByName(self)  # 并非动态判定 将self中的子孙对象按照ObjectName连接到相应的槽函数
		# btn.clicked.connect(self.click)
		pass

	@pyqtSlot(bool)  # 装饰器装饰槽函数
	def on_btn_clicked(self, val):  # 相应槽函数的定义方式on_objectName_signalName
		print('按钮被点击', val)

	'''
	装饰器的作用，将上方代码转化为下方代码
	self.btn.clicked[bool].connect(self.btn_clicked)
	def btn_clicked(self):
		pass
	'''


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
