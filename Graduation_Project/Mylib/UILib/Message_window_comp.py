# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Message_window_comp.ui'
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
        self.gridLayout.setContentsMargins(5, 5, 30, 5)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-left: 2px solid white;\n"
"border-top: 2px solid white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-left: 2px solid white;")
        self.label_2.setIndent(10)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.Lab_X_PosAbs = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_X_PosAbs.setFont(font)
        self.Lab_X_PosAbs.setStyleSheet("")
        self.Lab_X_PosAbs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lab_X_PosAbs.setIndent(10)
        self.Lab_X_PosAbs.setObjectName("Lab_X_PosAbs")
        self.gridLayout_2.addWidget(self.Lab_X_PosAbs, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-left: 2px solid white;")
        self.label_3.setIndent(10)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.Lab_Y_PosAbs = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Y_PosAbs.setFont(font)
        self.Lab_Y_PosAbs.setStyleSheet("")
        self.Lab_Y_PosAbs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lab_Y_PosAbs.setIndent(10)
        self.Lab_Y_PosAbs.setObjectName("Lab_Y_PosAbs")
        self.gridLayout_2.addWidget(self.Lab_Y_PosAbs, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-left: 2px solid white;")
        self.label_4.setIndent(10)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.Lab_Z_PosAbs = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Z_PosAbs.setFont(font)
        self.Lab_Z_PosAbs.setStyleSheet("")
        self.Lab_Z_PosAbs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lab_Z_PosAbs.setIndent(10)
        self.Lab_Z_PosAbs.setObjectName("Lab_Z_PosAbs")
        self.gridLayout_2.addWidget(self.Lab_Z_PosAbs, 3, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-top: 2px solid white;\n"
"border-right: 2px solid rgb(140,140,140);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setIndent(10)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.Lab_X_PosRel = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_X_PosRel.setFont(font)
        self.Lab_X_PosRel.setStyleSheet("border-right: 2px solid rgb(140,140,140);")
        self.Lab_X_PosRel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lab_X_PosRel.setIndent(10)
        self.Lab_X_PosRel.setObjectName("Lab_X_PosRel")
        self.gridLayout_3.addWidget(self.Lab_X_PosRel, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setIndent(10)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.Lab_Y_PosRel = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Y_PosRel.setFont(font)
        self.Lab_Y_PosRel.setStyleSheet("border-right: 2px solid rgb(140,140,140);")
        self.Lab_Y_PosRel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lab_Y_PosRel.setIndent(10)
        self.Lab_Y_PosRel.setObjectName("Lab_Y_PosRel")
        self.gridLayout_3.addWidget(self.Lab_Y_PosRel, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setIndent(10)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)
        self.Lab_Z_PosRel = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Z_PosRel.setFont(font)
        self.Lab_Z_PosRel.setStyleSheet("border-right: 2px solid rgb(140,140,140);")
        self.Lab_Z_PosRel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lab_Z_PosRel.setIndent(10)
        self.Lab_Z_PosRel.setObjectName("Lab_Z_PosRel")
        self.gridLayout_3.addWidget(self.Lab_Z_PosRel, 3, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_15 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border-left: 2px solid white;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border-left: 2px solid white;")
        self.label_16.setIndent(10)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)
        self.Lab_X_PosComp = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_X_PosComp.setFont(font)
        self.Lab_X_PosComp.setStyleSheet("")
        self.Lab_X_PosComp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lab_X_PosComp.setIndent(10)
        self.Lab_X_PosComp.setObjectName("Lab_X_PosComp")
        self.gridLayout_4.addWidget(self.Lab_X_PosComp, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border-left: 2px solid white;")
        self.label_17.setIndent(10)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        self.Lab_Y_PosComp = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Y_PosComp.setFont(font)
        self.Lab_Y_PosComp.setStyleSheet("")
        self.Lab_Y_PosComp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lab_Y_PosComp.setIndent(10)
        self.Lab_Y_PosComp.setObjectName("Lab_Y_PosComp")
        self.gridLayout_4.addWidget(self.Lab_Y_PosComp, 2, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border-left: 2px solid white;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.label_18.setIndent(10)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)
        self.Lab_Z_PosComp = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Z_PosComp.setFont(font)
        self.Lab_Z_PosComp.setStyleSheet("border-bottom: 2px solid rgb(140,140,140);")
        self.Lab_Z_PosComp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lab_Z_PosComp.setIndent(10)
        self.Lab_Z_PosComp.setObjectName("Lab_Z_PosComp")
        self.gridLayout_4.addWidget(self.Lab_Z_PosComp, 3, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 2)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setStyleSheet("border-bottom: 2px solid rgb(140,140,140);\n"
"border-right: 2px solid rgb(140,140,140);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "绝对坐标"))
        self.label_2.setText(_translate("Form", "X"))
        self.Lab_X_PosAbs.setText(_translate("Form", "0.000"))
        self.label_3.setText(_translate("Form", "Y"))
        self.Lab_Y_PosAbs.setText(_translate("Form", "0.000"))
        self.label_4.setText(_translate("Form", "Z"))
        self.Lab_Z_PosAbs.setText(_translate("Form", "0.000"))
        self.label_8.setText(_translate("Form", "相对坐标"))
        self.label_9.setText(_translate("Form", "X"))
        self.Lab_X_PosRel.setText(_translate("Form", "0.000"))
        self.label_10.setText(_translate("Form", "Y"))
        self.Lab_Y_PosRel.setText(_translate("Form", "0.000"))
        self.label_11.setText(_translate("Form", "Z"))
        self.Lab_Z_PosRel.setText(_translate("Form", "0.000"))
        self.label_15.setText(_translate("Form", "机械坐标"))
        self.label_16.setText(_translate("Form", "X"))
        self.Lab_X_PosComp.setText(_translate("Form", "0.000"))
        self.label_17.setText(_translate("Form", "Y"))
        self.Lab_Y_PosComp.setText(_translate("Form", "0.000"))
        self.label_18.setText(_translate("Form", "Z"))
        self.Lab_Z_PosComp.setText(_translate("Form", "0.000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
