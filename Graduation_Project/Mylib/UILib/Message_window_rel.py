# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Message_window_rel.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 207)
        Form.setMinimumSize(QtCore.QSize(350, 207))
        Form.setMaximumSize(QtCore.QSize(350, 207))
        Form.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(33, 40, -1, 40)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setIndent(20)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Lab_X_Pos = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_X_Pos.setFont(font)
        self.Lab_X_Pos.setStyleSheet("")
        self.Lab_X_Pos.setObjectName("Lab_X_Pos")
        self.gridLayout.addWidget(self.Lab_X_Pos, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setIndent(20)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.Lab_Y_Pos = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Y_Pos.setFont(font)
        self.Lab_Y_Pos.setStyleSheet("")
        self.Lab_Y_Pos.setObjectName("Lab_Y_Pos")
        self.gridLayout.addWidget(self.Lab_Y_Pos, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setIndent(20)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.Lab_Z_Pos = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Z_Pos.setFont(font)
        self.Lab_Z_Pos.setStyleSheet("")
        self.Lab_Z_Pos.setObjectName("Lab_Z_Pos")
        self.gridLayout.addWidget(self.Lab_Z_Pos, 2, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "X"))
        self.Lab_X_Pos.setText(_translate("Form", "0.000"))
        self.label_2.setText(_translate("Form", "Y"))
        self.Lab_Y_Pos.setText(_translate("Form", "0.000"))
        self.label_3.setText(_translate("Form", "Z"))
        self.Lab_Z_Pos.setText(_translate("Form", "0.000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
