from PyQt5 import QtCore, QtGui, QtWidgets
from src.ui.legendSelector import Ui_Form


class LegendSelector(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def setupLegend(self, classNames):
        return

