import sys
import os
import time
from PyQt5.Qt import *
from UILib.Prog_window_dir import Ui_Form


class WindowProgProgramDir(QWidget, Ui_Form):
	# 字典支持键值为数据元组、数据列表 元组不支持单元素操作 列表支持单元素操作
	# 另需设定时器 保证绝对坐标1秒钟(暂定)更新一次
	# 程序界面内部不同的界面之间传递信息的信号 参数为str数据
	WindowMessageExchangeSignal = pyqtSignal(str)
	# 显示窗口的行号 存储的是显示界面显示的总行数 默认为0行 一般为文件数量+1
	ProgramLineNum = 0
	# 存储当前光标所在的行号 行号在四个界面是一致的 光标移动时 将只触发一个界面的槽函数 其他界面将会顺势处理
	LineNumber = 0
	# 存储四个显示控件的行号与光标坐标的字典 key为行号 value为当前行首个字符的坐标值 光标值存储为列表 顺序根据显示顺序自左向右
	ProgramLineNumDict = { }
	# 存储四个显示控件的行号和显示内容的字典 key为行号 value为当前行上显示的内容 内容存储为列表 顺序根据显示循序自左向右
	ProgramLineDict = { }
	# 存储四个显示控件的光标最后位置 顺序根据显示顺序自左向右
	ProgramCursorEndPosition = [ 0, 0, 0, 0 ]

	def __init__(self, parent, PaneData, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.ProgData = PaneData
		self.Pane = Pane
		# 取消软换行，采取硬换行
		self.Lab_ProgramName.setLineWrapMode(QPlainTextEdit.NoWrap)
		self.Lab_ProgramComment.setLineWrapMode(QPlainTextEdit.NoWrap)
		self.Lab_ProgramSize.setLineWrapMode(QPlainTextEdit.NoWrap)
		self.Lab_ProgramUpdateTime.setLineWrapMode(QPlainTextEdit.NoWrap)
		# 当前控件显示初始化
		self.ProgWindowDirInit()
		# 当前控件的信号连接
		self.SignalConnectSelf(self.Pane)
		pass

	def ProgWindowDirInit(self):
		# 重新计算占用的内存之前应当清空其为0
		self.ProgData.FileTotalMemoryUsed = 0
		# 重新计算文件总数前应当将文件总数清空为0
		self.ProgData.FileTotalNum = 0
		# 获取对应路径下的文件列表
		self.ProgData.FileNameList = os.listdir(self.ProgData.FilePath)
		# 清空文件大小字典
		self.ProgData.FileSizeDict.clear()
		# 清空文件修改时间字典
		self.ProgData.FileUpdateTime.clear()
		# 获取对应文件的大小
		for i in self.ProgData.FileNameList:
			self.ProgData.FileSizeDict[ i ] = os.path.getsize(self.ProgData.FilePath + i)  # 文件大小单位为char
			self.ProgData.FileUpdateTime[ i ] = time.strftime('%Y/%m/%d %H:%M', time.localtime(os.path.getmtime(self.ProgData.FilePath + i)))
			self.ProgData.FileTotalNum += 1
			self.ProgData.FileTotalMemoryUsed += self.ProgData.FileSizeDict[ i ]
			pass
		# 内容更新完毕需要设置刷新显示标志位
		self.ProgData.FilePropertyChangeFlag = True
		print(self.ProgData.FileSizeDict)
		print(self.ProgData.FileUpdateTime)
		print(self.ProgData.FileTotalNum)
		print(self.ProgData.FileTotalMemoryUsed)
		# 显示程序列表相关信息
		self.ChangeConentToDict()
		# 向显示控件写入数据
		for i in range(1, self.ProgramLineNum):
			self.Lab_ProgramName.insertPlainText(self.ProgramLineDict[ i ][ 0 ])
			self.Lab_ProgramComment.insertPlainText(self.ProgramLineDict[ i ][ 1 ])
			self.Lab_ProgramSize.insertPlainText(self.ProgramLineDict[ i ][ 2 ])
			self.Lab_ProgramUpdateTime.insertPlainText(self.ProgramLineDict[ i ][ 3 ])
			pass
		self.CursorChangeFourSlot()
		self.Lab_ProgramName.cursorPositionChanged.connect(self.CursorChangeOneSlot)
		self.Lab_ProgramComment.cursorPositionChanged.connect(self.CursorChangeTwoSlot)
		self.Lab_ProgramSize.cursorPositionChanged.connect(self.CursorChangeThreeSlot)
		self.Lab_ProgramUpdateTime.cursorPositionChanged.connect(self.CursorChangeFourSlot)
		pass

	def CursorChangeOneSlot(self):
		# 不同的CRT状态对应不同的界面 界面对不上的时候即使接受到了信号也不处理
		if self.ProgData.CNCCRTState != 'PROG_DIR':
			return None
		self.Lab_ProgramName.blockSignals(True)
		self.Lab_ProgramComment.blockSignals(True)
		self.Lab_ProgramSize.blockSignals(True)
		self.Lab_ProgramUpdateTime.blockSignals(True)
		cursor = self.Lab_ProgramName.textCursor()
		self.LineNumber = cursor.blockNumber() + 1
		self.CursorSetLineEndPosition()
		self.highlightCurrentLine()
		# print(self.LineNumber)
		self.Lab_ProgramName.blockSignals(False)
		self.Lab_ProgramComment.blockSignals(False)
		self.Lab_ProgramSize.blockSignals(False)
		self.Lab_ProgramUpdateTime.blockSignals(False)
		pass

	def CursorChangeTwoSlot(self):
		# 不同的CRT状态对应不同的界面 界面对不上的时候即使接受到了信号也不处理
		if self.ProgData.CNCCRTState != 'PROG_DIR':
			return None
		self.Lab_ProgramName.blockSignals(True)
		self.Lab_ProgramComment.blockSignals(True)
		self.Lab_ProgramSize.blockSignals(True)
		self.Lab_ProgramUpdateTime.blockSignals(True)
		cursor = self.Lab_ProgramComment.textCursor()
		self.LineNumber = cursor.blockNumber() + 1
		self.CursorSetLineEndPosition()
		self.highlightCurrentLine()
		# print(self.LineNumber)
		self.Lab_ProgramName.blockSignals(False)
		self.Lab_ProgramComment.blockSignals(False)
		self.Lab_ProgramSize.blockSignals(False)
		self.Lab_ProgramUpdateTime.blockSignals(False)
		pass

	def CursorChangeThreeSlot(self):
		# 不同的CRT状态对应不同的界面 界面对不上的时候即使接受到了信号也不处理
		if self.ProgData.CNCCRTState != 'PROG_DIR':
			return None
		self.Lab_ProgramName.blockSignals(True)
		self.Lab_ProgramComment.blockSignals(True)
		self.Lab_ProgramSize.blockSignals(True)
		self.Lab_ProgramUpdateTime.blockSignals(True)
		cursor = self.Lab_ProgramSize.textCursor()
		self.LineNumber = cursor.blockNumber() + 1
		self.CursorSetLineEndPosition()
		self.highlightCurrentLine()
		# print(self.LineNumber)
		self.Lab_ProgramName.blockSignals(False)
		self.Lab_ProgramComment.blockSignals(False)
		self.Lab_ProgramSize.blockSignals(False)
		self.Lab_ProgramUpdateTime.blockSignals(False)
		pass

	def CursorChangeFourSlot(self):
		# 不同的CRT状态对应不同的界面 界面对不上的时候即使接受到了信号也不处理
		if self.ProgData.CNCCRTState != 'PROG_DIR':
			return None
		self.Lab_ProgramName.blockSignals(True)
		self.Lab_ProgramComment.blockSignals(True)
		self.Lab_ProgramSize.blockSignals(True)
		self.Lab_ProgramUpdateTime.blockSignals(True)
		cursor = self.Lab_ProgramUpdateTime.textCursor()
		self.LineNumber = cursor.blockNumber() + 1
		self.CursorSetLineEndPosition()
		self.highlightCurrentLine()
		# print(self.LineNumber)
		self.Lab_ProgramName.blockSignals(False)
		self.Lab_ProgramComment.blockSignals(False)
		self.Lab_ProgramSize.blockSignals(False)
		self.Lab_ProgramUpdateTime.blockSignals(False)
		pass

	def highlightCurrentLine(self):
		# 设置当前块的反白效果 临时有效 光标移动后自动解除相关的效果
		lineColor = QColor(255, 255, 0)
		hi_selection = QTextEdit.ExtraSelection()
		hi_selection.format.setBackground(lineColor)
		hi_selection.format.setProperty(QTextFormat.FullWidthSelection, True)
		hi_selection.cursor = self.Lab_ProgramName.textCursor()
		hi_selection.cursor.clearSelection()
		self.Lab_ProgramName.setExtraSelections([ hi_selection ])

		hi_selection.cursor = self.Lab_ProgramComment.textCursor()
		hi_selection.cursor.clearSelection()
		self.Lab_ProgramComment.setExtraSelections([ hi_selection ])

		hi_selection.cursor = self.Lab_ProgramSize.textCursor()
		hi_selection.cursor.clearSelection()
		self.Lab_ProgramSize.setExtraSelections([ hi_selection ])

		hi_selection.cursor = self.Lab_ProgramUpdateTime.textCursor()
		hi_selection.cursor.clearSelection()
		self.Lab_ProgramUpdateTime.setExtraSelections([ hi_selection ])
		pass

	def CursorSetLineEndPosition(self):
		cursor1 = self.Lab_ProgramName.textCursor()
		cursor2 = self.Lab_ProgramComment.textCursor()
		cursor3 = self.Lab_ProgramSize.textCursor()
		cursor4 = self.Lab_ProgramUpdateTime.textCursor()
		print(self.ProgramLineNumDict)
		# 判断是否在最后一行
		if self.LineNumber == self.ProgramLineNum:
			cursor1.setPosition(self.ProgramCursorEndPosition[ 0 ])
			cursor2.setPosition(self.ProgramCursorEndPosition[ 1 ])
			cursor3.setPosition(self.ProgramCursorEndPosition[ 2 ])
			cursor4.setPosition(self.ProgramCursorEndPosition[ 3 ])
		else:
			cursor1.setPosition(self.ProgramLineNumDict[ self.LineNumber + 1 ][ 0 ] - 1)
			cursor2.setPosition(self.ProgramLineNumDict[ self.LineNumber + 1 ][ 1 ] - 1)
			cursor3.setPosition(self.ProgramLineNumDict[ self.LineNumber + 1 ][ 2 ] - 1)
			cursor4.setPosition(self.ProgramLineNumDict[ self.LineNumber + 1 ][ 3 ] - 1)
		self.Lab_ProgramName.setTextCursor(cursor1)
		self.Lab_ProgramComment.setTextCursor(cursor2)
		self.Lab_ProgramSize.setTextCursor(cursor3)
		self.Lab_ProgramUpdateTime.setTextCursor(cursor4)
		pass

	# 将要显示的内容转化为字典
	def ChangeConentToDict(self):
		# 清空相关显示部分的字典
		self.ProgramLineNumDict.clear()
		self.ProgramLineDict.clear()
		self.ProgramLineNum = 0
		self.ProgramCursorEndPosition = [ 0, 0, 0, 0 ]
		for i in self.ProgData.FileNameList:
			self.ProgramLineNum += 1
			# 更新当前行首个字符的光标位置
			self.ProgramLineNumDict[ self.ProgramLineNum ] = [ self.ProgramCursorEndPosition[ 0 ], self.ProgramCursorEndPosition[ 1 ], self.ProgramCursorEndPosition[ 2 ], self.ProgramCursorEndPosition[ 3 ] ]
			# 更新当前行显示的内容
			self.ProgramLineDict[ self.ProgramLineNum ] = [ i.rstrip(self.ProgData.FileNamePostfix) + '\n', '\n', str(self.ProgData.FileSizeDict[ i ]) + '\n', self.ProgData.FileUpdateTime[ i ] + '\n' ]
			# 更新下一行首个字符的光标位置
			self.ProgramCursorEndPosition[ 0 ] += len(self.ProgramLineDict[ self.ProgramLineNum ][ 0 ])
			self.ProgramCursorEndPosition[ 1 ] += len(self.ProgramLineDict[ self.ProgramLineNum ][ 1 ])
			self.ProgramCursorEndPosition[ 2 ] += len(self.ProgramLineDict[ self.ProgramLineNum ][ 2 ])
			self.ProgramCursorEndPosition[ 3 ] += len(self.ProgramLineDict[ self.ProgramLineNum ][ 3 ])
			pass
		self.ProgramLineNum += 1
		# 更新当前行首个字符的光标位置
		self.ProgramLineNumDict[ self.ProgramLineNum ] = [ self.ProgramCursorEndPosition[ 0 ], self.ProgramCursorEndPosition[ 1 ], self.ProgramCursorEndPosition[ 2 ], self.ProgramCursorEndPosition[ 3 ] ]
		print(self.ProgramLineNum)
		print(self.ProgramLineDict)
		print(self.ProgramLineNumDict)
		print(self.ProgramCursorEndPosition)
		pass

	# 将CRT界面的信号连接到该类中
	def SignalConnectSelf(self, Pane):
		Pane.CRTProgramTextChange.connect(self.CRTProgramTextSlot)
		Pane.CRTProgramCursorMoveSignal.connect(self.ProgramCursorMoveSlot)
		Pane.CRTWindowMessageExchangeSignal.connect(self.LineTextToWindowSlot)
		self.WindowMessageExchangeSignal.connect(Pane.WindowMessageExchangeSlot)
		pass

	# 接受单行文本框的信号
	def LineTextToWindowSlot(self, value):
		# 不同的CRT状态对应不同的界面 界面对不上的时候即使接受到了信号也不处理
		if self.ProgData.CNCCRTState != 'PROG_DIR':
			return None
		print('信息总站的数据_Window', value)
		pass

	# 光标移动处理函数
	def ProgramCursorMoveSlot(self, name):
		# 不同的CRT状态对应不同的界面 界面对应不上的时候即使接收到了信号也不处理
		if self.ProgData.CNCCRTState != 'PROG_DIR':
			return None
		print(name)
		self.Lab_ProgramName.setFocus(True)
		cursor = self.Lab_ProgramName.textCursor()
		# 在该界面中的光标的上移操作和左移操作的作用相同
		if name == 'Btn_UP' or name == 'Btn_LEFT':
			if self.LineNumber != 1:
				self.LineNumber -= 1
			pass
		# 在该界面中的光标下移操作和右移操作的作用相同
		if name == 'Btn_DOWN' or name == 'Btn_RIGHT':
			if self.LineNumber != self.ProgramLineNum:
				self.LineNumber += 1
			pass
		cursor.setPosition(self.ProgramLineNumDict[ self.LineNumber ][ 0 ])
		self.Lab_ProgramName.setTextCursor(cursor)
		self.Lab_ProgramName.setFocus(False)
		pass

	# 文件信息显示窗口处理函数
	def CRTProgramTextSlot(self, value):
		if self.ProgData.CNCCRTState != 'PROG_DIR':
			return None
		# PROG_DIR状态下的特殊按键信息
		if value == 'INPUT':
			pass
		if value == 'DELETE':
			pass
		if value == 'INSERT':
			pass
		if value == 'ALTER':
			pass
		pass
