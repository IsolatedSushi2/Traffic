from vispy import scene
from vispy.scene import visuals
import src.renderers.renderer as renderer
import numpy as np
import time
from src.ui.customWidgets.cameraSelector import CameraSelector
from src.ui.customWidgets.legendSelector import LegendSelector
from src.constants import RENDER_LIST

class VispyPlot:
    def __init__(self, ui, camNames, renderData):

        self.ui = ui
        self.renderData = renderData

        self.setupVispyWidget()
        self.addSceneVisuals()

        # camNames = ['back_camera', 'front_camera', 'front_left_camera',
        #             'front_right_camera', 'left_camera', 'right_camera']
        # camNames = ['front_camera']

        self.setupCameraSelectorButtons(camNames)
        self.setupLegend()
        self.renderCarPath()

        self.rendered = False

    # Create the 3d vispy widget

    def setupCameraSelectorButtons(self, camNames):
        self.cameraSelector = CameraSelector(camNames, self.canvas.native)
        self.cameraSelector.move(25, 20)

        self.cameraSelector.newCamListSignal.connect(self.updatedCamList)
        self.cameraSelector.renderPathSignal.connect(self.updatedPathButton)

    def setupLegend(self):
        self.legend = LegendSelector(self.renderData, self.canvas.native)
        self.legend.clickedLabelSignal.connect(self.updatedLegend)
        self.legend.move(20, 280)
        self.legend.ui.segmentingCheckBox.clicked.connect(self.onSegmentClicked)

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

    def addSceneVisuals(self):
        # For the points
        self.scatter = visuals.Markers()
        self.carPath = visuals.Line()
        self.carPosition = visuals.Line()

        # TODO
        self.scatter.set_gl_state('opaque', depth_test=True)
        self.carPath.set_gl_state('opaque', depth_test=True)
        # self.scatter.set_data()

        self.view.add(self.carPath)
        self.view.add(self.scatter)
        self.view.add(self.carPosition)

    def updatedPathButton(self):
        self.renderCarPath()

    def updatedCamList(self):
        self.update(True)

    def updatedLegend(self):
        self.update(True)

    def onSegmentClicked(self):
        self.update(True)

    def renderCarPath(self):
        if not self.cameraSelector.renderPath:
            self.carPath.set_data(np.empty((0, 3)), color=(0, 0, 0))
            self.carPosition.set_data(np.empty((0, 3)), color=(0, 0, 0))
            return

        index = self.ui.frameSlider.value()
        currRenderData = self.renderData.renderFrameList[index]

        pos, colors, size, carPos, carColor = renderer.renderCarPath(
            currRenderData)

        self.carPath.set_data(pos, color=colors, width=size)

        self.carPosition.set_data(carPos, color=carColor, width=size)

    def renderPoints(self):

        self.rendered = True
        index = self.ui.frameSlider.value()
        renderList = self.renderData.renderFrameList
        camNames = self.cameraSelector.selCamList
        legendList = self.legend.selectedClasses
        useSegment = self.legend.ui.segmentingCheckBox.isChecked()

        if RENDER_LIST:
            pos, colors, sizes = renderer.renderPCList(renderList, camNames, useSegment, legendList)
        else:
            pos, colors, sizes = renderer.renderPC(renderList[index], camNames, useSegment, legendList)
        self.scatter.set_data(pos=pos, edge_color=None,
                              face_color=colors, size=sizes, scaling=False)

        print("Rendered", len(pos), "points")

    def updateCamera(self):
        return  # TODO

    def update(self, force=False):

        self.renderCarPath()

        if self.rendered and RENDER_LIST and not force:
            return

        self.renderPoints()
        self.updateCamera()
