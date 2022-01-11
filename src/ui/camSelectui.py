# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cameraSelector.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(120, 190)
        Form.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgba(181, 181, 181, 100);\n"
"border-style: solid;\n"
"border-color: rgba(0,0,0,50)\n"
";\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.left_camera = QtWidgets.QPushButton(Form)
        self.left_camera.setGeometry(QtCore.QRect(0, 90, 20, 70))
        self.left_camera.setText("")
        self.left_camera.setObjectName("left_camera")
        self.right_camera = QtWidgets.QPushButton(Form)
        self.right_camera.setGeometry(QtCore.QRect(100, 90, 20, 70))
        self.right_camera.setText("")
        self.right_camera.setObjectName("right_camera")
        self.front_camera = QtWidgets.QPushButton(Form)
        self.front_camera.setGeometry(QtCore.QRect(30, 0, 60, 20))
        self.front_camera.setStyleSheet("")
        self.front_camera.setText("")
        self.front_camera.setObjectName("front_camera")
        self.front_right_camera = QtWidgets.QPushButton(Form)
        self.front_right_camera.setGeometry(QtCore.QRect(95, 30, 20, 40))
        self.front_right_camera.setText("")
        self.front_right_camera.setObjectName("front_right_camera")
        self.front_left_camera = QtWidgets.QPushButton(Form)
        self.front_left_camera.setGeometry(QtCore.QRect(5, 30, 20, 40))
        self.front_left_camera.setText("")
        self.front_left_camera.setObjectName("front_left_camera")
        self.back_camera = QtWidgets.QPushButton(Form)
        self.back_camera.setGeometry(QtCore.QRect(25, 170, 70, 20))
        self.back_camera.setText("")
        self.back_camera.setObjectName("back_camera")
        self.carPositionBtn = QtWidgets.QPushButton(Form)
        self.carPositionBtn.setGeometry(QtCore.QRect(25, 25, 70, 140))
        self.carPositionBtn.setStyleSheet("QPushButton{\n"
"background-image: url(:/newPrefix/icons/smallCar.png);\n"
"background-color: transparent;\n"
"border-style: solid;\n"
"border-color: rgba(0,0,0,50);\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.carPositionBtn.setText("")
        self.carPositionBtn.setObjectName("carPositionBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import cameraSelector_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
