import sys
from PyQt5.Qt import *
from UILib.Prog_window_probase import Ui_Form


class WindowProgProgramBase(QWidget, Ui_Form):
	# 另需设定时器 保证绝对坐标1秒钟(暂定)更新一次
	def __init__(self, parent, PaneData, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.setAttribute(Qt.WA_StyledBackground, True)  # 设置属性，使资源文件可以加载
		self.setupUi(self)
		self.ProgData = PaneData
		self.Pane = Pane
		self.test()
		pass

	def test(self):
		with open('resource/src/O0001.txt', 'r', encoding='utf-8') as f:  # 可以确保关闭句柄 相对路径相对的是最开始文件运行的路径
			content = f.read()
			# print(content[ 11 ])  # 回车换行算一个字符
			print(len(content))
			self.Lab_ProgramEdit.insertPlainText(content)
			# self.Lab_ProgramEdit.insertPlainText(content[ 0 ])
			# self.Lab_ProgramEdit.insertPlainText(content[ 1 ])
			# self.Lab_ProgramEdit.insertPlainText(content[ 2 ])
			# self.Lab_ProgramEdit.insertPlainText(content[ 3 ])
			# self.Lab_ProgramEdit.insertPlainText(content[ 4 ])
			# self.Lab_ProgramEdit.insertPlainText(content[ 5 ])
			# for i in range(6, len(content)):
			# 	if content[ i ] != 'O':
			# 		if content[ i ] == '\n':
			# 			self.Lab_ProgramEdit.insertPlainText(' ;' + content[ i ])
			# 		elif 65 <= ord(content[ i ]) <= 90 and content[ i - 1 ] != '\n':
			# 			self.Lab_ProgramEdit.insertPlainText(' ' + content[ i ])
			# 		else:
			# 			self.Lab_ProgramEdit.insertPlainText(content[ i ])
			# 	else:
			# 		self.Lab_ProgramEdit.insertPlainText(content[ i ])
			pass
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = WindowProgProgramBase()
	window.show()
	sys.exit(app.exec_())
