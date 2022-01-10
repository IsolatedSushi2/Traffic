import os
from pandaset import DataSet
from src.constants import DEFAULT_DATA_SEQUENCE
from src.ui.vispyPlot2 import VispyPlot
from src.renderers.renderData import RenderData

# Acts as the "mainwindow"


class MainWindow:
    def __init__(self, ui):
        self.ui = ui
        self.currSeq = None

        self.useDefaultDataset()
        self.renderDatas = []

    def setupSlider(self):
        amount = len(self.renderDatas)
        self.ui.frameSlider.setMaximum(amount - 1)
        self.ui.frameSlider.valueChanged.connect(self.render)

    def useDefaultDataset(self):
        self.getDataset(DEFAULT_DATA_SEQUENCE)

    def getDataset(self, path):
        self.dataSet = DataSet(path)

        # TODO user should be able to select the sequence
        print(self.dataSet.sequences())
        firstSequence = self.dataSet.sequences()[8]
        self.currSeq = self.dataSet["012"]

        self.generateRenderDatas(self.currSeq)

        camNames = self.currSeq.camera.keys()
        self.plot = VispyPlot(self.ui, camNames, self.renderDatas)
        self.setupSlider()

        self.render()

    # Get the renderData (for now, just do the first frame)
    def generateRenderDatas(self, sequence):
        sequence.load()
        frameAmount = len(sequence.timestamps.data)

        self.renderDatas = [RenderData(sequence, ind)
                            for ind in range(0, frameAmount, 5)]
        
    def render(self):

        if not self.currSeq:
            return
        self.plot.update()
