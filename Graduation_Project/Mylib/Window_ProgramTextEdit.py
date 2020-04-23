import sys
from PyQt5.Qt import *
from UILib.Program_EditWindow import Ui_Form


class WindowProgramTextEdit(QWidget, Ui_Form):
	def __init__(self, parent, PaneData, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.ProgData = PaneData
		# 设置该控件所属的基本盘
		self.ProgPane = Pane
		pass

	pass

	if __name__ == '__main__':
		app = QApplication(sys.argv)
		window = WindowProgramTextEdit()
		window.show()
		sys.exit(app.exec_())
