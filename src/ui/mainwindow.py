import os
from pandaset import DataSet
from src.constants import DEFAULT_DATA_SEQUENCE, CHOSEN_SEQUENCE
from src.ui.vispyPlot2 import VispyPlot
from src.renderers.renderData import RenderData

# Acts as the "mainwindow"


class MainWindow:
    def __init__(self, ui):
        self.ui = ui
        self.currSeq = None

        self.useDefaultDataset()
        self.renderData = None

    def setupSlider(self):
        amount = len(self.renderData.renderFrameList)
        self.ui.frameSlider.setMaximum(amount - 1)
        self.ui.frameSlider.valueChanged.connect(self.render)

    def useDefaultDataset(self):
        self.getDataset(DEFAULT_DATA_SEQUENCE)

    def getDataset(self, path):
        self.dataSet = DataSet(path)

        # TODO user should be able to select the sequence
        print(self.dataSet.sequences(with_semseg=True))
        self.currSeq = self.dataSet[CHOSEN_SEQUENCE]

        self.generateRenderData(self.currSeq)

        camNames = self.currSeq.camera.keys()
        self.plot = VispyPlot(self.ui, camNames, self.renderData)
        self.setupSlider()

        self.render()

    # Get the renderData (for now, just do the first frame)
    def generateRenderData(self, sequence):
        sequence.load()
        frameAmount = len(sequence.timestamps.data)

        self.renderData = RenderData(sequence, range(0, frameAmount, 5))

    def render(self):

        if not self.currSeq:
            return

        self.plot.update()
