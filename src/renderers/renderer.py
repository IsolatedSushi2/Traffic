import numpy as np
from colour import Color


# Render the pointcloud for a single framae
def renderPC(renderFrame, selectedCameras, semseg, legendList):
    finalPos = renderFrame.PCpos
    pointAmount = finalPos.shape[0]

    # Get the  initial values
    finalSizes = np.ones(pointAmount) * 1
    finalColors = np.ones((pointAmount, 3))

    # Get the mask according to the selected legend
    mask = legendList[renderFrame.segmentVals]

    if semseg:  # Use the segmenting color ans size
        finalColors = renderFrame.segmentColors / 255
        finalSizes = finalSizes * 5
    else:  # Use the colors, with the selected cameras
        for camName in selectedCameras:
            indices = renderFrame.colIndices[camName]
            colors = renderFrame.cols[camName]
            finalSizes[indices] = 4
            finalColors[indices] = colors

    return finalPos[mask], finalColors[mask], finalSizes[mask]


def renderCarPath(renderFrame):
    # Heighten the path a bit for clarity
    finalPos = renderFrame.carPositions + np.array([0, 0, 4])

    # Get the gradient
    blue = Color("blue")
    amount = finalPos.shape[0]
    colors = list(blue.range_to(Color("red"), amount))
    finalColors = np.asarray([color.rgb for color in colors])

    # Also add a black line for the car
    currFrame = renderFrame.frameIndex
    currCarPos = finalPos[currFrame]
    carLine = np.vstack((currCarPos, currCarPos + np.array([0, 0, 2])))
    carColor = (0, 0, 0, 1)

    # Alpha channel
    finalColors = np.concatenate((finalColors, np.ones((amount, 1))), 1)

    return finalPos, finalColors, 10, carLine, carColor


def renderPCList(renderData, selectedCameras, semseg, legendList):
    # Get the renders for each separate frame
    dataList = [renderPC(renderFrame, selectedCameras, semseg, legendList)
                for renderFrame in renderData]

    positions, colors, sizes = zip(*dataList)

    # Join all the frames together
    concatPos = np.concatenate(tuple(positions))
    concatCol = np.concatenate(tuple(colors))
    concatSize = np.concatenate(tuple(sizes))

    return concatPos, concatCol, concatSize
