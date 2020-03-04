#!/usr/bin/python3 
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
'''
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(642, 303)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 70, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 91, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 131, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 131, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 200, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 200, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(340, 50, 256, 192))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "User Login"))
        self.label.setText(_translate("Form", "user name"))
        self.label_2.setText(_translate("Form", "passwords"))
        self.pushButton.setText(_translate("Form", "login in"))
        self.pushButton_2.setText(_translate("Form", "reback"))
'''
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(549, 199)
        self.user_label = QtWidgets.QLabel(Form)
        self.user_label.setGeometry(QtCore.QRect(50, 40, 61, 21))
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Form)
        self.user_lineEdit.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.pwd_label = QtWidgets.QLabel(Form)
        self.pwd_label.setGeometry(QtCore.QRect(50, 80, 54, 21))
        self.pwd_label.setObjectName("pwd_label")
        self.pwd_lineEdit = QtWidgets.QLineEdit(Form)
        self.pwd_lineEdit.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        self.login_Button = QtWidgets.QPushButton(Form)
        self.login_Button.setGeometry(QtCore.QRect(50, 120, 75, 23))
        self.login_Button.setObjectName("login_Button")
        self.cancel_Button = QtWidgets.QPushButton(Form)
        self.cancel_Button.setGeometry(QtCore.QRect(160, 120, 75, 23))
        self.cancel_Button.setObjectName("cancel_Button")
        self.user_textBrowser = QtWidgets.QTextBrowser(Form)
        self.user_textBrowser.setGeometry(QtCore.QRect(270, 30, 221, 101))
        self.user_textBrowser.setObjectName("user_textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户登录"))
        self.user_label.setText(_translate("Form", "用户名"))
        self.pwd_label.setText(_translate("Form", "密码"))
        self.login_Button.setText(_translate("Form", "登录"))
        self.cancel_Button.setText(_translate("Form", "退出"))

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    Form=QtWidgets.QMainWindow()
    ui=Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())