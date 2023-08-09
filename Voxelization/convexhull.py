from scipy.spatial import ConvexHull
from make_pcd import read_pcd
import plotly.figure_factory as ff
import os
import numpy as np

for i in range(20):

    files = os.listdir('pcds')

    j = np.random.randint(0,len(files))

    filename = files[j]

    points = read_pcd('pcds/' + filename)

    print(len(points))

    print(points[0])

    hull = ConvexHull(points)

    print(hull.simplices)

    fig= ff.create_trisurf(x=hull.points[:,0], y=hull.points[:,1],z=hull.points[:,2], simplices= hull.simplices, title="convhull", aspectratio=dict(x=1,y=1,z=1))

    fig.show()


