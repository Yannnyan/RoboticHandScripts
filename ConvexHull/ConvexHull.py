from stl import mesh
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import RotateByMatrix

stl_loaded = mesh.Mesh.from_file("./Pot.stl")
reshaped_points = stl_loaded.vectors.reshape((int(stl_loaded.vectors.size/3), 3))
print(reshaped_points.shape)
#points = np.around(np.unique(reshaped_points),2)
#print(points.shape)
print(reshaped_points)
# print ("Points are", points.tolist())

hull = ConvexHull(np.array(reshaped_points))
fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")
# ax.plot(reshaped_points.T[0], reshaped_points.T[1], reshaped_points.T[2], "ko")

show_num = 2000

# show convex hull
for ind, simplex in enumerate(hull.simplices):
    if(ind < show_num):
        vector = np.array([reshaped_points[simplex,0], reshaped_points[simplex,1], reshaped_points[simplex,2]])
        vector = RotateByMatrix.rotate_vector(vector, 90, 0 ,0)
        ax.scatter(vector[0], vector[1], vector[2], marker='o')
        # ax.plot(reshaped_points[simplex,0], reshaped_points[simplex, 1], reshaped_points[simplex, 2])

# show points
# print(len(reshaped_points) / 50000)
# for ind, point in enumerate(reshaped_points):
#     if(ind % 1000000 == 0):
#         ax.plot(point[0], point[1], point[2])



# vector = np.array([1,0,0])
# vector1 = np.array([2,2,2])
# print(vector.shape, z_rotation_matrix.shape)
# print(vector1.shape, z_rotation_matrix.shape)
# vector_z = vector.dot(z_rotation_matrix)
# vector1_z = vector1.dot(z_rotation_matrix)
# print(vector_z)
# print(vector1_z)
# # print(vector.shape)
# # print(reshaped_points[0,0].shape)
# ax.plot(vector[0], vector[1], vector[2], marker='o', color="green")
# # ax.plot(vector1[0], vector1[1], vector1[2], marker='o', color="green")
# ax.plot(vector_z[0], vector_z[1], vector_z[2], marker='o', color="red")
# # ax.plot(vector1_z[0], vector1_z[1], vector1_z[2], marker='o', color="red")



for i in ["x", "y", "z"]:
    eval("ax.set_{:s}label('{:s}')".format(i, i))
print("number of points in convex: ", show_num)




plt.show()


