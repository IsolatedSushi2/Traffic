from vispy import scene
from vispy.scene import visuals
from src.renderers.pointCloudRenderer import PointCloudRenderer
import numpy as np
import time

class VispyPlot:
    def __init__(self, ui, data):
        self.ui = ui
        self.data = data.load()
        self.setupVispyWidget()
        self.addSceneVisuals()

        self.renderPoints()

    # Create the 3d vispy widget

    def setupVispyWidget(self):

        bgColor = (235 / 255, 235 / 255, 235 / 255)

        self.canvas = scene.SceneCanvas(keys='interactive', size=(
            600, 600), show=True, bgcolor='black', vsync=False)
        self.ui.pointCloudPage.layout().addWidget(self.canvas.native)

        self.view = self.canvas.central_widget.add_view()

        self.view.camera = 'turntable'  # or try 'arcball'

        # add a colored 3D axis for orientation
        self.axis = visuals.XYZAxis(parent=self.view.scene)

    def addSceneVisuals(self):
        # For the points
        self.scatter = visuals.Markers()

        self.scatter.set_gl_state('opaque', depth_test=False)
        self.scatter.set_data(pos=None)

        self.view.add(self.scatter)

    def renderPoints(self):
        slices = slice(None, None, 5)
        t1 = time.time()
        pos, col, sizes = PointCloudRenderer.getFrameRenders(self.data, slices, ["front_camera"])
        print("Getting render tool",time.time() - t1, "seconds")
        print(col)
        t2 =time.time()
        
        self.scatter.set_data(pos=pos, edge_color=None,
                              face_color=col, size=sizes, scaling=False)

        print("Rendered", len(pos), "points in ",time.time() - t2, "seconds")
