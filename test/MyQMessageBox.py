import sys
from PyQt5.Qt import *


class MyQMessageBox(QMessageBox):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.setQuitOnLastWindowClosed(False)
		self.open()
		self.MessageBoxInit()
		pass

	def MessageBoxInit(self):
		self.setStyleSheet('background-color:white;')
		self.buttonClicked.connect(self.ButtonSlot)
		pass

	def closeEvent(self, evt):
		self.setParent(None)
		evt.accept()
		# super().closeEvent(evt)
		# evt.ignore()
		pass

	def ButtonSlot(self):
		self.setParent(None)
		pass

	pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	window.setStyleSheet('background-color:red;')
	window.show()
	mb = MyQMessageBox(QMessageBox.Warning, '提醒', '程序保护已开启！', QMessageBox.Yes | QMessageBox.No, window)
	time = QTimer(window)
	time.start(1000)
	time.timeout.connect(lambda: print(window.children()))

	sys.exit(app.exec_())
