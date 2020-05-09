# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prog_window_dir.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 229)
        Form.setMinimumSize(QtCore.QSize(700, 229))
        Form.setMaximumSize(QtCore.QSize(700, 229))
        Form.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-top: 2px solid white;\n"
"border-left: 2px solid white;")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.Lab_ProgramName = QtWidgets.QPlainTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lab_ProgramName.setFont(font)
        self.Lab_ProgramName.setStyleSheet("border-left: 2px solid white;\n"
"border-top: 0px solid;\n"
"border-right: 0px solid;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.Lab_ProgramName.setObjectName("Lab_ProgramName")
        self.verticalLayout.addWidget(self.Lab_ProgramName)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 19)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-top: 2px solid white;")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.Lab_ProgramComment = QtWidgets.QPlainTextEdit(self.widget_2)
        self.Lab_ProgramComment.setStyleSheet("border-left: 0px solid;\n"
"border-top: 0px solid;\n"
"border-right: 0px solid;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.Lab_ProgramComment.setObjectName("Lab_ProgramComment")
        self.verticalLayout_2.addWidget(self.Lab_ProgramComment)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 19)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-top: 2px solid white;")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.Lab_ProgramSize = QtWidgets.QPlainTextEdit(self.widget_3)
        self.Lab_ProgramSize.setStyleSheet("border-left: 0px solid;\n"
"border-top: 0px solid;\n"
"border-right: 0px solid;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.Lab_ProgramSize.setObjectName("Lab_ProgramSize")
        self.verticalLayout_3.addWidget(self.Lab_ProgramSize)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 19)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-top: 2px solid white;\n"
"border-right: 2px solid rgb(140,140,140);")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.Lab_ProgramUpdateTime = QtWidgets.QPlainTextEdit(self.widget_4)
        self.Lab_ProgramUpdateTime.setStyleSheet("border-left: 0px solid;\n"
"border-top: 0px solid;\n"
"border-right: 2px solid rgb(140,140,140);\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.Lab_ProgramUpdateTime.setObjectName("Lab_ProgramUpdateTime")
        self.verticalLayout_4.addWidget(self.Lab_ProgramUpdateTime)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 19)
        self.horizontalLayout.addWidget(self.widget_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "PROGRAM"))
        self.Lab_ProgramName.setPlainText(_translate("Form", "O0001\n"
"O0002\n"
"O0003"))
        self.label_8.setText(_translate("Form", "COMMENT"))
        self.label_11.setText(_translate("Form", "SIZE(CHAR.)"))
        self.label_12.setText(_translate("Form", "UPDATE TIME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
