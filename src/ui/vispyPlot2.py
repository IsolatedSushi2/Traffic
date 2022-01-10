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

        # camNames = ['back_camera', 'front_camera', 'front_left_camera',
        #             'front_right_camera', 'left_camera', 'right_camera']
        # camNames = ['front_camera']

        self.setupCameraSelectorButtons(camNames)
        self.setupLegend()
        self.renderCarPath()
    # Create the 3d vispy widget

    def setupCameraSelectorButtons(self, camNames):
        self.cameraSelector = CameraSelector(camNames, self.canvas.native)
        self.cameraSelector.move(20, 20)

        self.cameraSelector.newCamListSignal.connect(self.updatedCamList)
        self.cameraSelector.renderPathSignal.connect(self.updatedPathButton)

    def setupLegend(self):
        #classNames = self.seq
        self.legend = LegendSelector(self.canvas.native)
        self.legend.move(20, 220)

    def setupVispyWidget(self):

        bgColor = (235 / 255, 235 / 255, 235 / 255)
        bgColor = (28 / 255, 31 / 255, 36 / 255)
        self.canvas = scene.SceneCanvas(keys='interactive', size=(
            600, 600), show=True, bgcolor=bgColor, vsync=False)
        self.ui.pointCloudPage.layout().addWidget(self.canvas.native)

        self.view = self.canvas.central_widget.add_view()

        self.view.camera = 'turntable' #scene.cameras.FlyCamera()  # or try 'arcball'

        # add a colored 3D axis for orientation
        self.axis = visuals.XYZAxis(parent=self.view.scene)

    def addSceneVisuals(self):
        # For the points
        self.scatter = visuals.Markers()
        self.carPath = visuals.Line()
        self.carPosition = visuals.Line()

        # TODO
        self.scatter.set_gl_state('opaque', depth_test=False)
        # self.scatter.set_data()

        self.view.add(self.carPath)
        self.view.add(self.scatter)
        self.view.add(self.carPosition)

    def updatedPathButton(self):
        self.renderCarPath()

    def updatedCamList(self):
        self.renderPoints()

    def renderCarPath(self):
        if not self.cameraSelector.renderPath:
            self.carPath.set_data(np.empty((0, 3)), color=(0, 0, 0))
            self.carPosition.set_data(np.empty((0, 3)), color=(0, 0, 0))
            return

        index = self.ui.frameSlider.value()
        currRenderData = self.renderData.renderFrameList[index]

        pos, colors, size, carPos, carColor = renderer.renderCarPath(currRenderData)
        self.carPath.set_data(pos, color=colors, width=size)
        
        self.carPosition.set_data(carPos, color=carColor, width=size)


    def renderPoints(self):

        index = self.ui.frameSlider.value()
        currRenderData = self.renderData.renderFrameList[index]
        camNames = self.cameraSelector.selCamList
        pos, colors, sizes = renderer.renderPC(currRenderData, camNames, True)
        self.scatter.set_data(pos=pos, edge_color=None,
                              face_color=colors, size=sizes, scaling=False)

        print("Rendered", len(pos), "points")

    def updateCamera(self):
        return # TODO

    def update(self):
        self.renderPoints()
        self.renderCarPath()
        self.updateCamera()
        