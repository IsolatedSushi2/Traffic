from src.renderers.baseRenderer import BaseRenderer
from src.constants import RENDER_POINTCLOUD_RATIO
import pandas as pd
from pandaset import geometry
import numpy as np

# Calculates the renders for the PointClouds


class PointCloudRenderer(BaseRenderer):

    @staticmethod
    def getFrameRenders(sequence, slices, cameraList):
        # Pointcloud is stored in the lidar
        PCs = sequence.lidar[:]
        selIndices = np.arange(len(PCs))[slices]

        allCol = (0, 0, 0, 0.5)  # Default color

        allPos = pd.concat([PCs[i] for i in selIndices])
        allPos = allPos.to_numpy()[:, :3]  # Only interested in positions
        allSizes = np.repeat(1, allPos.shape[0])

        if len(cameraList) > 0:
            allCol = PointCloudRenderer.getAllColors(
                sequence, PCs, selIndices, cameraList)
            summedCols = np.sum(allCol, axis=1)
            mask = (summedCols < 3 - 0.01)
            allSizes[mask] = 5

        return allPos, allCol, allSizes

    @staticmethod
    def getAllColors(sequence, allPCs, indices, cameraList):

        allColors = np.empty((0, 3))

        for frameIndex in indices:
            currPC = allPCs[frameIndex]
            currPos = currPC.to_numpy()[:, :3]
            frameCameras = [sequence.camera[camName] for camName in cameraList]
            colors = PointCloudRenderer.projectSelectedCameras(
                currPos, frameCameras, frameIndex)
            allColors = np.concatenate((allColors, colors), axis=0)

        return allColors

    @staticmethod
    def projectSelectedCameras(currPC, cameraList, frameIndex):
        rows, columns = currPC.shape

        colors = np.ones((rows, 3))
        for camera in cameraList:
            indicedColors, indices = PointCloudRenderer.projectCamera(
                currPC, camera, frameIndex)
            colors[indices] = indicedColors

        return colors

    @staticmethod
    def projectCamera(positions, currCam, frameIndex):
        renderInterval = int(1.0 / RENDER_POINTCLOUD_RATIO)

        projected_points2d, camera_points_3d, inner_indices = geometry.projection(lidar_points=positions,
                                                                                  camera_data=currCam[frameIndex],
                                                                                  camera_pose=currCam.poses[frameIndex],
                                                                                  camera_intrinsics=currCam.intrinsics,
                                                                                  filter_outliers=True)

        # TODO, could do rounding, but then 1919.5 becomes 1920, fix that
        #pixelIndices = np.round(projected_points2d)
        pixelIndices = np.array(projected_points2d, dtype=np.uint16)
        # Maybe that _npx works?
        rowIndices = pixelIndices[:, 0]
        columnIndices = pixelIndices[:, 1]

        currCameraFrame = currCam.data[frameIndex]
        currCameraPixelValues = np.array(currCameraFrame)
        colors = currCameraPixelValues[columnIndices, rowIndices]

        return colors / 255, inner_indices
