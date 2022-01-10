from vispy import scene
from vispy.scene import visuals
import src.renderers.renderer as renderer
import numpy as np
import time
from src.ui.customWidgets.cameraSelector import CameraSelector


class VispyPlot:
    def __init__(self, ui, camNames, renderDataList):

        self.ui = ui
        self.renderDataList = renderDataList

        self.setupVispyWidget()
        self.addSceneVisuals()

        self.selCamNames = []

        # camNames = ['back_camera', 'front_camera', 'front_left_camera',
        #             'front_right_camera', 'left_camera', 'right_camera']
        # camNames = ['front_camera']

        self.setupCameraSelectorButtons(camNames)
    # Create the 3d vispy widget

    def setupCameraSelectorButtons(self, camNames):
        self.cameraSelector = CameraSelector(camNames, self.canvas.native)
        self.cameraSelector.move(20, 20)

        self.cameraSelector.newCamListSignal.connect(self.updatedCamList)

    def setupVispyWidget(self):

        bgColor = (235 / 255, 235 / 255, 235 / 255)
        bgColor = (28 / 255, 31 / 255, 36 / 255)
        self.canvas = scene.SceneCanvas(keys='interactive', size=(
            600, 600), show=True, bgcolor=bgColor, vsync=False)
        self.ui.pointCloudPage.layout().addWidget(self.canvas.native)

        self.view = self.canvas.central_widget.add_view()

        self.view.camera = 'turntable'  # or try 'arcball'

        # add a colored 3D axis for orientation
        self.axis = visuals.XYZAxis(parent=self.view.scene)

    def addSceneVisuals(self):
        # For the points
        self.scatter = visuals.Markers()

        #self.scatter.set_gl_state('opaque', depth_test=False)
        # self.scatter.set_data()

        self.view.add(self.scatter)

    def updatedCamList(self, newCamList):
        print(newCamList)

        self.selCamNames = newCamList
        self.renderPoints()

    def renderPoints(self):

        index = self.ui.frameSlider.value()
        currRenderData = self.renderDataList[index]

        pos, colors, sizes = renderer.renderPC(currRenderData, self.selCamNames)
        self.scatter.set_data(pos=pos, edge_color=None,
                              face_color=colors, size=sizes, scaling=False)

        print("Rendered", len(pos), "points")
