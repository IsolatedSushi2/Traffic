import numpy as np


def getDefaultColors(colorDict):
    colorDict['Reflection'] = [0, 0, 0]
    colorDict['Smoke'] = [100, 100, 100]
    colorDict['Exhaust'] = [100, 100, 100]
    colorDict['Rain'] = [0, 85, 255]
    colorDict['Vegetation'] = [0, 85, 0]
    colorDict['Ground'] = [109, 65, 22]
    colorDict['Road'] = [126, 126, 126]
    colorDict['Lane Line'] = [255, 255, 0]
    colorDict['Stop Line'] = [255, 255, 0]
    colorDict['Other Marking'] = [255, 255, 0]
    colorDict['Sidewalk'] = [80, 80, 80]
    colorDict['Car'] = [170, 0, 0]
    colorDict['Pickup Truck'] = [0, 0, 170]
    colorDict['Medium Truck'] = [0, 0, 170]
    colorDict['Semi-truck'] = [0, 0, 120]
    colorDict['Motorcycle'] = [100, 0, 0]
    colorDict['Construction Vehicle'] = [170, 170, 0]
    colorDict['Other Vehicle'] = [40, 40, 40]
    colorDict['Emergency Vehicle'] = [112, 0, 168]
    colorDict['Scooter'] = [200, 200, 0]
    colorDict['Bicycle'] = [140, 0, 0]
    colorDict['Train'] = [112, 0, 168]
    colorDict['Tram'] = [80, 200, 160]
    colorDict['Pedestrian'] = [255, 0, 125]
    colorDict['Pedestrian & Object'] = [255, 0, 180]
    colorDict['Bird'] = [85, 255, 0]
    colorDict['Animal'] = [170, 170, 0]
    colorDict['Pylons'] = [126, 126, 126]
    colorDict['Road Barriers'] = [100, 0, 0]
    colorDict['Signs'] = [255, 170, 126]
    colorDict['Cones'] = [231, 154, 0]
    colorDict['Construction Signs'] = [255, 0, 0]
    colorDict['Construction Barriers'] = [255, 0, 0]
    colorDict['Building'] = [0, 0, 0]
    colorDict['Other Object'] = [40, 40, 40]

    return np.array(list(colorDict.values()))