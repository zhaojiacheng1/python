# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
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
		Form.setStyleSheet("QWidget#Form{\n"
		                   "    border-image: url(:/register/images/register_background.jpg);\n"
		                   "}")
		self.main_menu_btn = QtWidgets.QPushButton(Form)
		self.main_menu_btn.setGeometry(QtCore.QRect(30, 40, 50, 50))
		self.main_menu_btn.setStyleSheet("QPushButton {\n"
		                                 "    border-radius: 25px;\n"
		                                 "    background-color: rgb(255, 170, 255);\n"
		                                 "    border: 2px solid rgb(250, 218, 218);\n"
		                                 "    color: white;\n"
		                                 "}\n"
		                                 "QPushButton:hover {\n"
		                                 "    border: 4px solid rgb(147, 49, 147);\n"
		                                 "}\n"
		                                 "QPushButton:checked {\n"
		                                 "    background-color: rgb(143, 0, 143);\n"
		                                 "}")
		self.main_menu_btn.setCheckable(True)
		self.main_menu_btn.setObjectName("main_menu_btn")
		self.about_menu_btn = QtWidgets.QPushButton(Form)
		self.about_menu_btn.setGeometry(QtCore.QRect(120, 30, 50, 50))
		self.about_menu_btn.setStyleSheet("QPushButton {\n"
		                                  "    border-radius: 25px;\n"
		                                  "    background-color: rgb(255, 170, 255);\n"
		                                  "    border: 2px solid rgb(250, 218, 218);\n"
		                                  "    color: white;\n"
		                                  "}\n"
		                                  "QPushButton:hover {\n"
		                                  "    border: 4px solid rgb(147, 49, 147);\n"
		                                  "}\n"
		                                  "QPushButton:checked {\n"
		                                  "    background-color: rgb(143, 0, 143);\n"
		                                  "}")
		self.about_menu_btn.setCheckable(False)
		self.about_menu_btn.setObjectName("about_menu_btn")
		self.reset_menu_btn = QtWidgets.QPushButton(Form)
		self.reset_menu_btn.setGeometry(QtCore.QRect(110, 110, 50, 50))
		self.reset_menu_btn.setStyleSheet("QPushButton {\n"
		                                  "    border-radius: 25px;\n"
		                                  "    background-color: rgb(255, 170, 255);\n"
		                                  "    border: 2px solid rgb(250, 218, 218);\n"
		                                  "    color: white;\n"
		                                  "}\n"
		                                  "QPushButton:hover {\n"
		                                  "    border: 4px solid rgb(147, 49, 147);\n"
		                                  "}\n"
		                                  "QPushButton:checked {\n"
		                                  "    background-color: rgb(143, 0, 143);\n"
		                                  "}")
		self.reset_menu_btn.setCheckable(False)
		self.reset_menu_btn.setObjectName("reset_menu_btn")
		self.exit_menu_btn = QtWidgets.QPushButton(Form)
		self.exit_menu_btn.setGeometry(QtCore.QRect(30, 130, 50, 50))
		self.exit_menu_btn.setStyleSheet("QPushButton {\n"
		                                 "    border-radius: 25px;\n"
		                                 "    background-color: rgb(255, 170, 255);\n"
		                                 "    border: 2px solid rgb(250, 218, 218);\n"
		                                 "    color: white;\n"
		                                 "}\n"
		                                 "QPushButton:hover {\n"
		                                 "    border: 4px solid rgb(147, 49, 147);\n"
		                                 "}\n"
		                                 "QPushButton:checked {\n"
		                                 "    background-color: rgb(143, 0, 143);\n"
		                                 "}")
		self.exit_menu_btn.setCheckable(False)
		self.exit_menu_btn.setObjectName("exit_menu_btn")
		self.widget = QtWidgets.QWidget(Form)
		self.widget.setGeometry(QtCore.QRect(200, 210, 251, 212))
		self.widget.setObjectName("widget")
		self.formLayout = QtWidgets.QFormLayout(self.widget)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setVerticalSpacing(20)
		self.formLayout.setObjectName("formLayout")
		self.label = QtWidgets.QLabel(self.widget)
		self.label.setStyleSheet("color: rgb(222, 222, 222);\n"
		                         "font: 12pt \"隶书\";")
		self.label.setObjectName("label")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
		self.account_le = QtWidgets.QLineEdit(self.widget)
		self.account_le.setMinimumSize(QtCore.QSize(0, 35))
		self.account_le.setStyleSheet("background-color: transparent; /*    设置透明 */\n"
		                              "color: rgb(240, 240, 240);\n"
		                              "border: none;\n"
		                              "border-bottom: 1px solid lightgray;")
		self.account_le.setClearButtonEnabled(True)
		self.account_le.setObjectName("account_le")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_le)
		self.label_2 = QtWidgets.QLabel(self.widget)
		self.label_2.setStyleSheet("color: rgb(222, 222, 222);\n"
		                           "font: 12pt \"隶书\";")
		self.label_2.setObjectName("label_2")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
		self.password_le = QtWidgets.QLineEdit(self.widget)
		self.password_le.setMinimumSize(QtCore.QSize(0, 35))
		self.password_le.setStyleSheet("background-color: transparent; /*    设置透明 */\n"
		                               "color: rgb(240, 240, 240);\n"
		                               "border: none;\n"
		                               "border-bottom: 1px solid lightgray;")
		self.password_le.setClearButtonEnabled(True)
		self.password_le.setObjectName("password_le")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_le)
		self.label_3 = QtWidgets.QLabel(self.widget)
		self.label_3.setStyleSheet("color: rgb(222, 222, 222);\n"
		                           "font: 12pt \"隶书\";")
		self.label_3.setObjectName("label_3")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
		self.confirm_le = QtWidgets.QLineEdit(self.widget)
		self.confirm_le.setMinimumSize(QtCore.QSize(0, 35))
		self.confirm_le.setStyleSheet("background-color: transparent; /*    设置透明 */\n"
		                              "color: rgb(240, 240, 240);\n"
		                              "border: none;\n"
		                              "border-bottom: 1px solid lightgray;")
		self.confirm_le.setClearButtonEnabled(True)
		self.confirm_le.setObjectName("confirm_le")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.confirm_le)
		self.register_btn = QtWidgets.QPushButton(self.widget)
		self.register_btn.setEnabled(False)
		self.register_btn.setMinimumSize(QtCore.QSize(0, 45))
		self.register_btn.setStyleSheet("QPushButton {\n"
		                                "    background-color: rgb(255, 170, 127);\n"
		                                "    color: rgb(35, 64, 255);\n"
		                                "    border-radius: 10px;\n"
		                                "}\n"
		                                "QPushButton:hover {\n"
		                                "    \n"
		                                "    background-color: rgb(255, 213, 193);\n"
		                                "}\n"
		                                "QPushButton:pressed {\n"
		                                "    \n"
		                                "    background-color: rgb(239, 150, 41);\n"
		                                "}\n"
		                                "QPushButton:disabled {\n"
		                                "    background-color: rgb(190, 190, 190);\n"
		                                "}")
		self.register_btn.setObjectName("register_btn")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.register_btn)
		self.label.raise_()
		self.label_2.raise_()
		self.label_3.raise_()
		self.account_le.raise_()
		self.password_le.raise_()
		self.confirm_le.raise_()
		self.register_btn.raise_()
		self.about_menu_btn.raise_()
		self.reset_menu_btn.raise_()
		self.exit_menu_btn.raise_()
		self.main_menu_btn.raise_()

		self.retranslateUi(Form)
		self.main_menu_btn.clicked[ 'bool' ].connect(Form.show_hide_menu)
		self.about_menu_btn.clicked.connect(Form.about_menu)
		self.reset_menu_btn.clicked.connect(Form.reset)
		self.exit_menu_btn.clicked.connect(Form.exit_menu)
		self.register_btn.clicked.connect(Form.check_register)
		self.account_le.textChanged[ 'QString' ].connect(Form.enable_register_btn)
		self.password_le.textChanged[ 'QString' ].connect(Form.enable_register_btn)
		self.confirm_le.textChanged[ 'QString' ].connect(Form.enable_register_btn)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "注册"))
		self.main_menu_btn.setText(_translate("Form", "菜单"))
		self.about_menu_btn.setText(_translate("Form", "关于"))
		self.reset_menu_btn.setText(_translate("Form", "重置"))
		self.exit_menu_btn.setText(_translate("Form", "退出"))
		self.label.setText(_translate("Form", "账   号："))
		self.label_2.setText(_translate("Form", "密   码："))
		self.label_3.setText(_translate("Form", "确认密码："))
		self.register_btn.setText(_translate("Form", "注册"))


import images_rc

if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
