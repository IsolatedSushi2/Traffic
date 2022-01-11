import numpy as np

# Get the path positions
def getCarPositions(sequence):
    positions = [list(pose["position"].values()) for pose in sequence.lidar.poses]
    positions = np.array(positions)
    return positions