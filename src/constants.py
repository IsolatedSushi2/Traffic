import os
import seaborn as sns
import numpy as np
# Data paramaters
DEFAULT_DATA_SEQUENCE = os.path.join(os.getcwd(), "data")

# PointCloud parameters
RENDER_POINTCLOUD_RATIO = 0.1
SEMSEG_COLORMAP = np.array(sns.color_palette(None, 42))
