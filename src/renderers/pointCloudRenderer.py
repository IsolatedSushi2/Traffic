from src.renderers.baseRenderer import BaseRenderer
from src.constants import RENDER_POINTCLOUD_RATIO
import pandas as pd

# Calculates the renders for the PointClouds

class PointCloudRenderer(BaseRenderer):

    @staticmethod
    def getFrameRenders(pointCloud, slices):
        renderInterval = int(1.0 / RENDER_POINTCLOUD_RATIO)
        renderPC = pointCloud[:][slices][::renderInterval]
        print(len(renderPC))
        renderPC = pd.concat(renderPC)
        positions = renderPC.to_numpy()[:, :3] # Not interested in the heading

        return positions
        
    
    