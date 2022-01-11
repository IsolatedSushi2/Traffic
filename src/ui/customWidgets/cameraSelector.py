from PyQt5 import QtCore, QtGui, QtWidgets
from src.ui.camSelectui import Ui_Form


class CameraSelector(QtWidgets.QWidget):
    newCamListSignal = QtCore.pyqtSignal()
    renderPathSignal = QtCore.pyqtSignal()

    def __init__(self, camNames, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.camNames = camNames
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.renderPath = False

        defaultStylesheet = """
QPushButton{{
background-color: {color};
border-style: solid;
border-color: rgba(0,0,0,50)
;
border-width: 1px;
border-radius: 10px;
}}

QPushButton:hover {{
	background-color: rgb(33, 37, 43);
}}
QPushButton:pressed {{	
	background-color: rgb(85, 170, 255);
}}"""
        selectedColor = defaultStylesheet.format(color="rgba(181, 181, 181, 255);")
        notSelectedColor = defaultStylesheet.format(color="rgba(181, 181, 181, 100);")

        self.buttonColors = {True: selectedColor,
                             False: notSelectedColor}

        self.selectedCams = dict.fromkeys(camNames, True)
        self.updateCamList()

        self.connectCamButtons()

    def switchRenderPath(self):
        self.renderPath = not self.renderPath
        self.renderPathSignal.emit()

    def connectCamButtons(self):
        self.ui.carPositionBtn.clicked.connect(self.switchRenderPath)
        for camName in self.camNames:
            currButton = getattr(self.ui, camName)
            currButton.clicked.connect(self.clickedCamButton)
            currSelected = self.selectedCams[camName]
            print(currSelected)
            currButton.setStyleSheet(self.buttonColors[currSelected])

    @QtCore.pyqtSlot()
    def clickedCamButton(self):
        # Get which button was clicked, and store if it is selected
        camName = self.sender().objectName()
        currSelected = self.selectedCams[camName]
        self.selectedCams[camName] = not currSelected

        # Color the button
        self.sender().setStyleSheet(self.buttonColors[not currSelected])
        self.updateCamList()
        self.emitNewCamList()

    # Emit the camera names which are selected
    def emitNewCamList(self):
        
        self.newCamListSignal.emit()

    def updateCamList(self):
        dictItems = self.selectedCams.items()
        self.selCamList = [camName for camName, sel in dictItems if sel]
