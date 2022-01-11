import src.extractors.pointCloudExtractor as PCE
import src.extractors.positionExtractor as PE
from src.constants import SEMSEG_COLORMAP, CLASS_NAMES
import numpy as np

#  Stores all the renders for a single frame (from all the sensors)
class RenderFrame:

    def __init__(self, sequence, frameIndex):
        self.seq = sequence  # Load the data
        self.frameIndex = frameIndex

        self.PCpos = PCE.getOriginalPC(self.seq, self.frameIndex)
        self.carPositions = PE.getCarPositions(self.seq)
        self.cols, self.colIndices = PCE.getColorIndicesDict(
            self.PCpos, self.frameIndex, self.seq)

        self.segmentVals = sequence.semseg[frameIndex].to_numpy().flatten() - 1
        self.segmentColors = SEMSEG_COLORMAP[self.segmentVals]


class RenderData:
    def __init__(self, sequence, selectedRange):
        self.renderFrameList = [RenderFrame(
            sequence, ind) for ind in selectedRange]

        self.classNames = CLASS_NAMES

