from pandaset import geometry
import numpy as np

# Return the Lidar pointcloud
def getOriginalPC(sequence, frameIndex):
    PCdataFrame = sequence.lidar[frameIndex]
    PC = PCdataFrame.to_numpy()[:, :3]
    return PC

# Get the indices and colors per camera per frame (for easy rendering)
def getColorIndicesDict(pos, frameIndex, seq):

    colorDict = {}
    indiceDict = {}

    allCamNames = seq.camera.keys()

    for camName in allCamNames:
        currCam = seq.camera[camName]
        currColors, currIndices = projectCamera(pos, currCam, frameIndex)

        colorDict[camName] = currColors
        indiceDict[camName] = currIndices

    return colorDict, indiceDict


# Project the camera colors onto the pointcloud, and store the indices
def projectCamera(positions, currCam, frameIndex):
    projected_points2d, _, inner_indices = geometry.projection(lidar_points=positions,
                                                               camera_data=currCam[frameIndex],
                                                               camera_pose=currCam.poses[frameIndex],
                                                               camera_intrinsics=currCam.intrinsics,
                                                               filter_outliers=True)

    pixelIndices = np.array(projected_points2d, dtype=np.uint16)

    rowIndices = pixelIndices[:, 0]
    columnIndices = pixelIndices[:, 1]

    currCameraFrame = currCam.data[frameIndex]
    currCameraPixelValues = np.array(currCameraFrame)
    colors = currCameraPixelValues[columnIndices, rowIndices]

    return colors / 255, inner_indices
