# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Parameter_window_rel.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 160)
        Form.setMinimumSize(QtCore.QSize(200, 160))
        Form.setMaximumSize(QtCore.QSize(200, 160))
        Form.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-left: 2px solid white;\n"
"border-top: 2px solid white;\n"
"border-right: 2px solid rgb(140,140,140);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-left: 2px solid white;\n"
"border-right: 2px solid rgb(140,140,140);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-left: 2px solid white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.Lab_X_Pos = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_X_Pos.setFont(font)
        self.Lab_X_Pos.setStyleSheet("border-right: 2px solid rgb(140,140,140);")
        self.Lab_X_Pos.setText("")
        self.Lab_X_Pos.setObjectName("Lab_X_Pos")
        self.gridLayout.addWidget(self.Lab_X_Pos, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-left: 2px solid white;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.Lab_Y_Pos = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Y_Pos.setFont(font)
        self.Lab_Y_Pos.setStyleSheet("border-right: 2px solid rgb(140,140,140);")
        self.Lab_Y_Pos.setText("")
        self.Lab_Y_Pos.setObjectName("Lab_Y_Pos")
        self.gridLayout.addWidget(self.Lab_Y_Pos, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-left: 2px solid white;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.Lab_Z_Pos = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Z_Pos.setFont(font)
        self.Lab_Z_Pos.setStyleSheet("border-right: 2px solid rgb(140,140,140);\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.Lab_Z_Pos.setText("")
        self.Lab_Z_Pos.setObjectName("Lab_Z_Pos")
        self.gridLayout.addWidget(self.Lab_Z_Pos, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "现在位置"))
        self.label_2.setText(_translate("Form", "相对坐标"))
        self.label_3.setText(_translate("Form", "X"))
        self.label_4.setText(_translate("Form", "Y"))
        self.label_5.setText(_translate("Form", "Z"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
