import sys
from PyQt5.Qt import *
from UILib.Position_window_comp import Ui_Form


class WindowPosComp(QWidget, Ui_Form):
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
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = WindowPosComp()
	window.show()
	sys.exit(app.exec_())
