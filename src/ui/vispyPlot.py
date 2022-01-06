from vispy import scene
from vispy.scene import visuals
from src.renderers.pointCloudRenderer import PointCloudRenderer
import numpy as np


class VispyPlot:
    def __init__(self, ui, data):
        self.ui = ui
        self.data = data
        self.pointCloud = self.data.load_lidar().lidar
        self.setupVispyWidget()
        self.addSceneVisuals()

        self.renderPoints()

    # Create the 3d vispy widget

    def setupVispyWidget(self):

        bgColor = (235 / 255, 235 / 255, 235 / 255)

        self.canvas = scene.SceneCanvas(
            keys='interactive', size=(600, 600), show=True, bgcolor=bgColor, vsync=False)
        self.ui.pointCloudPage.layout().addWidget(self.canvas.native)

        self.view = self.canvas.central_widget.add_view()

        self.view.camera = 'turntable'  # or try 'arcball'

    def addSceneVisuals(self):
        # For the points
        self.scatter = visuals.Markers()

        self.scatter.set_gl_state('opaque', depth_test=False)
        self.scatter.set_data(pos=None)

        self.view.add(self.scatter)

        # add a colored 3D axis for orientation
        self.axis = visuals.XYZAxis(parent=self.view.scene)

    def renderPoints(self):
        slices = slice(None, None, 1)
        positions = PointCloudRenderer.getFrameRenders(self.pointCloud, slices)
        self.scatter.set_data(pos=positions, edge_color=None, face_color=(
            0, 0, 0, 0.5), size=1, scaling=False)

        print("Rendered", len(positions), "points")
