import sys
from PyQt5.Qt import *
from UILib.Message_window_alarm import Ui_Form
from datetime import datetime


class WindowMessageAlarm(QWidget, Ui_Form):
	# 另需设定时器 保证绝对坐标1秒钟(暂定)更新一次
	colorint = 0

	def __init__(self, parent, PaneData, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.MessageData = PaneData
		self.Pane = Pane
		self.SignalConnectWindow(Pane)
		pass

	# 将CRTMessagePane中的信号传递到WindowMessageAlarm界面中
	def SignalConnectWindow(self, Pane):
		Pane.CRTtoWindowSignal.connect(self.CRTMessageToWindowSlot)
		pass

	def CRTMessageToWindowSlot(self, *args):
		value = args[ 0 ]
		if value == 'ALARM':
			# 设置alarm信息界面
			Messagestr = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '  Alarm'
			# fmt = QTextCharFormat()  # 文本字符格式
			# fmt.setForeground(QColor(204, self.colorint, 204))  # 前景色(即字体色)设为color色
			# cursor.mergeCharFormat(fmt)  # 光标后的文字就用该格式显示
			# self.Lab_alarmwindow.mergeCurrentCharFormat(fmt)  # textEdit使用当前的字符格式
			# self.Lab_alarmwindow.setFocus(True)
			# QTextCursor
			self.Lab_alarmwindow.clear()
			self.Lab_alarmwindow.insertPlainText(Messagestr)
			cursor = self.Lab_alarmwindow.textCursor()  # 获取文本光标
			print("在第几列", cursor.columnNumber())
			print("光标位置", cursor.position())
			print('块数量', cursor.blockNumber())
			if len(self.MessageData.CNCAlarmMessage) == 0:
				self.MessageData.CNCAlarmMessage += Messagestr
			else:
				self.MessageData.CNCAlarmMessage += '\r\n' + Messagestr
			self.colorint += 10
			if self.colorint > 250:
				self.colorint = 0
		if value == 'MSG':
			# 设置msg信息界面
			self.Lab_alarmwindow.clear()
			Messagestr = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '  Msg'
			self.Lab_alarmwindow.appendPlainText(Messagestr)
			if len(self.MessageData.CNCAlarmMessage) == 0:
				self.MessageData.CNCAlarmMessage += Messagestr
			else:
				self.MessageData.CNCAlarmMessage += '\r\n' + Messagestr
			self.Lab_alarmwindow.setFocus(True)
			cursor = self.Lab_alarmwindow.textCursor()  # 获取文本光标
			print("在第几列", cursor.columnNumber())
			print("光标位置", cursor.position())
			print('块数量', cursor.blockNumber())
		if value == 'HISTORY':
			# 设置 history 信息界面
			self.Lab_alarmwindow.clear()
			self.Lab_alarmwindow.insertPlainText(self.MessageData.CNCAlarmMessage)
			self.Lab_alarmwindow.setFocus(True)
			cursor = self.Lab_alarmwindow.textCursor()  # 获取文本光标
			print("在第几列", cursor.columnNumber())
			print("光标位置", cursor.position())
			print('块数量', cursor.blockNumber())
		if value == 'CLEAR':
			# 清除当前界面的信息
			self.MessageData.CNCAlarmMessage = ''
			self.Lab_alarmwindow.clear()
			self.Lab_alarmwindow.setFocus(True)
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = WindowMessageAlarm()
	window.show()
	sys.exit(app.exec_())
