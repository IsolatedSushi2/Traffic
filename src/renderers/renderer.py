import numpy as np


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


def renderPCList(renderDataList, camNameList):
    dataList = [renderPC(renderData, camNameList) for renderData in renderDataList]

    positions, colors, sizes = zip(*dataList)

    concatPos = np.concatenate(tuple(positions))
    concatCol = np.concatenate(tuple(colors))
    concatSize = np.concatenate(tuple(sizes))

    return concatPos, concatCol, concatSize

