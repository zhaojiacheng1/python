import sys
from PyQt5.Qt import *
from UILib.Program_EditWindow import Ui_Form


class WindowProgramTextEdit(QWidget, Ui_Form):
	# 程序界面内部不同的界面之间传递信息的信号 参数为str数据
	WindowMessageExchangeSignal = pyqtSignal(str)

	def __init__(self, parent, PaneData, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.ProgData = PaneData
		# 设置该控件所属的基本盘
		self.ProgPane = Pane
		self.ProgramTextEditInit()
		self.SignalConnectSlot(self.ProgPane)
		pass

	# 将CRT界面的信号连接到该类中
	def SignalConnectSlot(self, Pane):
		Pane.CRTTemporaryInputDataSignal.connect(self.ShowLineTextSlot)
		Pane.CRTWindowMessageExchangeSignal.connect(self.WindowToLineTextSlot)
		self.WindowMessageExchangeSignal.connect(Pane.WindowMessageExchangeSlot)
		pass

	def SignalDisconnectSlot(self, Pane):
		Pane.CRTTemporaryInputDataSignal.disconnect(self.ShowLineTextSlot)
		Pane.CRTWindowMessageExchangeSignal.disconnect(self.WindowToLineTextSlot)
		self.WindowMessageExchangeSignal.disconnect(Pane.WindowMessageExchangeSlot)
		pass

	# 接受程序显示窗口的信号
	def WindowToLineTextSlot(self, value):
		print('信息总站的数据_LineText:', value)
		if value == 'LineTextInsert':
			self.ShowLineTextSlot(True)
		if value == 'LineTextAlter':
			self.ShowLineTextSlot(True)
		pass

	# 单行文本框的显示操作
	def ShowLineTextSlot(self, state):
		if state:
			print('刷新显示')
			self.ProgramTextEdit.clear()
			self.ProgramTextEdit.setText(self.ProgData.CRTTemporaryInputData)
			pass

	def ProgramTextEditInit(self):
		self.ProgramTextEdit.clear()
		self.ProgramTextEdit.setText(self.ProgData.CRTTemporaryInputData)
		pass

	pass

	if __name__ == '__main__':
		app = QApplication(sys.argv)
		window = WindowProgramTextEdit()
		window.show()
		sys.exit(app.exec_())
