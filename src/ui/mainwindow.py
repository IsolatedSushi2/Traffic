import os
from pandaset import DataSet
from src.constants import DEFAULT_DATA_SEQUENCE
from src.ui.vispyPlot import VispyPlot

# Acts as the "mainwindow"
class MainWindow:
    def __init__(self, ui):
        self.ui = ui

        self.useDefaultDataset()

    def useDefaultDataset(self):
        self.getDataset(DEFAULT_DATA_SEQUENCE)
    
    def getDataset(self, path):
        self.dataSet = DataSet(path)
        # TODO user should be able to select the sequence
        firstSequence = self.dataSet.sequences()[0]
        print("Sequence:", firstSequence)
        self.currSeq = self.dataSet[firstSequence]

        self.plot = VispyPlot(self.ui, self.currSeq)
