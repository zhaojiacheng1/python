# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prog_window_probase.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(349, 175)
        Form.setMinimumSize(QtCore.QSize(349, 175))
        Form.setMaximumSize(QtCore.QSize(349, 175))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Lab_ProgramEdit = QtWidgets.QPlainTextEdit(Form)
        self.Lab_ProgramEdit.setStyleSheet("background-color: rgb(255, 204, 204);\n"
"border-left: 2px solid white;\n"
"border-top: 2px solid white;\n"
"border-bottom: 2px solid rgb(140,140,140);\n"
"border-right: 2px solid rgb(140,140,140);")
        self.Lab_ProgramEdit.setObjectName("Lab_ProgramEdit")
        self.verticalLayout.addWidget(self.Lab_ProgramEdit)

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
