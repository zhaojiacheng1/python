# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_right_clicked.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(775, 577)
		self.pushButton = Btn(Form)
		self.pushButton.setGeometry(QtCore.QRect(170, 130, 93, 28))
		self.pushButton.setObjectName("pushButton")

		self.retranslateUi(Form)
		self.pushButton.rightClicked.connect(Form.test_right_click)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.pushButton.setText(_translate("Form", "PushButton"))


from test import Btn

if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
