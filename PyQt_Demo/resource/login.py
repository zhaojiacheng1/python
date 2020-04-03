# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(500, 450)
		Form.setMinimumSize(QtCore.QSize(500, 450))
		Form.setMaximumSize(QtCore.QSize(500, 450))
		self.verticalLayout = QtWidgets.QVBoxLayout(Form)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.widget = QtWidgets.QWidget(Form)
		self.widget.setStyleSheet("")
		self.widget.setObjectName("widget")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setSpacing(0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.login_top_bg_label = QtWidgets.QLabel(self.widget)
		self.login_top_bg_label.setText("")
		self.login_top_bg_label.setObjectName("login_top_bg_label")
		self.horizontalLayout_2.addWidget(self.login_top_bg_label)
		self.verticalLayout.addWidget(self.widget)
		self.widget_2 = QtWidgets.QWidget(Form)
		self.widget_2.setStyleSheet("")
		self.widget_2.setObjectName("widget_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
		self.horizontalLayout.setContentsMargins(10, 0, 10, 15)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.pushButton = QtWidgets.QPushButton(self.widget_2)
		self.pushButton.setFlat(True)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
		self.widget_3 = QtWidgets.QWidget(self.widget_2)
		self.widget_3.setStyleSheet("")
		self.widget_3.setObjectName("widget_3")
		self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
		self.gridLayout.setObjectName("gridLayout")
		self.comboBox = QtWidgets.QComboBox(self.widget_3)
		self.comboBox.setMinimumSize(QtCore.QSize(0, 45))
		self.comboBox.setStyleSheet("QComboBox {\n"
		                            "    font-size: 20px;\n"
		                            "    border: none;\n"
		                            "    border-bottom: 1px solid lightgray;\n"
		                            "    background-color: transparent;\n"
		                            "}\n"
		                            "QComboBox:hover {\n"
		                            "    border-bottom: 1px solid gray;\n"
		                            "}\n"
		                            "QComboBox:focus {\n"
		                            "    border-bottom: 1px solid rgb(18, 183,245);\n"
		                            "}\n"
		                            "QComboBox:drop-down {\n"
		                            "    background-color: transparent;\n"
		                            "    width: 60px;\n"
		                            "    height: 40px;\n"
		                            "}\n"
		                            "QComboBox:down-arrow {\n"
		                            "    image: url(:/login/images/login_combobox_icon.jpg);\n"
		                            "    width: 60px;\n"
		                            "    height: 20px;\n"
		                            "}\n"
		                            "QComboBox QAbstractItemView {\n"
		                            "    min-height: 60px;\n"
		                            "}\n"
		                            "QComboBox QAbstractItemView:item {\n"
		                            "    color: lightblue;\n"
		                            "}")
		self.comboBox.setEditable(True)
		self.comboBox.setObjectName("comboBox")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/login/images/login_item_icon1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.comboBox.addItem(icon, "")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/login/images/login_item_icon2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.comboBox.addItem(icon1, "")
		self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)
		self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
		self.lineEdit.setMinimumSize(QtCore.QSize(0, 45))
		self.lineEdit.setStyleSheet("QLineEdit {\n"
		                            "    font-size: 20px;\n"
		                            "    border: none;\n"
		                            "    border-bottom: 1px solid lightgray;\n"
		                            "    background: transparent;\n"
		                            "}\n"
		                            "QLineEdit:hover {\n"
		                            "    border-bottom: 1px solid gray;\n"
		                            "}\n"
		                            "QLineEdit:focus {\n"
		                            "    border-bottom: 1px solid rgb(18, 183, 245);\n"
		                            "}")
		self.lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
		self.lineEdit.setClearButtonEnabled(True)
		self.lineEdit.setObjectName("lineEdit")
		self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
		self.checkBox = QtWidgets.QCheckBox(self.widget_3)
		self.checkBox.setObjectName("checkBox")
		self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
		self.checkBox_2 = QtWidgets.QCheckBox(self.widget_3)
		self.checkBox_2.setObjectName("checkBox_2")
		self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1, QtCore.Qt.AlignRight)
		self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
		self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
		self.pushButton_3.setStyleSheet("QPushButton {\n"
		                                "    background-color: rgb(33, 174, 250);\n"
		                                "    border-radius: 8px;\n"
		                                "    color: white;\n"
		                                "    spacing: 20px;\n"
		                                "}\n"
		                                "QPushButton:hover {\n"
		                                "    background-color: rgb(72, 203, 250);\n"
		                                "}\n"
		                                "QPushButton:pressed {\n"
		                                "    background-color: rgb(85, 85, 255);\n"
		                                "}")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/login/images/login_btn_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushButton_3.setIcon(icon2)
		self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
		self.pushButton_3.setObjectName("pushButton_3")
		self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 2)
		self.horizontalLayout.addWidget(self.widget_3)
		self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
		self.pushButton_2.setMinimumSize(QtCore.QSize(100, 100))
		self.pushButton_2.setMaximumSize(QtCore.QSize(100, 100))
		self.pushButton_2.setStyleSheet("border-image: url(:/login/images/login_qrcode.jpg);")
		self.pushButton_2.setText("")
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
		self.horizontalLayout.setStretch(0, 2)
		self.horizontalLayout.setStretch(1, 6)
		self.horizontalLayout.setStretch(2, 2)
		self.verticalLayout.addWidget(self.widget_2)
		self.verticalLayout.setStretch(0, 2)
		self.verticalLayout.setStretch(1, 3)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "登录"))
		self.pushButton.setText(_translate("Form", "注册账号"))
		self.comboBox.setItemText(0, _translate("Form", "6350434234"))
		self.comboBox.setItemText(1, _translate("Form", "931363918"))
		self.checkBox.setText(_translate("Form", "自动登录"))
		self.checkBox_2.setText(_translate("Form", "记住密码"))
		self.pushButton_3.setText(_translate("Form", "安全登录"))


import images_rc

if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
