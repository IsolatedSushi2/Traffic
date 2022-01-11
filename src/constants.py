import os
import seaborn as sns
import numpy as np
from src.colors import getDefaultColors

# Data paramaters
DEFAULT_DATA_SEQUENCE = os.path.join(os.getcwd(), "testData")
CHOSEN_SEQUENCE = "040"

# Legend parameters
CLASS_NAMES = ['Smoke', 'Exhaust', 'Rain', 'Reflection', 'Vegetation', 'Ground', 'Road', 'Lane Line', 'Stop Line', 'Other Marking', 'Sidewalk', 'Driveway', 'Car', 'Pickup Truck', 'Medium Truck', 'Semi-truck', 'Towed Object', 'Motorcycle', 'Construction Vehicle', 'Other Vehicle', 'Pedicab',
               'Emergency Vehicle', 'Bus', 'Mobility Device', 'Scooter', 'Bicycle', 'Train', 'Trolley', 'Tram ', 'Pedestrian', 'Pedestrian & Object', 'Bird', 'Animal', 'Pylons', 'Road Barriers', 'Signs', 'Cones', 'Construction Signs', 'Construction Barriers', 'Rolling Containers', 'Building', 'Other Object']
colorDict = dict.fromkeys(CLASS_NAMES, [0, 0, 0])
SEMSEG_COLORMAP = getDefaultColors(colorDict)

