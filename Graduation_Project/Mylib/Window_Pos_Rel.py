import sys
from PyQt5.Qt import *
from UILib.Position_window_rel import Ui_Form


class WindowPosRel(QWidget, Ui_Form):
	# 另需设定时器 保证绝对坐标1秒钟(暂定)更新一次
	def __init__(self, parent, PaneData, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.PosData = PaneData
		# 设置相对坐标
		self.Lab_X_Pos.setText(str(PaneData.CNCPosRelative[ 'X' ]))
		self.Lab_Y_Pos.setText(str(PaneData.CNCPosRelative[ 'Y' ]))
		self.Lab_Z_Pos.setText(str(PaneData.CNCPosRelative[ 'Z' ]))
		self.timerinit()
		pass

	def timerinit(self):
		self.timer_id = self.startTimer(1000)  # 设置1s定时器
		self.timernum = 0
		pass

	def timerEvent(self, evt):
		# 刷新坐标显示
		self.Lab_X_Pos.setText(str(self.PosData.CNCPosRelative[ 'X' ]))
		self.Lab_Y_Pos.setText(str(self.PosData.CNCPosRelative[ 'Y' ]))
		self.Lab_Z_Pos.setText(str(self.PosData.CNCPosRelative[ 'Z' ]))
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = WindowPosRel()
	window.show()
	sys.exit(app.exec_())
