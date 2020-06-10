import sys
import time
import operator
from PyQt5.Qt import *
from UILib.Parameter_window_Tool import Ui_Form


class WindowParameterTool(QWidget, Ui_Form):
	# 字典支持键值为数据元组、数据列表 元组不支持单元素操作 列表支持单元素操作
	# 另需设定时器 保证绝对坐标1秒钟(暂定)更新一次
	# 程序界面内部不同的界面之间传递信息的信号 参数为str数据
	WindowMessageExchangeSignal = pyqtSignal(str)
	# 高亮样式设置
	ParameterSetHightlightStr = """
		background-color: rgb(255,255,0);
		border-top: 2px solid rgb(140,140,140);
		border-left: 2px solid rgb(140,140,140);
		border-right: 2px solid white;
		border-bottom: 2px solid white;	
	"""
	# 正常显示样式设置
	ParameterUnsetHightlightStr = """
		background-color: rgb(192,192,192);
		border-top: 2px solid rgb(140,140,140);
		border-left: 2px solid rgb(140,140,140);
		border-right: 2px solid white;
		border-bottom: 2px solid white;
	"""

	def __init__(self, parent, PaneData, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.ParameterData = PaneData
		self.Pane = Pane
		# 当前控件显示初始化
		self.ParameterWindowToolInit()
		# 当前控件的信号连接
		self.SignalConnectSelf(self.Pane)
		pass

	def ParameterWindowToolInit(self):
		# 番号显示初始化
		self.DesignationShow()
		# 参数显示初始化
		self.ParameterShow()
		# 当前聚焦显示初始化
		self.HightlightShowInit()
		pass

	# 番号显示
	def DesignationShow(self):
		self.Lab_One.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 1).zfill(3))
		self.Lab_Two.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 2).zfill(3))
		self.Lab_Three.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 3).zfill(3))
		self.Lab_Four.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 4).zfill(3))
		self.Lab_Five.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 5).zfill(3))
		self.Lab_Six.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 6).zfill(3))
		self.Lab_Seven.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 7).zfill(3))
		self.Lab_Eight.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 8).zfill(3))
		self.Lab_Nine.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 9).zfill(3))
		self.Lab_Ten.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 10).zfill(3))
		self.Lab_Eleven.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 11).zfill(3))
		self.Lab_Twelve.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 12).zfill(3))
		self.Lab_Thirteen.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 13).zfill(3))
		self.Lab_Fourteen.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 14).zfill(3))
		self.Lab_Fifteen.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 15).zfill(3))
		self.Lab_Sixteen.setText(str((self.ParameterData.ParameterToolShowPage - 1) * 16 + 16).zfill(3))
		pass

	# 参数显示设置
	def ParameterShow(self):
		if self.ParameterData.CNCCRTState != 'Parameter':
			return None
		self.Lab_One_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 1 ][ 0 ])))
		self.Lab_One_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 1 ][ 1 ])))
		self.Lab_One_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 1 ][ 2 ])))
		self.Lab_One_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 1 ][ 3 ])))
		self.Lab_Two_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 2 ][ 0 ])))
		self.Lab_Two_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 2 ][ 1 ])))
		self.Lab_Two_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 2 ][ 2 ])))
		self.Lab_Two_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 2 ][ 3 ])))
		self.Lab_Three_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 3 ][ 0 ])))
		self.Lab_Three_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 3 ][ 1 ])))
		self.Lab_Three_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 3 ][ 2 ])))
		self.Lab_Three_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 3 ][ 3 ])))
		self.Lab_Four_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 4 ][ 0 ])))
		self.Lab_Four_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 4 ][ 1 ])))
		self.Lab_Four_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 4 ][ 2 ])))
		self.Lab_Four_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 4 ][ 3 ])))
		self.Lab_Five_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 5 ][ 0 ])))
		self.Lab_Five_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 5 ][ 1 ])))
		self.Lab_Five_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 5 ][ 2 ])))
		self.Lab_Five_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 5 ][ 3 ])))
		self.Lab_Six_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 6 ][ 0 ])))
		self.Lab_Six_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 6 ][ 1 ])))
		self.Lab_Six_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 6 ][ 2 ])))
		self.Lab_Six_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 6 ][ 3 ])))
		self.Lab_Seven_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 7 ][ 0 ])))
		self.Lab_Seven_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 7 ][ 1 ])))
		self.Lab_Seven_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 7 ][ 2 ])))
		self.Lab_Seven_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 7 ][ 3 ])))
		self.Lab_Eight_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 8 ][ 0 ])))
		self.Lab_Eight_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 8 ][ 1 ])))
		self.Lab_Eight_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 8 ][ 2 ])))
		self.Lab_Eight_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 8 ][ 3 ])))
		self.Lab_Nine_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 9 ][ 0 ])))
		self.Lab_Nine_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 9 ][ 1 ])))
		self.Lab_Nine_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 9 ][ 2 ])))
		self.Lab_Nine_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 9 ][ 3 ])))
		self.Lab_Ten_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 10 ][ 0 ])))
		self.Lab_Ten_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 10 ][ 1 ])))
		self.Lab_Ten_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 10 ][ 2 ])))
		self.Lab_Ten_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 10 ][ 3 ])))
		self.Lab_Eleven_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 11 ][ 0 ])))
		self.Lab_Eleven_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 11 ][ 1 ])))
		self.Lab_Eleven_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 11 ][ 2 ])))
		self.Lab_Eleven_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 11 ][ 3 ])))
		self.Lab_Twelve_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 12 ][ 0 ])))
		self.Lab_Twelve_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 12 ][ 1 ])))
		self.Lab_Twelve_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 12 ][ 2 ])))
		self.Lab_Twelve_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 12 ][ 3 ])))
		self.Lab_Thirteen_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 13 ][ 0 ])))
		self.Lab_Thirteen_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 13 ][ 1 ])))
		self.Lab_Thirteen_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 13 ][ 2 ])))
		self.Lab_Thirteen_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 13 ][ 3 ])))
		self.Lab_Fourteen_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 14 ][ 0 ])))
		self.Lab_Fourteen_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 14 ][ 1 ])))
		self.Lab_Fourteen_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 14 ][ 2 ])))
		self.Lab_Fourteen_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 14 ][ 3 ])))
		self.Lab_Fifteen_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 15 ][ 0 ])))
		self.Lab_Fifteen_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 15 ][ 1 ])))
		self.Lab_Fifteen_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 15 ][ 2 ])))
		self.Lab_Fifteen_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + 15 ][ 3 ])))
		self.Lab_Sixteen_One.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ self.ParameterData.ParameterToolShowPage * 16 ][ 0 ])))
		self.Lab_Sixteen_Two.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ self.ParameterData.ParameterToolShowPage * 16 ][ 1 ])))
		self.Lab_Sixteen_Three.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ self.ParameterData.ParameterToolShowPage * 16 ][ 2 ])))
		self.Lab_Sixteen_Four.setText(str('%.3f' % (self.ParameterData.CNCParameterToolDict[ self.ParameterData.ParameterToolShowPage * 16 ][ 3 ])))
		pass

	# 当前聚焦参数框高亮
	def HightlightShowInit(self):
		if self.ParameterData.CNCCRTState != 'Parameter':
			return None
		self.HightlightUnsetShow()
		self.HightlightSetShow()
		pass

	# 设置高亮显示
	def HightlightSetShow(self):
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 1, 1 ]):
			self.Lab_One_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 1, 2 ]):
			self.Lab_One_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 1, 3 ]):
			self.Lab_One_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 1, 4 ]):
			self.Lab_One_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 2, 1 ]):
			self.Lab_Two_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 2, 2 ]):
			self.Lab_Two_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 2, 3 ]):
			self.Lab_Two_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 2, 4 ]):
			self.Lab_Two_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 3, 1 ]):
			self.Lab_Three_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 3, 2 ]):
			self.Lab_Three_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 3, 3 ]):
			self.Lab_Three_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 3, 4 ]):
			self.Lab_Three_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 4, 1 ]):
			self.Lab_Four_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 4, 2 ]):
			self.Lab_Four_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 4, 3 ]):
			self.Lab_Four_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 4, 4 ]):
			self.Lab_Four_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 5, 1 ]):
			self.Lab_Five_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 5, 2 ]):
			self.Lab_Five_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 5, 3 ]):
			self.Lab_Five_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 5, 4 ]):
			self.Lab_Five_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 6, 1 ]):
			self.Lab_Six_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 6, 2 ]):
			self.Lab_Six_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 6, 3 ]):
			self.Lab_Six_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 6, 4 ]):
			self.Lab_Six_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 7, 1 ]):
			self.Lab_Seven_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 7, 2 ]):
			self.Lab_Seven_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 7, 3 ]):
			self.Lab_Seven_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 7, 4 ]):
			self.Lab_Seven_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 8, 1 ]):
			self.Lab_Eight_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 8, 2 ]):
			self.Lab_Eight_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 8, 3 ]):
			self.Lab_Eight_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 8, 4 ]):
			self.Lab_Eight_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 9, 1 ]):
			self.Lab_Nine_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 9, 2 ]):
			self.Lab_Nine_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 9, 3 ]):
			self.Lab_Nine_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 9, 4 ]):
			self.Lab_Nine_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 10, 1 ]):
			self.Lab_Ten_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 10, 2 ]):
			self.Lab_Ten_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 10, 3 ]):
			self.Lab_Ten_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 10, 4 ]):
			self.Lab_Ten_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 11, 1 ]):
			self.Lab_Eleven_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 11, 2 ]):
			self.Lab_Eleven_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 11, 3 ]):
			self.Lab_Eleven_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 11, 4 ]):
			self.Lab_Eleven_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 12, 1 ]):
			self.Lab_Twelve_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 12, 2 ]):
			self.Lab_Twelve_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 12, 3 ]):
			self.Lab_Twelve_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 12, 4 ]):
			self.Lab_Twelve_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 13, 1 ]):
			self.Lab_Thirteen_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 13, 2 ]):
			self.Lab_Thirteen_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 13, 3 ]):
			self.Lab_Thirteen_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 13, 4 ]):
			self.Lab_Thirteen_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 14, 1 ]):
			self.Lab_Fourteen_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 14, 2 ]):
			self.Lab_Fourteen_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 14, 3 ]):
			self.Lab_Fourteen_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 14, 4 ]):
			self.Lab_Fourteen_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 15, 1 ]):
			self.Lab_Fifteen_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 15, 2 ]):
			self.Lab_Fifteen_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 15, 3 ]):
			self.Lab_Fifteen_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 15, 4 ]):
			self.Lab_Fifteen_Four.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 16, 1 ]):
			self.Lab_Sixteen_One.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 16, 2 ]):
			self.Lab_Sixteen_Two.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 16, 3 ]):
			self.Lab_Sixteen_Three.setStyleSheet(self.ParameterSetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 16, 4 ]):
			self.Lab_Sixteen_Four.setStyleSheet(self.ParameterSetHightlightStr)
		pass

	# 设置高亮前应当将所有的高亮取消
	def HightlightUnsetShow(self):
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 1, 1 ]):
			self.Lab_One_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 1, 2 ]):
			self.Lab_One_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 1, 3 ]):
			self.Lab_One_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 1, 4 ]):
			self.Lab_One_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 2, 1 ]):
			self.Lab_Two_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 2, 2 ]):
			self.Lab_Two_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 2, 3 ]):
			self.Lab_Two_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 2, 4 ]):
			self.Lab_Two_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 3, 1 ]):
			self.Lab_Three_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 3, 2 ]):
			self.Lab_Three_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 3, 3 ]):
			self.Lab_Three_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 3, 4 ]):
			self.Lab_Three_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 4, 1 ]):
			self.Lab_Four_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 4, 2 ]):
			self.Lab_Four_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 4, 3 ]):
			self.Lab_Four_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 4, 4 ]):
			self.Lab_Four_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 5, 1 ]):
			self.Lab_Five_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 5, 2 ]):
			self.Lab_Five_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 5, 3 ]):
			self.Lab_Five_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 5, 4 ]):
			self.Lab_Five_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 6, 1 ]):
			self.Lab_Six_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 6, 2 ]):
			self.Lab_Six_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 6, 3 ]):
			self.Lab_Six_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 6, 4 ]):
			self.Lab_Six_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 7, 1 ]):
			self.Lab_Seven_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 7, 2 ]):
			self.Lab_Seven_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 7, 3 ]):
			self.Lab_Seven_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 7, 4 ]):
			self.Lab_Seven_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 8, 1 ]):
			self.Lab_Eight_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 8, 2 ]):
			self.Lab_Eight_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 8, 3 ]):
			self.Lab_Eight_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 8, 4 ]):
			self.Lab_Eight_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 9, 1 ]):
			self.Lab_Nine_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 9, 2 ]):
			self.Lab_Nine_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 9, 3 ]):
			self.Lab_Nine_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 9, 4 ]):
			self.Lab_Nine_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 10, 1 ]):
			self.Lab_Ten_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 10, 2 ]):
			self.Lab_Ten_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 10, 3 ]):
			self.Lab_Ten_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 10, 4 ]):
			self.Lab_Ten_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 11, 1 ]):
			self.Lab_Eleven_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 11, 2 ]):
			self.Lab_Eleven_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 11, 3 ]):
			self.Lab_Eleven_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 11, 4 ]):
			self.Lab_Eleven_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 12, 1 ]):
			self.Lab_Twelve_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 12, 2 ]):
			self.Lab_Twelve_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 12, 3 ]):
			self.Lab_Twelve_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 12, 4 ]):
			self.Lab_Twelve_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 13, 1 ]):
			self.Lab_Thirteen_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 13, 2 ]):
			self.Lab_Thirteen_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 13, 3 ]):
			self.Lab_Thirteen_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 13, 4 ]):
			self.Lab_Thirteen_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 14, 1 ]):
			self.Lab_Fourteen_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 14, 2 ]):
			self.Lab_Fourteen_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 14, 3 ]):
			self.Lab_Fourteen_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 14, 4 ]):
			self.Lab_Fourteen_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 15, 1 ]):
			self.Lab_Fifteen_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 15, 2 ]):
			self.Lab_Fifteen_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 15, 3 ]):
			self.Lab_Fifteen_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 15, 4 ]):
			self.Lab_Fifteen_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 16, 1 ]):
			self.Lab_Sixteen_One.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 16, 2 ]):
			self.Lab_Sixteen_Two.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 16, 3 ]):
			self.Lab_Sixteen_Three.setStyleSheet(self.ParameterUnsetHightlightStr)
		if operator.eq(self.ParameterData.ParameterToolShowList, [ 16, 4 ]):
			self.Lab_Sixteen_Four.setStyleSheet(self.ParameterUnsetHightlightStr)
		pass

	# 翻页操作
	def PageChangeSlot(self, value):
		if self.ParameterData.CNCCRTState != 'Parameter':
			return None
		print('window', value)
		if value == 'Btn_PAGE_UP':
			if self.ParameterData.ParameterToolShowPage != 25:
				self.ParameterData.ParameterToolShowPage += 1
			pass
		if value == 'Btn_PAGE_DOWN':
			if self.ParameterData.ParameterToolShowPage != 1:
				self.ParameterData.ParameterToolShowPage -= 1
			pass
		self.DesignationShow()
		self.ParameterShow()
		pass

	# 将CRT界面的信号连接到该类中
	def SignalConnectSelf(self, Pane):
		Pane.CRTParameterTextChange.connect(self.CRTParameterTextSlot)
		Pane.CRTParameterCursorMoveSignal.connect(self.ParameterCursorMoveSlot)
		Pane.CRTWindowMessageExchangeSignal.connect(self.LineTextToWindowSlot)
		Pane.CRTPageChangeSignal.connect(self.PageChangeSlot)
		self.WindowMessageExchangeSignal.connect(Pane.WindowMessageExchangeSlot)
		pass

	# 接受单行文本框的信号
	def LineTextToWindowSlot(self, value):
		# 不同的CRT状态对应不同的界面 界面对不上的时候即使接受到了信号也不处理
		if self.ParameterData.CNCCRTState != 'Parameter':
			return None
		print('信息总站的数据_Window', value)
		pass

	# 光标移动处理函数
	def ParameterCursorMoveSlot(self, name):
		# 不同的CRT状态对应不同的界面 界面对应不上的时候即使接收到了信号也不处理
		if self.ParameterData.CNCCRTState != 'Parameter':
			return None
		print(name)
		self.HightlightUnsetShow()
		# 在该界面中的光标的上移操作和左移操作的作用相同
		if name == 'Btn_UP':
			if self.ParameterData.ParameterToolShowList[ 0 ] != 1:
				self.ParameterData.ParameterToolShowList[ 0 ] -= 1
			pass
		if name == 'Btn_LEFT':
			if self.ParameterData.ParameterToolShowList[ 1 ] != 1:
				self.ParameterData.ParameterToolShowList[ 1 ] -= 1
			pass
		# 在该界面中的光标下移操作和右移操作的作用相同
		if name == 'Btn_DOWN':
			if self.ParameterData.ParameterToolShowList[ 0 ] != 16:
				self.ParameterData.ParameterToolShowList[ 0 ] += 1
			pass
		if name == 'Btn_RIGHT':
			if self.ParameterData.ParameterToolShowList[ 1 ] != 4:
				self.ParameterData.ParameterToolShowList[ 1 ] += 1
			pass
		self.HightlightSetShow()
		pass

	# 文件信息显示窗口处理函数
	def CRTParameterTextSlot(self, value):
		if self.ParameterData.CNCCRTState != 'Parameter':
			return None
		print('Window', value)
		# Parameter状态下的特殊按键信息 参数修改
		if value == 'INPUT' or value == 'INSERT' or value == 'ALTER':
			reply = self.InputStrToFormat()
			if reply == False:
				print('输入的字符串为:', reply)
				return False
			print('reply:', reply)
			self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + self.ParameterData.ParameterToolShowList[ 0 ] ][ self.ParameterData.ParameterToolShowList[ 1 ] - 1 ] = reply
			pass
		# 参数重置 设置为0.000
		if value == 'DELETE':
			self.ParameterData.CNCParameterToolDict[ (self.ParameterData.ParameterToolShowPage - 1) * 16 + self.ParameterData.ParameterToolShowList[ 0 ] ][ self.ParameterData.ParameterToolShowList[ 1 ] - 1 ] = 0.000
			pass
		self.ParameterShow()
		self.WindowMessageExchangeSignal.emit('LineTextInsert')
		pass

	# 将输入框中的文本进行格式转化
	def InputStrToFormat(self):
		InsertStr = self.ParameterData.CRTTemporaryInputData
		print('输入的数据:', InsertStr)
		NumFlag = True
		DotNum = 0
		# 小数点检测
		for i in range(0, len(InsertStr)):
			if ord(InsertStr[ i ]) == 46:
				DotNum += 1
		print('小数点出现的次数:', DotNum)
		if DotNum > 1:
			NumFlag = False
		# 数字检测
		for i in range(0, len(InsertStr)):
			if ord(InsertStr[ i ]) != 46 and ord(InsertStr[ i ]) < 48 and ord(InsertStr[ i ]) > 57:
				NumFlag = False
		if NumFlag == False:
			# 非全数字 返回错误
			QMessageBox.warning(None, 'CNC提醒', '输入参数的格式错误！系统无法识别代码的具体含义！', QMessageBox.Yes | QMessageBox.No)  # 阻塞运行，结束自动杀死
			return False
		self.ParameterData.CRTTemporaryInputData = ''
		return float(InsertStr)
		pass
