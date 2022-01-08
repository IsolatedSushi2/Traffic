from PyQt5 import QtCore, QtGui, QtWidgets
from src.ui.camSelectui import Ui_Form


class CameraSelector(QtWidgets.QWidget):
    newCamListSignal = QtCore.pyqtSignal(object)
    
    def __init__(self, camNames, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.camNames = camNames
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.connectCamButtons()
        
        self.buttonColors = {True: "background-color: rgba(181, 181, 181, 100);", 
                            False: "background-color: rgba(181, 181, 181, 255);"}

        self.selectedCams = dict.fromkeys(camNames, False)

    def connectCamButtons(self):
        for camName in self.camNames:
            currButton = getattr(self.ui, camName)
            currButton.clicked.connect(self.clickedCamButton)

    @QtCore.pyqtSlot()
    def clickedCamButton(self):
        # Get which button was clicked, and store if it is selected
        camName = self.sender().objectName()
        currSelected = self.selectedCams[camName]
        self.selectedCams[camName] = not currSelected

        # Color the button
        self.sender().setStyleSheet(self.buttonColors[currSelected])

        self.emitNewCamList()

    # Emit the camera names which are selected
    def emitNewCamList(self):
        dictItems = self.selectedCams.items()
        selCamList = [camName for camName, sel in dictItems if sel]
        self.newCamListSignal.emit(selCamList)