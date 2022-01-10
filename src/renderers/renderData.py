import src.extractors.pointCloudExtractor as PCE
import src.extractors.positionExtractor as PE


#  Stores all the renders for a single frame (from all the sensors)
class RenderData:

    def __init__(self, sequence, frameIndex):
        self.seq = sequence  # Load the data
        self.frameIndex = frameIndex

        self.PCpos = PCE.getOriginalPC(self.seq, self.frameIndex)
        self.carPositions = PE.getCarPositions(self.seq)
        self.cols, self.colIndices = PCE.getColorIndicesDict(
            self.PCpos, self.frameIndex, self.seq)
