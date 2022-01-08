import numpy as np


def renderPC(renderData, camNameList):
    finalPos = renderData.PCpos
    pointAmount = finalPos.shape[0]

    finalSizes = np.ones(pointAmount) * 3
    finalColors = np.ones((pointAmount, 3))

    for camName in camNameList:
        indices = renderData.colIndices[camName]
        colors = renderData.cols[camName]
        finalSizes[indices] = 3
        finalColors[indices] = colors

    print(finalColors)

    return finalPos, finalColors, finalSizes


def renderPCList(renderDataList, camNameList):
    print(len(renderDataList))
    dataList = [renderPC(renderData, camNameList) for renderData in renderDataList]

    positions, colors, sizes = zip(*dataList)

    concatPos = np.concatenate(tuple(positions))
    concatCol = np.concatenate(tuple(colors))
    concatSize = np.concatenate(tuple(sizes))

    return concatPos, concatCol, concatSize

