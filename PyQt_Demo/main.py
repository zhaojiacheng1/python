#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from Login_pane import LoginPane
from Register_pane import RegisterPane
from Caculator_pane import CaculatorPane
from PyQt5.Qt import *

if __name__ == '__main__':
	app = QApplication(sys.argv)
	login_pane = LoginPane()
	register_pane = RegisterPane(login_pane)
	register_pane.move(0, login_pane.height())
	register_pane.show()
	caculator = CaculatorPane()

	def exit_register_pane():
		anmiation = QPropertyAnimation(register_pane)
		anmiation.setTargetObject(register_pane)
		anmiation.setPropertyName(b'pos')
		anmiation.setStartValue(QPoint(0, 0))
		anmiation.setEndValue(QPoint(login_pane.width(), 0))
		anmiation.setDuration(1000)
		anmiation.setEasingCurve(QEasingCurve.OutBounce)
		anmiation.start(QAbstractAnimation.DeleteWhenStopped)
		pass


	register_pane.exit_signal.connect(exit_register_pane)

	register_pane.register_account_pwd_signal.connect(lambda account, pwd: print(account, pwd))


	def show_register_pane():
		print('展示注册界面')
		anmiation = QPropertyAnimation(register_pane)
		anmiation.setTargetObject(register_pane)
		anmiation.setPropertyName(b'pos')
		anmiation.setStartValue(QPoint(0, login_pane.height()))
		anmiation.setEndValue(QPoint(0, 0))
		anmiation.setDuration(1000)
		anmiation.setEasingCurve(QEasingCurve.OutBounce)
		anmiation.start(QAbstractAnimation.DeleteWhenStopped)


	login_pane.show_register_pane_signal.connect(show_register_pane)


	def check_login(account, pwd):
		print('账号密码判定', account, pwd)
		if account == '6350434234' and pwd == 'itlike':
			print('登录成功')
			caculator.show()
			login_pane.hide()
		else:
			login_pane.show_error_animation()
		pass


	login_pane.check_login_signal.connect(check_login)
	login_pane.show()
	sys.exit(app.exec_())
