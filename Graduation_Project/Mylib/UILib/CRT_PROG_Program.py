# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CRT_PROG_Program.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 424)
        Form.setMinimumSize(QtCore.QSize(700, 424))
        Form.setMaximumSize(QtCore.QSize(700, 424))
        Form.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(96, 224, 224);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(153, 255, 244);")
        self.label.setIndent(10)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("background-color: rgb(153, 255, 244);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(153, 255, 244);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(153, 255, 244);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.programwindow = QtWidgets.QWidget(self.widget_2)
        self.programwindow.setStyleSheet("")
        self.programwindow.setObjectName("programwindow")
        self.gridLayout = QtWidgets.QGridLayout(self.programwindow)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addWidget(self.programwindow)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Lab_ProgramEdit = QtWidgets.QWidget(self.widget_5)
        self.Lab_ProgramEdit.setStyleSheet("")
        self.Lab_ProgramEdit.setObjectName("Lab_ProgramEdit")
        self.horizontalLayout_5.addWidget(self.Lab_ProgramEdit)
        self.widget_10 = QtWidgets.QWidget(self.widget_5)
        self.widget_10.setStyleSheet("")
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_11 = QtWidgets.QWidget(self.widget_10)
        self.widget_11.setStyleSheet("")
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_3.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_10)
        self.widget_12.setStyleSheet("")
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.Lab_OSper = QtWidgets.QLabel(self.widget_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_OSper.setFont(font)
        self.Lab_OSper.setStyleSheet("")
        self.Lab_OSper.setIndent(10)
        self.Lab_OSper.setObjectName("Lab_OSper")
        self.horizontalLayout_6.addWidget(self.Lab_OSper)
        self.label_9 = QtWidgets.QLabel(self.widget_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.Lab_Lper = QtWidgets.QLabel(self.widget_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Lper.setFont(font)
        self.Lab_Lper.setStyleSheet("")
        self.Lab_Lper.setIndent(10)
        self.Lab_Lper.setObjectName("Lab_Lper")
        self.horizontalLayout_6.addWidget(self.Lab_Lper)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 1)
        self.verticalLayout_3.addWidget(self.widget_12)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout_5.addWidget(self.widget_10)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setStyleSheet("")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setStyleSheet("")
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Lab_Mode = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Mode.setFont(font)
        self.Lab_Mode.setStyleSheet("border-left: 2px solid white;\n"
"border-top: 2px solid white;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.Lab_Mode.setAlignment(QtCore.Qt.AlignCenter)
        self.Lab_Mode.setObjectName("Lab_Mode")
        self.horizontalLayout_4.addWidget(self.Lab_Mode)
        self.label_6 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-top: 2px solid white;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-top: 2px solid white;\n"
"border-right: 2px solid black;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.Lab_EMG = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_EMG.setFont(font)
        self.Lab_EMG.setStyleSheet("border-top: 2px solid white;\n"
"border-left: 2px solid white;\n"
"border-right: 2px solid black;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.Lab_EMG.setAlignment(QtCore.Qt.AlignCenter)
        self.Lab_EMG.setObjectName("Lab_EMG")
        self.horizontalLayout_4.addWidget(self.Lab_EMG)
        self.Lab_ALM = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_ALM.setFont(font)
        self.Lab_ALM.setStyleSheet("border-left: 2px solid white;\n"
"border-top: 2px solid white;\n"
"border-right: 2px solid black;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.Lab_ALM.setAlignment(QtCore.Qt.AlignCenter)
        self.Lab_ALM.setObjectName("Lab_ALM")
        self.horizontalLayout_4.addWidget(self.Lab_ALM)
        self.Lab_Date = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lab_Date.setFont(font)
        self.Lab_Date.setStyleSheet("border-left: 2px solid white;\n"
"border-top: 2px solid white;\n"
"border-right: 2px solid black;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.Lab_Date.setAlignment(QtCore.Qt.AlignCenter)
        self.Lab_Date.setObjectName("Lab_Date")
        self.horizontalLayout_4.addWidget(self.Lab_Date)
        self.label_11 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-left: 2px solid white;\n"
"border-top: 2px solid white;\n"
"border-right: 2px solid black;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 9)
        self.horizontalLayout_4.setStretch(2, 10)
        self.horizontalLayout_4.setStretch(3, 10)
        self.horizontalLayout_4.setStretch(4, 9)
        self.horizontalLayout_4.setStretch(5, 16)
        self.horizontalLayout_4.setStretch(6, 4)
        self.horizontalLayout_3.addWidget(self.widget_8)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout_2.setStretch(0, 48)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Btn_BACK = QtWidgets.QPushButton(self.widget_3)
        self.Btn_BACK.setMinimumSize(QtCore.QSize(20, 50))
        self.Btn_BACK.setMaximumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_BACK.setFont(font)
        self.Btn_BACK.setStyleSheet("color: rgb(3, 255, 255);")
        self.Btn_BACK.setText("")
        self.Btn_BACK.setObjectName("Btn_BACK")
        self.horizontalLayout_2.addWidget(self.Btn_BACK)
        self.Btn_One = CRTSoftBtn(self.widget_3)
        self.Btn_One.setMinimumSize(QtCore.QSize(65, 50))
        self.Btn_One.setMaximumSize(QtCore.QSize(65, 50))
        self.Btn_One.setStyleSheet("")
        self.Btn_One.setText("")
        self.Btn_One.setObjectName("Btn_One")
        self.horizontalLayout_2.addWidget(self.Btn_One)
        self.Btn_Two = CRTSoftBtn(self.widget_3)
        self.Btn_Two.setMinimumSize(QtCore.QSize(65, 50))
        self.Btn_Two.setMaximumSize(QtCore.QSize(65, 50))
        self.Btn_Two.setStyleSheet("")
        self.Btn_Two.setText("")
        self.Btn_Two.setObjectName("Btn_Two")
        self.horizontalLayout_2.addWidget(self.Btn_Two)
        self.Btn_Three = CRTSoftBtn(self.widget_3)
        self.Btn_Three.setMinimumSize(QtCore.QSize(65, 50))
        self.Btn_Three.setMaximumSize(QtCore.QSize(65, 50))
        self.Btn_Three.setStyleSheet("")
        self.Btn_Three.setText("")
        self.Btn_Three.setObjectName("Btn_Three")
        self.horizontalLayout_2.addWidget(self.Btn_Three)
        self.Btn_Four = CRTSoftBtn(self.widget_3)
        self.Btn_Four.setMinimumSize(QtCore.QSize(65, 50))
        self.Btn_Four.setMaximumSize(QtCore.QSize(65, 50))
        self.Btn_Four.setStyleSheet("")
        self.Btn_Four.setText("")
        self.Btn_Four.setObjectName("Btn_Four")
        self.horizontalLayout_2.addWidget(self.Btn_Four)
        self.Btn_Five = CRTSoftBtn(self.widget_3)
        self.Btn_Five.setMinimumSize(QtCore.QSize(65, 50))
        self.Btn_Five.setMaximumSize(QtCore.QSize(65, 50))
        self.Btn_Five.setStyleSheet("")
        self.Btn_Five.setText("")
        self.Btn_Five.setObjectName("Btn_Five")
        self.horizontalLayout_2.addWidget(self.Btn_Five)
        self.Btn_Six = CRTSoftBtn(self.widget_3)
        self.Btn_Six.setMinimumSize(QtCore.QSize(65, 50))
        self.Btn_Six.setMaximumSize(QtCore.QSize(65, 50))
        self.Btn_Six.setStyleSheet("")
        self.Btn_Six.setText("")
        self.Btn_Six.setObjectName("Btn_Six")
        self.horizontalLayout_2.addWidget(self.Btn_Six)
        self.Btn_Seven = CRTSoftBtn(self.widget_3)
        self.Btn_Seven.setMinimumSize(QtCore.QSize(65, 50))
        self.Btn_Seven.setMaximumSize(QtCore.QSize(65, 50))
        self.Btn_Seven.setStyleSheet("")
        self.Btn_Seven.setText("")
        self.Btn_Seven.setObjectName("Btn_Seven")
        self.horizontalLayout_2.addWidget(self.Btn_Seven)
        self.Btn_Eight = CRTSoftBtn(self.widget_3)
        self.Btn_Eight.setMinimumSize(QtCore.QSize(65, 50))
        self.Btn_Eight.setMaximumSize(QtCore.QSize(65, 50))
        self.Btn_Eight.setStyleSheet("")
        self.Btn_Eight.setText("")
        self.Btn_Eight.setObjectName("Btn_Eight")
        self.horizontalLayout_2.addWidget(self.Btn_Eight)
        self.Btn_Nine = CRTSoftBtn(self.widget_3)
        self.Btn_Nine.setMinimumSize(QtCore.QSize(65, 50))
        self.Btn_Nine.setMaximumSize(QtCore.QSize(65, 50))
        self.Btn_Nine.setStyleSheet("")
        self.Btn_Nine.setText("")
        self.Btn_Nine.setObjectName("Btn_Nine")
        self.horizontalLayout_2.addWidget(self.Btn_Nine)
        self.Btn_Ten = CRTSoftBtn(self.widget_3)
        self.Btn_Ten.setMinimumSize(QtCore.QSize(65, 50))
        self.Btn_Ten.setMaximumSize(QtCore.QSize(65, 50))
        self.Btn_Ten.setStyleSheet("")
        self.Btn_Ten.setText("")
        self.Btn_Ten.setObjectName("Btn_Ten")
        self.horizontalLayout_2.addWidget(self.Btn_Ten)
        self.Btn_GO = QtWidgets.QPushButton(self.widget_3)
        self.Btn_GO.setMinimumSize(QtCore.QSize(20, 50))
        self.Btn_GO.setMaximumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_GO.setFont(font)
        self.Btn_GO.setStyleSheet("color: rgb(3, 255, 255);")
        self.Btn_GO.setText("")
        self.Btn_GO.setObjectName("Btn_GO")
        self.horizontalLayout_2.addWidget(self.Btn_GO)
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 71)
        self.verticalLayout.setStretch(2, 10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "程式"))
        self.label_3.setText(_translate("Form", "O0001"))
        self.label_4.setText(_translate("Form", "N00000"))
        self.label_5.setText(_translate("Form", "OS"))
        self.Lab_OSper.setText(_translate("Form", "50%"))
        self.label_9.setText(_translate("Form", "L"))
        self.Lab_Lper.setText(_translate("Form", "100%"))
        self.Lab_Mode.setText(_translate("Form", "REF"))
        self.label_6.setText(_translate("Form", "***"))
        self.label_7.setText(_translate("Form", "***"))
        self.Lab_EMG.setText(_translate("Form", "EMG"))
        self.Lab_ALM.setText(_translate("Form", "***"))
        self.Lab_Date.setText(_translate("Form", "14:18:25"))
from CRT_Soft_Btn import CRTSoftBtn


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
