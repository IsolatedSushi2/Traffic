import os
from pandaset import DataSet
from src.constants import DEFAULT_DATA_SEQUENCE
from src.ui.vispyPlot2 import VispyPlot
from src.renderers.renderData import RenderData

# Acts as the "mainwindow"


class MainWindow:
    def __init__(self, ui):
        self.ui = ui

        self.useDefaultDataset()
        self.currSeq = None
        self.renderDatas = []

    def useDefaultDataset(self):
        self.getDataset(DEFAULT_DATA_SEQUENCE)

    def getDataset(self, path):
        self.dataSet = DataSet(path)

        # TODO user should be able to select the sequence
        firstSequence = self.dataSet.sequences()[0]
        self.currSeq = self.dataSet[firstSequence]

        self.generateRenderDatas(self.currSeq)

        camNames = self.currSeq.camera.keys()
        self.plot = VispyPlot(self.ui, camNames, self.renderDatas)

        self.render()

    # Get the renderData (for now, just do the first frame)
    def generateRenderDatas(self, sequence):
        sequence.load()
        frameAmount = len(sequence.timestamps.data)
        frameAmount = 1

        self.renderDatas = [RenderData(sequence, ind)
                            for ind in range(0, frameAmount, 10)]
        
    def render(self):

        if not self.currSeq:
            return

        self.plot.renderPoints()
