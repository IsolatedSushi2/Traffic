from src.renderers.baseRenderer import BaseRenderer
from src.constants import RENDER_POINTCLOUD_RATIO
import pandas as pd
from pandaset import geometry
import numpy as np

# Calculates the renders for the PointClouds


class PointCloudRenderer(BaseRenderer):

    @staticmethod
    def getFrameRenders(sequence, slices, colorCameraList):
        # Pointcloud is stored in the lidar
        pointClouds = sequence.lidar
        indices = np.arange(len(pointClouds[:]))[slices]


        pointClouds = pointClouds[slices]

        for index in range(len(pointClouds)):
            frameIndex = indices[index]
            currPointCloud = 


        positions = renderPC.to_numpy()[:, :3]  # Only interested in positions

        rows, columns = positions.shape

        colors = (0, 0, 0, 0.5)
        if len(colorCameraList) == 0:
            colors = np.zeros((rows, 3))
            indicedColors, indices = PointCloudRenderer.getPCColours(sequence, positions, frameIndex)
            colors[indices] = indicedColors
        return positions, colors

    @staticmethod
    def getPCColours(sequence, positions, frameIndex):
        renderInterval = int(1.0 / RENDER_POINTCLOUD_RATIO)

        camera_name = "front_camera"
        chosen_camera = sequence.camera[camera_name]
        projected_points2d, camera_points_3d, inner_indices = geometry.projection(lidar_points=positions, 
                                                                          camera_data=chosen_camera[frameIndex],
                                                                          camera_pose=chosen_camera.poses[frameIndex],
                                                                          camera_intrinsics=chosen_camera.intrinsics,
                                                                          filter_outliers=True)


        # TODO, could do rounding, but then 1919.5 becomes 1920, fix that 
        #pixelIndices = np.round(projected_points2d)
        pixelIndices = np.array(projected_points2d, dtype=np.uint16)
        # Maybe that _npx works?
        rowIndices = pixelIndices[:, 0]
        columnIndices = pixelIndices[:, 1]

        currCameraFrame = chosen_camera.data[frameIndex]
        currCameraPixelValues = np.array(currCameraFrame)
        colors = currCameraPixelValues[columnIndices, rowIndices]

        return colors / 255, inner_indices
