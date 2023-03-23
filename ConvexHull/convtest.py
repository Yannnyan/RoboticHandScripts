# -*- coding: utf-8 -*-
import numpy as np
import cdd as pcdd
import matplotlib.pyplot as plt

points= np.array([
    [0,0,0],
    [4,0,0],
    [4,4,0],
    [0,4,0],
    [0,0,4],
    [4,0,4],
    [4,4,4],
    [0,4,4]
])

# to get the convex hull with cdd, one has to prepend a column of ones
vertices = np.hstack((np.ones((8,1)), points))

# do the polyhedron
mat = pcdd.Matrix(vertices, linear=False, number_type="fraction") 
mat.rep_type = pcdd.RepType.GENERATOR
poly = pcdd.Polyhedron(mat)

# get the adjacent vertices of each vertex
adjacencies = [list(x) for x in poly.get_input_adjacency()]

# store the edges in a matrix (giving the indices of the points)
edges = [None]*(8-1)
for i,indices in enumerate(adjacencies[:-1]):
    indices = list(filter(lambda x: x>i, indices))
    l = len(indices)
    col1 = np.full((l, 1), i)
    indices = np.reshape(indices, (l, 1))
    edges[i] = np.hstack((col1, indices))
Edges = np.vstack(tuple(edges))

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

start = points[Edges[:,0]]
end = points[Edges[:,1]]

for i in range(12):
    ax.plot(
        [start[i,0], end[i,0]], 
        [start[i,1], end[i,1]], 
        [start[i,2], end[i,2]],
        "blue"
    )

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.set_xlim3d(-1,5)
ax.set_ylim3d(-1,5)
ax.set_zlim3d(-1,5)

plt.show()