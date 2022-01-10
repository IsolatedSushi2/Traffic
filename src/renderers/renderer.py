import numpy as np
from colour import Color


def renderPC(renderData, camNameList):
    finalPos = renderData.PCpos
    pointAmount = finalPos.shape[0]

    finalSizes = np.ones(pointAmount) * 1
    finalColors = np.ones((pointAmount, 3))

    for camName in camNameList:
        indices = renderData.colIndices[camName]
        colors = renderData.cols[camName]
        finalSizes[indices] = 4
        finalColors[indices] = colors

    return finalPos, finalColors, finalSizes

def renderCarPath(renderData):
    finalPos = renderData.carPositions

    red = Color("blue")   
    amount = finalPos.shape[0]
    colors = list(red.range_to(Color("red"), amount))

    finalColors = np.asarray([color.rgb for color in colors])

    currFrame = renderData.frameIndex
    currCarPos = finalPos[currFrame]
    carLine = np.vstack((currCarPos, currCarPos + np.array([0, 0, 2])))
    carColor = tuple(finalColors[currFrame])

    # Alpha channel
    finalColors = np.concatenate((finalColors, np.ones((amount, 1)) * 0.4), 1)

    return finalPos, finalColors, 5, carLine, carColor

def renderPCList(renderDataList, camNameList):
    dataList = [renderPC(renderData, camNameList) for renderData in renderDataList]

    positions, colors, sizes = zip(*dataList)

    concatPos = np.concatenate(tuple(positions))
    concatCol = np.concatenate(tuple(colors))
    concatSize = np.concatenate(tuple(sizes))

    return concatPos, concatCol, concatSize

