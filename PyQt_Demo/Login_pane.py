#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from resource.login import Ui_Form


class LoginPane(QWidget, Ui_Form):
	show_register_pane_signal = pyqtSignal()
	check_login_signal = pyqtSignal(str, str)

	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		movie = QMovie(':/login/images/login_top_bg.gif')
		movie.setScaledSize(QSize(500, 235))
		self.login_top_bg_label.setMovie(movie)
		movie.start()
		pass

	def show_register_pane(self):
		self.show_register_pane_signal.emit()
		pass

	def open_qq_link(self):
		link = 'http://shang.qq.com/wpa/qunwpa?idkey=b4d516fe37a2da8c8690140b133cb5a194aef98e639f4481500e271e1850ab3d'
		QDesktopServices.openUrl(QUrl(link))
		pass

	def enable_login_btn(self):
		account = self.account_cb.currentText()
		pwd = self.pwd_le.text()
		# print(account, pwd)
		if len(account) > 0 and len(pwd) > 0:
			self.login_btn.setEnabled(True)
		else:
			self.login_btn.setEnabled(False)
		pass

	def check_login(self):
		account = self.account_cb.currentText()
		pwd = self.pwd_le.text()
		self.check_login_signal.emit(account, pwd)
		pass

	def auto_login(self, checked):
		print('自动登录', checked)
		if checked:
			self.remember_pwd_cb.setChecked(True)
		pass

	def remember_pwd(self, checked):
		print('记住密码', checked)
		if not checked:
			self.auto_login_cb.setChecked(False)
		pass

	def show_error_animation(self):
		animation = QPropertyAnimation(self)
		animation.setTargetObject(self.login_bottom)
		animation.setPropertyName(b'pos')
		animation.setKeyValueAt(0, self.login_bottom.pos())
		animation.setKeyValueAt(0.2, self.login_bottom.pos() + QPoint(15, 0))
		animation.setKeyValueAt(0.5, self.login_bottom.pos())
		animation.setKeyValueAt(0.7, self.login_bottom.pos() + QPoint(-15, 0))
		animation.setKeyValueAt(1, self.login_bottom.pos())
		animation.setLoopCount(3)
		animation.setDuration(200)
		animation.start(QAbstractAnimation.DeleteWhenStopped)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = LoginPane()
	window.show()
	sys.exit(app.exec_())
