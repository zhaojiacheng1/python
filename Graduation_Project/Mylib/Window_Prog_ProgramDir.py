import sys
from PyQt5.Qt import *
from UILib.Prog_window_dir import Ui_Form


class WindowProgProgramDir(QWidget, Ui_Form):
	# 另需设定时器 保证绝对坐标1秒钟(暂定)更新一次
	# 程序界面内部不同的界面之间传递信息的信号 参数为str数据
	WindowMessageExchangeSignal = pyqtSignal(str)

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
		# self.ProgWindowEditInit()
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
		# 在该界面中的光标的上移操作和左移操作的作用相同
		if name == 'Btn_UP' or name == 'Btn_LEFT':
			pass
		# 在该界面中的光标下移操作和右移操作的作用相同
		if name == 'Btn_DOWN' or name == 'Btn_RIGHT':
			pass
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
