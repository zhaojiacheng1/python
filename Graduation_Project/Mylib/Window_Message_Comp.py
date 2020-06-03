import sys
from PyQt5.Qt import *
from UILib.Message_window_comp import Ui_Form


class WindowMessageComp(QWidget, Ui_Form):
	# 另需设定时器 保证绝对坐标1秒钟(暂定)更新一次
	def __init__(self, parent, PaneData, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.PosData = PaneData
		# 设置绝对坐标
		self.Lab_X_PosAbs.setText(str(PaneData.CNCPosAbs[ 'X' ]))
		self.Lab_Y_PosAbs.setText(str(PaneData.CNCPosAbs[ 'Y' ]))
		self.Lab_Z_PosAbs.setText(str(PaneData.CNCPosAbs[ 'Z' ]))
		# 设置相对坐标
		self.Lab_X_PosRel.setText(str(PaneData.CNCPosRelative[ 'X' ]))
		self.Lab_Y_PosRel.setText(str(PaneData.CNCPosRelative[ 'Y' ]))
		self.Lab_Z_PosRel.setText(str(PaneData.CNCPosRelative[ 'Z' ]))
		# 设置机械坐标
		self.Lab_X_PosComp.setText(str(PaneData.CNCPosMechanical[ 'X' ]))
		self.Lab_Y_PosComp.setText(str(PaneData.CNCPosMechanical[ 'Y' ]))
		self.Lab_Z_PosComp.setText(str(PaneData.CNCPosMechanical[ 'Z' ]))
		self.timerinit()
		pass

	def timerinit(self):
		self.timer_id = self.startTimer(1000)  # 设置1s定时器
		self.timernum = 0
		pass

	def timerEvent(self, evt):
		# 刷新坐标显示
		# 设置绝对坐标
		self.Lab_X_PosAbs.setText(str(self.PosData.CNCPosAbs[ 'X' ]))
		self.Lab_Y_PosAbs.setText(str(self.PosData.CNCPosAbs[ 'Y' ]))
		self.Lab_Z_PosAbs.setText(str(self.PosData.CNCPosAbs[ 'Z' ]))
		# 设置相对坐标
		self.Lab_X_PosRel.setText(str(self.PosData.CNCPosRelative[ 'X' ]))
		self.Lab_Y_PosRel.setText(str(self.PosData.CNCPosRelative[ 'Y' ]))
		self.Lab_Z_PosRel.setText(str(self.PosData.CNCPosRelative[ 'Z' ]))
		# 设置机械坐标
		self.Lab_X_PosComp.setText(str(self.PosData.CNCPosMechanical[ 'X' ]))
		self.Lab_Y_PosComp.setText(str(self.PosData.CNCPosMechanical[ 'Y' ]))
		self.Lab_Z_PosComp.setText(str(self.PosData.CNCPosMechanical[ 'Z' ]))
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = WindowMessageComp()
	window.show()
	sys.exit(app.exec_())
