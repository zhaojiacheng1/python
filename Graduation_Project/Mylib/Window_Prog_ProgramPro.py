import sys
from PyQt5.Qt import *
from UILib.Prog_window_pro import Ui_Form


class WindowProgProgramPro(QWidget, Ui_Form):
	# 另需设定时器 保证绝对坐标1秒钟(暂定)更新一次
	# 程序界面内部不同的界面之间传递信息的信号 参数为str数据
	WindowMessageExchangeSignal = pyqtSignal(str)
	# 设置当前显示程序的暂存分块数据映射字典 key是行号 value是当前行的内容
	ProgramDict = { }
	# 设置当前显示文本的行号和光标坐标值的映射字典 key是行号 value是当前行首个字符的光标位置值
	ProgramLineNumDict = { }
	# 存储文件的行数 默认为0行
	ProgramLineNum = 0
	# 存储光标的末尾位置值 默认值为0
	ProgramCursorEndPosition = 0
	# 存储当前控件显示的内容 以文件存储的格式 去除\ 和;
	ProgramFileStr = ''
	# 存储当前光标所在行的数据
	ProgramFileLineStr = ''
	# 存储当前光标所在的行号 列号
	LineNumber = 0
	ColumnNumber = 0

	def __init__(self, parent, PaneData, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.ProgData = PaneData
		self.Pane = Pane
		# 取消软换行，采取硬换行
		self.Lab_ProgramEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
		self.ProgWindowEditInit()
		self.LineNumber = self.ProgramLineNum
		self.ChangeDictToFile()
		self.SignalConnectSelf(self.Pane)
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
		if self.ProgData.CNCCRTState != 'PROG_Program':
			return None
		print('信息总站的数据_Window:', value)
		pass

	# 光标移动处理函数
	def ProgramCursorMoveSlot(self, name):
		# 不同的CRT状态对应不同的界面 界面对不上的时候即使接受到了信号也不处理
		if self.ProgData.CNCCRTState != 'PROG_Program':
			return None
		print(name)
		self.Lab_ProgramEdit.setFocus(True)
		cursor = self.Lab_ProgramEdit.textCursor()
		print('当前行号:', self.LineNumber)
		print('最大行号:', self.ProgramLineNum)
		# 在该界面中光标的上移操作和左移操作的作用相同
		if name == 'Btn_UP' or name == 'Btn_LEFT':
			if self.LineNumber != 1:
				self.LineNumber -= 1
		# 在该界面中光标的下移操作和右移操作的作用相同
		if name == 'Btn_DOWN' or name == 'Btn_RIGHT':
			if self.LineNumber != self.ProgramLineNum:
				self.LineNumber += 1
		print('当前行号:', self.LineNumber)
		cursor.setPosition(self.ProgramLineNumDict[ self.LineNumber ])
		self.Lab_ProgramEdit.setTextCursor(cursor)
		self.Lab_ProgramEdit.setFocus(False)
		pass

	# 程序内容改变处理函数函数
	def CRTProgramTextSlot(self, value):
		# 不同的CRT状态对应不同的界面 界面对不上的时候即使接受到了信号也不处理
		if self.ProgData.CNCCRTState != 'PROG_Program':
			return None
		print('界面中', value)
		print('当前的CRT状态:', self.ProgData.CNCCRTState)
		print('当前处于ProgramPro界面')
		# PROG状态下的特殊按键信息
		if self.ProgData.CNCCRTState == 'PROG' or self.ProgData.CNCCRTState == 'PROG_Program':
			# 暂时不处理
			if value == 'INPUT':
				pass
			# 删除光标所在的整行数据
			if value == 'DELETE':
				self.CRTProgramDelete()
			# 将单行输入文本框的内容插入到程序光标所在行的下一行
			if value == 'INSERT':
				print('处理INSERT')
				self.CRTProgramInsert()
				pass
			# 将文本输入框的内容替换程序光标所在行
			if value == 'ALTER':
				self.CRTProgramAlter()
				pass
		pass

	# 将当前行的文本替换为输入框的文本
	def CRTProgramAlter(self):
		reply = self.InputStrToFormat()
		if reply == False:
			print('替换的文本:', reply)
			return False
		print('替换的文本:', reply)
		# print('光标最后的位置:', self.ProgramCursorEndPosition)
		self.WindowMessageExchangeSignal.emit('LineTextAlter')
		# 将当前行的文本替换为输入框的文本 从当前行替换
		# 1、计算光标坐标值的变化量
		positiondifference = len(reply) - len(self.ProgramDict[ self.LineNumber ])
		# print('光标位置的差值:', positiondifference)
		self.ProgramDict[ self.LineNumber ] = reply
		for i in range(self.LineNumber + 1, self.ProgramLineNum + 1):
			self.ProgramLineNumDict[ i ] += positiondifference
		# 判断是否是最后一行 如果是最后一行就插入空白新行
		if self.LineNumber == self.ProgramLineNum:
			self.ProgramLineNum += 1
			self.ProgramDict[ self.ProgramLineNum ] = ''
			self.ProgramCursorEndPosition += positiondifference
			self.ProgramLineNumDict[ self.ProgramLineNum ] = self.ProgramCursorEndPosition
		print(self.ProgramDict)
		print(self.ProgramLineNumDict)
		print('当前行:', self.LineNumber)
		print('光标最后位置:', self.ProgramCursorEndPosition)
		# 更新控件显示的内容 1、删除当前行的内容 2、插入新行内容
		# self.UpdateTextShow(self.LineNumber)
		self.Lab_ProgramEdit.blockSignals(True)
		cursor = self.Lab_ProgramEdit.textCursor()
		cursor.select(QTextCursor.BlockUnderCursor)
		cursor.removeSelectedText()
		cursor.setPosition(self.ProgramLineNumDict[ self.LineNumber ])
		self.Lab_ProgramEdit.setTextCursor(cursor)
		self.Lab_ProgramEdit.blockSignals(False)
		self.Lab_ProgramEdit.insertPlainText(reply)
		pass

	# 插入输入框的文本
	def CRTProgramInsert(self):
		reply = self.InputStrToFormat()
		if reply == False:
			print('输入的字符串为:', reply)
			return False
		print('reply:', reply)
		self.WindowMessageExchangeSignal.emit('LineTextInsert')
		# 将输入的文本插入到当前的程序文本中 从当前行开始插入
		# 1、计算光标坐标值变化量
		positiondifference = len(reply)
		strtemp = self.ProgramDict[ self.LineNumber ]
		self.ProgramDict[ self.LineNumber ] = reply
		positiontemp = self.ProgramLineNumDict[ self.LineNumber ]
		for i in range(self.LineNumber + 1, self.ProgramLineNum + 1):
			# 更新程序内容
			temp = self.ProgramDict[ i ]
			self.ProgramDict[ i ] = strtemp
			strtemp = temp
			# 更新光标位置值
			position = self.ProgramLineNumDict[ i ]
			self.ProgramLineNumDict[ i ] = positiontemp + positiondifference
			positiontemp = position
		# 由于插入一行所以最后应当插入空白行
		self.ProgramLineNum += 1
		self.ProgramDict[ self.ProgramLineNum ] = strtemp
		self.ProgramCursorEndPosition += positiondifference
		self.ProgramLineNumDict[ self.ProgramLineNum ] = self.ProgramCursorEndPosition
		self.Lab_ProgramEdit.blockSignals(True)
		cursor = self.Lab_ProgramEdit.textCursor()
		cursor.setPosition(self.ProgramLineNumDict[ self.LineNumber ])
		self.Lab_ProgramEdit.setTextCursor(cursor)
		# self.UpdateTextShow(self.LineNumber)
		self.Lab_ProgramEdit.blockSignals(False)
		self.Lab_ProgramEdit.insertPlainText(reply)
		pass

	# 将输入框中的文本进行格式转化
	def InputStrToFormat(self):
		InsertStr = self.ProgData.CRTTemporaryInputData
		InsertStrBack = ''
		# 处理字符串末尾的分号，一次输入值只允许出现一个分号且在字符串的末尾，不然报错且不处理
		SemNumber = 0
		SemPosition = 0
		for i in range(0, len(InsertStr)):
			if InsertStr[ i ] == ';':
				SemNumber += 1
				SemPosition = i
		# 分号出现多次 返回错误
		if SemNumber > 1:
			QMessageBox.warning(None, 'CNC提醒', '输入代码的格式错误！系统无法识别代码的具体含义！', QMessageBox.Yes | QMessageBox.No)  # 阻塞运行，结束自动杀死
			return False
		# 分号只出现一次但是不是在最后 返回错误
		if SemNumber == 1 and SemPosition != len(InsertStr) - 1:
			QMessageBox.warning(None, 'CNC提醒', '输入代码的格式错误！系统无法识别代码的具体含义！', QMessageBox.Yes | QMessageBox.No)  # 阻塞运行，结束自动杀死
			return False
		# 没有分号要添加分号
		if SemNumber == 0:
			InsertStr += ';'
		# 先处理空格的问题 除了最开始的大写英文字符之前不需要插入空格外 其他的大写字母和分号前需要插入空格
		# 1、删除所有空格
		InsertStr.replace(' ', '')
		# 2、添加大写字母前的空格
		InsertStrBack += InsertStr[ 0 ]
		for i in range(1, len(InsertStr)):
			if 65 <= ord(InsertStr[ i ]) <= 90:
				InsertStrBack += ' '
			if InsertStr[ i ] == ';':
				InsertStrBack += ' '
			InsertStrBack += InsertStr[ i ]
		InsertStrBack += '\n'
		self.ProgData.CRTTemporaryInputData = ''
		# self.WindowMessageExchangeSignal.emit('LineTextInsert')
		return InsertStrBack
		pass

	# 删除当前行数据操作
	def CRTProgramDelete(self):
		# 当前行为最后一行
		if self.LineNumber == self.ProgramLineNum:
			# 处理最后的光标位置
			self.ProgramCursorEndPosition = self.ProgramLineNumDict[ self.LineNumber ] - 1
			self.LineNumber -= 1
		else:
			# 光标位置的差值
			positiondifference = len(self.ProgramDict[ self.LineNumber + 1 ]) - len(self.ProgramDict[ self.LineNumber ])
			print('光标差值:', positiondifference)
			# 保存光标的最后位置
			self.ProgramCursorEndPosition -= positiondifference
			# 将所有行的数据上移一行
			for i in range(self.LineNumber, self.ProgramLineNum):
				self.ProgramDict[ i ] = self.ProgramDict[ i + 1 ]
				if i != self.LineNumber:
					self.ProgramLineNumDict[ i ] += positiondifference
		# print('改变后的光标值:', i, self.ProgramLineNumDict[ i ])
		# print('删除后的数据字典:', self.ProgramDict)
		# print('删除后的行号字典:', self.ProgramLineNumDict)
		# 清除多余的最后一行
		self.ProgramDict.pop(self.ProgramLineNum)
		self.ProgramLineNumDict.pop(self.ProgramLineNum)
		self.ProgramLineNum -= 1
		# 刷新当前的显示数据
		cursor = self.Lab_ProgramEdit.textCursor()
		cursor.select(QTextCursor.BlockUnderCursor)
		# 需要确保数据更新和光标位置更新没有问题
		cursor.removeSelectedText()
		# self.UpdateTextShow(self.LineNumber)
		pass

	# 通过该方法更新显示界面会改变当前行在界面中的显示位置
	def UpdateTextShow(self, p_startposition):
		self.Lab_ProgramEdit.blockSignals(True)
		self.Lab_ProgramEdit.clear()
		for i in range(1, self.ProgramLineNum + 1):
			self.Lab_ProgramEdit.insertPlainText(self.ProgramDict[ i ])
		cursor = self.Lab_ProgramEdit.textCursor()
		cursor.setPosition(self.ProgramLineNumDict[ p_startposition ])
		self.Lab_ProgramEdit.blockSignals(False)
		self.Lab_ProgramEdit.setTextCursor(cursor)
		pass

	# 程序编辑窗口的初始化函数
	def ProgWindowEditInit(self):
		with open('E:/python/Graduation_Project/resource/src/O0002.txt', 'r', encoding='utf-8') as f:  # 可以确保关闭句柄 相对路径相对的是最开始文件运行的路径
			content = f.read()
			self.ChangeFileToDict(content)
		for i in range(1, self.ProgramLineNum + 1):
			self.Lab_ProgramEdit.insertPlainText(self.ProgramDict[ i ])
		# self.Lab_ProgramEdit.setFocus(True)
		cursor = self.Lab_ProgramEdit.textCursor()
		cursor.setPosition(self.ProgramLineNumDict[ self.ProgramLineNum ])
		self.Lab_ProgramEdit.setTextCursor(cursor)
		# self.Lab_ProgramEdit.ensureCursorVisible()
		print(cursor.position())
		print('行号和内容的字典：\n', self.ProgramDict)
		print('行号和光标位置的字典：\n', self.ProgramLineNumDict)
		# 当前控件的所有文本
		print(self.Lab_ProgramEdit.toPlainText())
		self.Lab_ProgramEdit.cursorPositionChanged.connect(self.CursorChangeSlot)
		# 设置当前行高亮
		self.highlightCurrentLine()
		pass

	def CursorChangeSlot(self):
		# 不同的CRT状态对应不同的界面 界面对不上的时候即使接受到了信号也不处理
		if self.ProgData.CNCCRTState != 'PROG_Program':
			return None
		cursor = self.Lab_ProgramEdit.textCursor()
		# self.Lab_ProgramEdit.setViewportMargins(40, 0, 0, 0)
		self.highlightCurrentLine()
		self.LineNumber = cursor.blockNumber() + 1
		self.ColumnNumber = cursor.columnNumber()
		self.ProgramFileLineStr = self.ProgramDict[ self.LineNumber ]
		# print('当前光标所在的位置', cursor.position())
		# print('当前行首光标:', self.ProgramLineNumDict[ self.LineNumber ])
		# print('最后的光标位置:', self.ProgramCursorEndPosition)
		# print('当前行的文本内容:', self.ProgramFileLineStr)
		# print('当前行的文本内容2:', self.Lab_ProgramEdit.document().findBlockByLineNumber(self.LineNumber - 1).text())
		# print('当前的行号:', self.LineNumber, '当前的列号:', self.ColumnNumber)
		self.CursorSetLineEndPosition()
		pass

	# 设置光标坐标为当前行的最后一位
	def CursorSetLineEndPosition(self):
		cursor = self.Lab_ProgramEdit.textCursor()
		# 判断是否在最后一行
		if self.LineNumber == self.ProgramLineNum:
			cursor.setPosition(self.ProgramCursorEndPosition)
		else:
			cursor.setPosition(self.ProgramLineNumDict[ self.LineNumber + 1 ] - 1)
		self.Lab_ProgramEdit.setTextCursor(cursor)
		# self.Lab_ProgramEdit.setFocus(False)
		pass

	# 这段代码比较重要 用于代码的高亮显示
	def highlightCurrentLine(self):
		# 设置当前块的反白效果 临时有效 光标移动后自动解除相关的效果
		lineColor = QColor(255, 255, 0)
		hi_selection = QTextEdit.ExtraSelection()
		hi_selection.format.setBackground(lineColor)
		# hi_selection.format.setForeground(QColor(Qt.red))
		hi_selection.format.setProperty(QTextFormat.FullWidthSelection, True)
		hi_selection.cursor = self.Lab_ProgramEdit.textCursor()
		# print('块的个数:', hi_selection.cursor.blockNumber())  # 返回当前
		hi_selection.cursor.clearSelection()
		self.Lab_ProgramEdit.setExtraSelections([ hi_selection ])
		pass

	# 将不包含; \ 、的程序代码转换为显示的模式
	def ChangeFileToDict(self, p_str, startposition=0):
		# 删除字符串结尾的换行符
		while p_str[ -1 ] == '\n':
			p_str = p_str[ :-1 ]
		# print('当前字符串:', p_str)
		p_strsaveonline = ''
		p_strlinenum = 0  # 行号从1开始
		p_strcursorpositionstart = startposition  # 光标的位置从0开始 开始的位置
		p_strcursorpositionend = 0  # 光标的位置结束的位置
		for i in range(startposition, len(p_str)):
			if p_str[ i ] != 'O' and 65 <= ord(p_str[ i ]) <= 90 and p_str[ i - 1 ] != '\n':
				p_strsaveonline += ' ' + p_str[ i ]
				p_strcursorpositionend += 2
			elif p_str[ i ] == '\n':
				if p_strsaveonline[ 0 ] != 'O':
					p_strsaveonline += ' ;' + p_str[ i ]  # 保留回车换行
					p_strcursorpositionend += 3
				else:
					p_strsaveonline += p_str[ i ]  # 保留回车换行
					p_strcursorpositionend += 1
				p_strlinenum += 1
				self.ProgramDict[ p_strlinenum ] = p_strsaveonline
				self.ProgramLineNumDict[ p_strlinenum ] = p_strcursorpositionstart
				p_strcursorpositionstart = p_strcursorpositionend
				p_strsaveonline = ''
			else:
				p_strsaveonline += p_str[ i ]
				p_strcursorpositionend += 1
			if i == len(p_str) - 1:
				p_strsaveonline += p_str[ i ]
				p_strlinenum += 1
				p_strsaveonline += ' ;\n'
				p_strcursorpositionend += 4
				self.ProgramDict[ p_strlinenum ] = p_strsaveonline
				self.ProgramLineNumDict[ p_strlinenum ] = p_strcursorpositionstart
				self.ProgramLineNum = p_strlinenum
				self.ProgramCursorEndPosition = p_strcursorpositionend
		# 为字符串字典切片添加空白行
		self.ProgramLineNum += 1
		self.ProgramDict[ self.ProgramLineNum ] = ''
		self.ProgramLineNumDict[ self.ProgramLineNum ] = self.ProgramCursorEndPosition
		pass

	def ChangeDictToFile(self):
		p_str = self.Lab_ProgramEdit.toPlainText()
		print(len(p_str))
		for i in range(0, len(p_str)):
			# 判断当前字符是否是空格 或是分号 并且剔除字符串中的空格和分号 尽量避免使用break语句,python的支持不太好
			if p_str[ i ] != ' ' and p_str[ i ] != ';':
				self.ProgramFileStr += p_str[ i ]
		with open('E:/python/Graduation_Project/resource/src/O0003.txt', 'w', encoding='utf-8') as f:  # 可以确保关闭句柄 相对路径相对的是最开始文件运行的路径
			f.write(self.ProgramFileStr)
		pass

	pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = WindowProgProgramBase()
	window.show()
	sys.exit(app.exec_())
