# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Program_EditWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(349, 22)
        Form.setMinimumSize(QtCore.QSize(349, 22))
        Form.setMaximumSize(QtCore.QSize(349, 22))
        Form.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(96, 224, 224);\n"
"border-top: 2px solid white;\n"
"border-left: 2px solid white;\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.label.setIndent(5)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ProgramTextEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ProgramTextEdit.setFont(font)
        self.ProgramTextEdit.setStyleSheet("background-color: rgb(96, 224, 224);\n"
"border-top: 2px solid white;\n"
"border-right: 2px solid rgb(140,140,140);\n"
"border-bottom: 2px solid rgb(140,140,140);")
        self.ProgramTextEdit.setObjectName("ProgramTextEdit")
        self.horizontalLayout.addWidget(self.ProgramTextEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 16)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", ">"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
