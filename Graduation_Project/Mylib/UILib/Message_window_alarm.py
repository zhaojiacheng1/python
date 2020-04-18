# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Message_window_alarm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(349, 195)
        Form.setMinimumSize(QtCore.QSize(349, 195))
        Form.setMaximumSize(QtCore.QSize(349, 195))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Lab_alarmwindow = QtWidgets.QPlainTextEdit(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Lab_alarmwindow.setFont(font)
        self.Lab_alarmwindow.setStyleSheet("background-color: rgb(255, 204, 204);")
        self.Lab_alarmwindow.setObjectName("Lab_alarmwindow")
        self.horizontalLayout.addWidget(self.Lab_alarmwindow)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
