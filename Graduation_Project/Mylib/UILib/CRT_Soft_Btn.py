#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.Qt import *
import sys


class CRTSoftBtn(QPushButton):
	""" 阻断鼠标事件的按钮 不可用于与用户交互，但是可以通过程序设置选中状态 """

	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setCheckable(True)
		pass

	# 鼠标按下控件的事件
	def mousePressEvent(self, *args, **kwargs):
		# super().mousePressEvent(*args, **kwargs)
		pass

	# 鼠标松开控件的事件
	def mouseReleaseEvent(self, *args, **kwargs):
		# super().mouseReleaseEvent(*args, **kwargs)
		pass

	pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	btn1 = QPushButton(window)
	btn1.setText('xxx1')
	btn2 = CRTSoftBtn(window)
	btn2.setText('xxx2')
	btn1.move(100, 100)
	btn1.clicked.connect(lambda: btn2.setChecked(not btn2.isChecked()))
	window.show()
	sys.exit(app.exec_())
