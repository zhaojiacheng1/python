import sys
from PyQt5.Qt import *
from UILib.Prog_window_probase import Ui_Form


class WindowProgProgramBase(QWidget, Ui_Form):
	# 另需设定时器 保证绝对坐标1秒钟(暂定)更新一次
	# 设置当前显示程序的暂存字典 key是行号 value是当前行的内容
	ProgramDict = { }
	# 设置当前显示行号和光标坐标值的字典 key是行号 value是当前行首个字符的光标位置值
	ProgramLineNumDict = { }
	# 存储文件的行数 默认为0行
	ProgramLineNum = 0
	# 存储光标的末尾位置值 默认值为0
	ProgramCursorEndPosition = 0
	# 存储当前控件显示的内容 以文件存储的格式 去除\ 和;
	ProgramFileStr = ''

	def __init__(self, parent, PaneData, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.ProgData = PaneData
		self.Pane = Pane
		# 取消软换行，采取硬换行
		self.Lab_ProgramEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
		self.ProgWindowEditInit()
		self.ChangeDictToFile()
		pass

	# 程序编辑窗口的初始化函数
	def ProgWindowEditInit(self):
		with open('E:/python/Graduation_Project/resource/src/O0002.txt', 'r', encoding='utf-8') as f:  # 可以确保关闭句柄 相对路径相对的是最开始文件运行的路径
			content = f.read()
			# print(content[ 11 ])  # 回车换行算一个字符
			# print(len(content))
			# self.Lab_ProgramEdit.insertPlainText(content)
			self.ChangeFileToDict(content)
		# cursor = self.Lab_ProgramEdit.textCursor()
		# print(cursor.blockNumber())
		for i in range(1, self.ProgramLineNum + 1):
			self.Lab_ProgramEdit.insertPlainText(self.ProgramDict[ i ])
		self.Lab_ProgramEdit.setFocus(True)
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
		pass

	def CursorChangeSlot(self):
		cursor = self.Lab_ProgramEdit.textCursor()
		# self.Lab_ProgramEdit.setViewportMargins(40, 0, 0, 0)
		self.highligtCurrentLine()
		print(cursor.position())
		pass

	# 这段代码比较重要 用于代码的高亮显示
	def highligtCurrentLine(self):
		# 设置当前块的反白效果 临时有效 光标移动后自动解除相关的效果
		# lineColor = QColor(Qt.yellow).lighter(160)
		lineColor = QColor(255, 255, 0)
		hi_selection = QTextEdit.ExtraSelection()
		hi_selection.format.setBackground(lineColor)
		# hi_selection.format.setForeground(QColor(Qt.red))
		hi_selection.format.setProperty(QTextFormat.FullWidthSelection, True)
		hi_selection.cursor = self.Lab_ProgramEdit.textCursor()
		print('块的个数:', hi_selection.cursor.blockNumber())
		hi_selection.cursor.clearSelection()
		self.Lab_ProgramEdit.setExtraSelections([ hi_selection ])
		pass

	# 将不包含; \ 、的程序代码转换为显示的模式
	def ChangeFileToDict(self, p_str):
		p_strsaveonline = ''
		p_strlinenum = 0  # 行号从1开始
		p_strcursorpositionstart = 0  # 光标的位置从0开始 开始的位置
		p_strcursorpositionend = 0  # 光标的位置结束的位置
		for i in range(0, len(p_str)):
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
				self.ProgramDict[ p_strlinenum ] = p_strsaveonline
				self.ProgramLineNumDict[ p_strlinenum ] = p_strcursorpositionstart
				self.ProgramLineNum = p_strlinenum
				self.ProgramCursorEndPosition = p_strcursorpositionend
		pass

	def ChangeDictToFile(self):
		p_str = self.Lab_ProgramEdit.toPlainText()
		print(len(p_str))
		for i in range(0, len(p_str)):
			# 判断当前字符是否是空格 或是分号 并且剔除字符串中的空格和分号
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
