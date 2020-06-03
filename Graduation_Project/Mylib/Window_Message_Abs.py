import sys
from PyQt5.Qt import *
from UILib.Message_window_abs import Ui_Form


class WindowMessageAbs(QWidget, Ui_Form):
	# 另需设定时器 保证绝对坐标1秒钟(暂定)更新一次
	def __init__(self, parent, PaneData, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.PosData = PaneData
		# 设置绝对坐标
		self.Lab_X_Pos.setText(str(PaneData.CNCPosAbs[ 'X' ]))
		self.Lab_Y_Pos.setText(str(PaneData.CNCPosAbs[ 'Y' ]))
		self.Lab_Z_Pos.setText(str(PaneData.CNCPosAbs[ 'Z' ]))
		self.timerinit()
		pass

	def timerinit(self):
		self.timer_id = self.startTimer(1000)  # 设置1s定时器
		self.timernum = 0
		pass

	def timerEvent(self, evt):
		# 刷新坐标显示
		self.Lab_X_Pos.setText(str(self.PosData.CNCPosAbs[ 'X' ]))
		self.Lab_Y_Pos.setText(str(self.PosData.CNCPosAbs[ 'Y' ]))
		self.Lab_Z_Pos.setText(str(self.PosData.CNCPosAbs[ 'Z' ]))
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = WindowMessageAbs()
	window.show()
	sys.exit(app.exec_())
