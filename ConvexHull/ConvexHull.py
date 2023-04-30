from stl import mesh
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import RotateByMatrix
from PointsLoader import Loader
from PointsChanger import Changer
from ConvertPoints import convertPoints

# stl_loaded = mesh.Mesh.from_file("./stls/KeyHeart.stl")
# reshaped_points = stl_loaded.vectors.reshape((int(stl_loaded.vectors.size/3), 3))
# reshaped_points = np.around(np.unique(reshaped_points, axis=0), 2)

points = Loader.LoadPointsFromCSV(r"C:\Users\Yan\Desktop\augment_input.csv",2,0)[0,:]
reshaped_points = convertPoints(points)
changer = Changer()
print(reshaped_points.shape)
#points = np.around(np.unique(reshaped_points),2)
print(reshaped_points)

hull = ConvexHull(reshaped_points)
vertices = changer.changePoints(hull.simplices, 10)
print("convex points", len(vertices))
fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")
# show the object
ax.plot(reshaped_points.T[0], reshaped_points.T[1], reshaped_points.T[2], "ko")

show_num = 10

# show convex hull
for ind, simplex in enumerate(vertices):
    if(ind < show_num):
        vector = np.array([reshaped_points[simplex,0], reshaped_points[simplex,1], reshaped_points[simplex,2]])
        vector = RotateByMatrix.rotate_vector(vector, 0, 0 ,0)
        ax.scatter(vector[0], vector[1], vector[2], marker='.',)
        # ax.plot(reshaped_points[simplex,0], reshaped_points[simplex, 1], reshaped_points[simplex, 2])
        # ax.plot(vector[0], vector[1], vector[2])

for i in ["x", "y", "z"]:
    eval("ax.set_{:s}label('{:s}')".format(i, i))
print("number of points in convex: ", show_num)




plt.show()


