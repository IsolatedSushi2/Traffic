import numpy as np


def getCarPositions(sequence):
    positions = [list(pose["position"].values()) for pose in sequence.lidar.poses]
    positions = np.array(positions)
    return positions