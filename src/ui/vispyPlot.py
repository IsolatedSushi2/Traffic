from vispy import scene
from vispy.scene import visuals
import src.renderers.renderer as renderer
import numpy as np
import time
from src.ui.customWidgets.cameraSelector import CameraSelector
from src.ui.customWidgets.legendSelector import LegendSelector


class VispyPlot:
    def __init__(self, ui, camNames, renderData):

        self.ui = ui
        self.renderData = renderData

        self.setupVispyWidget()
        self.addSceneVisuals()
        self.setupCameraSelectorButtons(camNames)
        self.setupLegend()
        self.renderCarPath()
        self.rendered = False

    # Connect the camera selection buttons
    def setupCameraSelectorButtons(self, camNames):
        self.cameraSelector = CameraSelector(camNames, self.canvas.native)
        self.cameraSelector.move(25, 20)

        self.cameraSelector.newCamListSignal.connect(self.forceUpdate)
        self.cameraSelector.renderPathSignal.connect(self.updatedPathButton)

    # Connect the legend widget
    def setupLegend(self):
        self.legend = LegendSelector(self.renderData, self.canvas.native)
        self.legend.clickedLabelSignal.connect(self.forceUpdate)
        self.legend.move(20, 280)
        self.legend.ui.segmentingCheckBox.clicked.connect(self.forceUpdate)
        self.legend.ui.renderListCheckBox.clicked.connect(self.forceUpdate)

    # Create the 3d vispy widget
    def setupVispyWidget(self):

        bgColor = (235 / 255, 235 / 255, 235 / 255)
        bgColor = (28 / 255, 31 / 255, 36 / 255)
        self.canvas = scene.SceneCanvas(keys='interactive', size=(
            600, 600), show=True, bgcolor=bgColor, vsync=False)
        self.ui.pointCloudPage.layout().addWidget(self.canvas.native)

        self.view = self.canvas.central_widget.add_view()

        self.view.camera = 'turntable'  # scene.cameras.FlyCamera()  # or try 'arcball'

        # add a colored 3D axis for orientation
        self.axis = visuals.XYZAxis(parent=self.view.scene)

    # Add the visuals for the pointcloud, path and position
    def addSceneVisuals(self):
        # For the points
        self.scatter = visuals.Markers()
        self.carPath = visuals.Line()
        self.carPosition = visuals.Line()

        self.scatter.set_gl_state('opaque', depth_test=True)
        self.carPath.set_gl_state('opaque', depth_test=True)
        self.carPosition.set_gl_state('opaque', depth_test=True)

        self.view.add(self.carPath)
        self.view.add(self.scatter)
        self.view.add(self.carPosition)

    # Just need to update the carpath (dont need to re-render the pointclouds)
    def updatedPathButton(self):
        self.renderCarPath()

    def forceUpdate(self):
        self.update(True)

    def renderCarPath(self):
        if not self.cameraSelector.renderPath:  # Clear the carpath and position
            self.carPath.set_data(np.empty((0, 3)), color=(0, 0, 0))
            self.carPosition.set_data(np.empty((0, 3)), color=(0, 0, 0))
            return

        # Get current Frame
        index = self.ui.frameSlider.value()
        currRenderData = self.renderData.renderFrameList[index]

        pos, colors, size, carPos, carColor = renderer.renderCarPath(
            currRenderData)

        self.carPath.set_data(pos, color=colors, width=size)

        self.carPosition.set_data(carPos, color=carColor, width=size)

    # Render the pointcloud
    def renderPoints(self):

        self.rendered = True
        index = self.ui.frameSlider.value()
        renderList = self.renderData.renderFrameList
        camNames = self.cameraSelector.selCamList
        legendList = self.legend.selectedClasses
        useSegment = self.legend.ui.segmentingCheckBox.isChecked()
        useList = self.legend.ui.renderListCheckBox.isChecked()

        if useList:  # Render all the frames
            pos, colors, sizes = renderer.renderPCList(
                renderList, camNames, useSegment, legendList)
        else:  # Render a single frame
            pos, colors, sizes = renderer.renderPC(
                renderList[index], camNames, useSegment, legendList)

        self.scatter.set_data(pos=pos, edge_color=None,
                              face_color=colors, size=sizes, scaling=False)

        print("Rendered", len(pos), "points")

    def update(self, force=False):

        self.renderCarPath()
        useList = self.legend.ui.renderListCheckBox.isChecked()

        if self.rendered and useList and not force:  # To prevent unnecessary rendering
            return

        self.renderPoints()
