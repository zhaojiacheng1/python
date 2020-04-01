#!/usr/bin/python3
# -*- coding: utf-8 -*-

class QSSTool:
	@staticmethod  # 设置装饰器 将其设为静态方法 必须在定义的函数前
	def setQssToObj(file_path, obj, encoding_str='utf-8'):  # 不需要self
		"""setQssToObj(filepath = str , obj = class,encoding_str = str) -> None"""
		with open(file_path, 'r', encoding=encoding_str) as f:  # 可以确保关闭句柄
			content = f.read()
			obj.setStyleSheet(content)
