import numpy as np
from colour import Color


def renderPC(renderData, camNameList, semseg, legendList):
    finalPos = renderData.PCpos
    pointAmount = finalPos.shape[0]

    finalSizes = np.ones(pointAmount) * 1
    finalColors = np.ones((pointAmount, 3))

    mask = legendList[renderData.segmentVals]

    if semseg:
        finalColors = renderData.segmentColors / 255
        finalSizes = finalSizes * 5
    else:
        for camName in camNameList:
            indices = renderData.colIndices[camName]
            colors = renderData.cols[camName]
            finalSizes[indices] = 4
            finalColors[indices] = colors

    finalSizes = finalSizes[mask]

    return finalPos[mask], finalColors[mask], finalSizes

def renderCarPath(renderData):
    finalPos = renderData.carPositions + np.array([0, 0, 4])

    red = Color("blue")   
    amount = finalPos.shape[0]
    colors = list(red.range_to(Color("red"), amount))

    finalColors = np.asarray([color.rgb for color in colors])

    currFrame = renderData.frameIndex
    currCarPos = finalPos[currFrame]
    carLine = np.vstack((currCarPos, currCarPos + np.array([0, 0, 2])))
    carColor = (0, 0, 0, 1)

    # Alpha channel
    finalColors = np.concatenate((finalColors, np.ones((amount, 1))), 1)

    return finalPos, finalColors, 10, carLine, carColor

def renderPCList(renderDataList, camNameList, semseg, legendList):
    dataList = [renderPC(renderData, camNameList, semseg, legendList) for renderData in renderDataList]

    positions, colors, sizes = zip(*dataList)

    concatPos = np.concatenate(tuple(positions))
    concatCol = np.concatenate(tuple(colors))
    concatSize = np.concatenate(tuple(sizes))

    return concatPos, concatCol, concatSize

