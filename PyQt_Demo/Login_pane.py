#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from resource.login import Ui_Form


class LoginPane(QWidget, Ui_Form):

	def __init__(self):
		super().__init__()
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		movie = QMovie(':/login/images/login_top_bg.gif')
		movie.setScaledSize(QSize(500, 235))
		self.login_top_bg_label.setMovie(movie)
		movie.start()
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = LoginPane()
	window.show()
	sys.exit(app.exec_())
