#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from resource.register import Ui_Form


class RegisterPane(QWidget, Ui_Form):
	exit_signal = pyqtSignal()
	register_account_pwd_signal = pyqtSignal(str, str)

	def __init__(self):
		super().__init__()
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.animation_targets = [ self.about_menu_btn, self.reset_menu_btn, self.exit_menu_btn ]
		self.animation_targets_pos = [ target.pos() for target in self.animation_targets ]  # 列表推导式
		pass

	def show_hide_menu(self, checked):
		print('显示和隐藏', checked)
		animation_group = QSequentialAnimationGroup(self)
		for idx, target in enumerate(self.animation_targets):
			animation = QPropertyAnimation()
			animation.setTargetObject(target)
			animation.setPropertyName(b'pos')
			# if not checked:
			animation.setStartValue(self.main_menu_btn.pos())
			animation.setEndValue(self.animation_targets_pos[ idx ])
			# else:
			# 	animation.setEndValue(self.main_menu_btn.pos())
			# 	animation.setStartValue(self.animation_targets_pos[ idx ])
			animation.setDuration(200)
			animation.setEasingCurve(QEasingCurve.InOutBounce)  # 设置动画运行曲线
			animation_group.addAnimation(animation)
		if not checked:
			animation_group.setDirection(QAbstractAnimation.Forward)
		else:
			animation_group.setDirection(QAbstractAnimation.Backward)
		animation_group.start(QAbstractAnimation.DeleteWhenStopped)
		pass

	def about_menu(self):
		print('关于')
		QMessageBox.about(self, '撩课学院', 'https://www.itlike.com')  # 设置消息盒子
		pass

	def reset(self):
		print('重置')
		self.account_le.clear()
		self.password_le.clear()
		self.confirm_le.clear()
		pass

	def exit_menu(self):
		print('退出')
		self.exit_signal.emit()
		pass

	def check_register(self):
		print('注册')
		account_txt = self.account_le.text()
		password_txt = self.password_le.text()
		self.register_account_pwd_signal.emit(account_txt, password_txt)
		pass

	def enable_register_btn(self):
		print('判定')
		account_txt = self.account_le.text()
		password_txt = self.password_le.text()
		cp_txt = self.confirm_le.text()
		if len(account_txt) > 0 and len(password_txt) > 0 and len(cp_txt) > 0 and password_txt == cp_txt:
			self.register_btn.setEnabled(True)
		else:
			self.register_btn.setEnabled(False)
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = RegisterPane()
	window.exit_signal.connect(lambda: print('退出'))
	window.register_account_pwd_signal.connect(lambda account, pwd: print(account, pwd))
	window.show()
	sys.exit(app.exec_())
