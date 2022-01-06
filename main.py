from src.ui.ui import Ui_MainWindow
from src.ui.mainwindow import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


if __name__ == "__main__":

    # Create the window and setup the UI
    app = QtWidgets.QApplication(sys.argv)
    QMainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(QMainWindow)
    QMainWindow.show()

    # Create and run the application
    window = MainWindow(ui)
    sys.exit(app.exec_())