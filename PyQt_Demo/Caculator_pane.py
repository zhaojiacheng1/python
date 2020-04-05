#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from resource.caculator import Ui_Form


class Caculator(QObject):
	show_content = pyqtSignal(str)

	def __init__(self, parent):
		super().__init__(parent)
		self.key_models = [ ]
		pass

	def key_model_to_str(self):
		expression = ''
		if len(self.key_models) == 0:
			expression = '0'
			print(expression)
			return expression
		for model in self.key_models:
			if model[ 'role' ] == 'operator':
				expression += ' '
				expression += model[ 'title' ]
				expression += ' '
			else:
				expression += model[ 'title' ]
		# print(expression)
		return expression

	def caculate(self):
		if len(self.key_models) > 0 and self.key_models[ -1 ][ 'role' ] == 'operator':
			self.key_models.pop(-1)  # 删除最后一个
		expression = ''
		for model in self.key_models:
			expression += model[ 'title' ]
		result = eval(expression)  # 计算字符串算式，返回值为计算结果
		self.key_models.clear()
		self.key_models.append({ 'title': '{}'.format(result), 'role': 'num' })
		# print(result)
		return result
		pass

	def parse_key_model(self, key_model):
		if key_model[ 'role' ] == 'clear':
			self.key_models.clear()
			# print(self.key_models)
			self.show_content.emit(self.key_model_to_str())
			return None
		if key_model[ 'role' ] == 'caculate':
			result = self.caculate()
			# print(self.key_models)
			self.show_content.emit(str(result))
			return None
		if len(self.key_models) == 0:
			if key_model[ 'role' ] == 'num':
				if key_model[ 'title' ] == '.':
					key_model[ 'title' ] = '0.'
				self.key_models.append(key_model)
			# print(self.key_models)
			self.show_content.emit(self.key_model_to_str())
			return None
		if key_model[ 'title' ] in ('%', '+/-'):
			if self.key_models[ -1 ][ 'role' ] != 'num':
				# print(self.key_models)
				self.show_content.emit(self.key_model_to_str())
				return None
			else:
				if key_model[ 'title' ] == '%':
					self.key_models[ -1 ][ 'title' ] = str(float(self.key_models[ -1 ][ 'title' ]) / 100)
				else:
					self.key_models[ -1 ][ 'title' ] = str(float(self.key_models[ -1 ][ 'title' ]) * -1)
				# print(self.key_models)
				self.show_content.emit(self.key_model_to_str())
			return None
		if key_model[ 'role' ] == self.key_models[ -1 ][ 'role' ]:
			if key_model[ 'role' ] == 'num':
				if key_model[ 'title' ] == '.' and self.key_models[ -1 ][ 'title' ].__contains__('.'):
					# print(self.key_models)
					self.show_content.emit(self.key_model_to_str())
					return None
				if self.key_models[ -1 ][ 'title' ] != '0':
					self.key_models[ -1 ][ 'title' ] += key_model[ 'title' ]
				else:
					if key_model[ 'title' ] == '.':
						self.key_models[ -1 ][ 'title' ] += key_model[ 'title' ]
					else:
						self.key_models[ -1 ][ 'title' ] = key_model[ 'title' ]
			if key_model[ 'role' ] == 'operator':
				self.key_models[ -1 ][ 'title' ] = key_model[ 'title' ]
		else:
			self.key_models.append(key_model)
		self.show_content.emit(self.key_model_to_str())
		# print(self.key_models)
		pass


class CaculatorPane(QWidget, Ui_Form):
	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.caculator = Caculator(self)
		self.lineEdit.setText('0')
		self.caculator.show_content.connect(self.show_content)
		pass

	def show_content(self, content):
		self.lineEdit.setText(content)
		pass

	def get_key(self, title, role):
		# print(title, role)
		self.caculator.parse_key_model({ 'title': title, 'role': role })
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = CaculatorPane()
	window.show()
	sys.exit(app.exec_())
