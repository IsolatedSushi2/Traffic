import pandaset
import os

# load dataset
dataset = pandaset.DataSet(os.path.join(os.getcwd(), 'data'))
seq002 = dataset["002"]
seq002.load()

print("avaliable cameras: ", seq002.camera.keys())

from pandaset import geometry

# generate projected points
seq_idx = 1
camera_name = "front_camera"
lidar = seq002.lidar
points3d_lidar_xyz = lidar.data[seq_idx].to_numpy()[:, :3]
choosen_camera = seq002.camera[camera_name]
projected_points2d, camera_points_3d, inner_indices = geometry.projection(lidar_points=points3d_lidar_xyz, 
                                                                          camera_data=choosen_camera[seq_idx],
                                                                          camera_pose=choosen_camera.poses[seq_idx],
                                                                          camera_intrinsics=choosen_camera.intrinsics,
                                                                          filter_outliers=True)
print("projection 2d-points inside image count:", projected_points2d.shape)

from matplotlib import pyplot as plt

# image before projection

ori_image = seq002.camera[camera_name][seq_idx]
print(ori_image)
plt.imshow(ori_image)
import matplotlib.cm as cm
import numpy as np

# image after projection
plt.imshow(ori_image)
distances = np.sqrt(np.sum(np.square(camera_points_3d), axis=-1))
colors = cm.jet(distances / np.max(distances))
plt.gca().scatter(projected_points2d[:, 0], projected_points2d[:, 1], color=colors, s=1)
plt.show()
