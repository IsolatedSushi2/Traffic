from PyQt5 import QtCore, QtGui, QtWidgets
from src.ui.legendSelector import Ui_Form
from src.constants import SEMSEG_COLORMAP
import numpy as np

# Handles the UI for the Legend Selector widget
class LegendSelector(QtWidgets.QWidget):
    clickedLabelSignal = QtCore.pyqtSignal()

    def __init__(self, renderData, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.renderData = renderData
        self.alphaChannel = {True: 255, False: 40}

        self.selectedClasses = np.ones(42, dtype=np.bool)
        self.setupLegend(renderData.classNames)

    # Initial legend
    def setupLegend(self, classNames):
        print(classNames)
        for index, name in enumerate(classNames):
            currRow, currWidget = self.getRow(name, index)
            self.ui.listWidget.addItem(currRow)
            self.ui.listWidget.setItemWidget(currRow, currWidget)

        self.ui.listWidget.itemClicked.connect(self.clickedItem)

    @QtCore.pyqtSlot()
    def clickedItem(self):
        
        index = self.sender().selectedIndexes()[0].row()

        lastValue = self.selectedClasses[index]
        self.selectedClasses[index] = ~lastValue

        rowWidget = self.ui.listWidget.item(index)
        rowWidget = self.ui.listWidget.itemWidget(rowWidget)

        frameWidget = rowWidget.layout().itemAt(0).widget()
        labelWidget = rowWidget.layout().itemAt(1).widget()
        widgetColor, labelColor = self.getWidgetColor(index)

        frameWidget.setStyleSheet(
            "background-color: rgba{}; border-radius:10px;".format(tuple(widgetColor)))
        labelWidget.setStyleSheet("color: rgba{}".format(tuple(labelColor)))

        self.clickedLabelSignal.emit()

    # Get the legend color
    def getWidgetColor(self, index):
        selectedIndex = self.selectedClasses[index]
        alphaChannel = self.alphaChannel[selectedIndex]

        frameColor = np.concatenate((SEMSEG_COLORMAP[index], [alphaChannel]))
        labelColor = np.concatenate((np.array([255, 255, 255]), [alphaChannel]))

        return frameColor, labelColor

    #Create the UI for the rows
    def getRow(self, className, index):
        currRow = QtWidgets.QListWidgetItem()
        # Create widget
        widget = QtWidgets.QWidget()
        widgetFrame = QtWidgets.QFrame()

        frameColor, labelColor = self.getWidgetColor(index)
        frameStylesheet = "background-color: rgba{}; border-radius:10px;".format(
            tuple(frameColor))
        widgetFrame.setStyleSheet(frameStylesheet)

        widgetFrame.setMinimumWidth(20)
        widgetFrame.setMinimumHeight(20)
        widgetFrame.setMaximumWidth(20)
        widgetFrame.setMaximumHeight(20)


        widgetText = QtWidgets.QLabel(className)
        widgetText.setStyleSheet("color: rgba{}".format(tuple(labelColor)))
       
        font = QtGui.QFont('Segoe UI', 10)
        font.setBold(True)
        widgetText.setFont(font)
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.setContentsMargins(0, 0, 0, 0)
        widgetLayout.addWidget(widgetFrame)
        widgetLayout.addWidget(widgetText)
        widgetLayout.addStretch()

        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)
        currRow.setSizeHint(widget.sizeHint())

        return currRow, widget