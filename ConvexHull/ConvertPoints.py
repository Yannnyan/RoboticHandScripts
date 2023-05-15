import numpy as np
from PointsChanger import Changer
from PointsLoader import Loader
from scipy.spatial import ConvexHull
from PointsLoader import Saver
MAXVERTICES = 2000


def convertPoints(meshes):
    """
    Conv to standard all non nan values vectorical form
    This function takes all non nan values in the mesh 
    and reshapes it to a vector form, then appends it to to mesh points and returns 
    """
    mesh_points = []
    for mesh in meshes:
        points = mesh[~np.isnan(mesh)]
        reshaped_points = points.reshape(int(points.shape[0]/3), 3)
        reshaped_points = np.around(np.unique(reshaped_points, axis=0), 2)
        mesh_points.append(reshaped_points)
    return mesh_points

def convertAndChangeMesh(points):
    changer = Changer()
    points = points[~np.isnan(points)]
    reshaped_points = points.reshape(int(points.shape[0]/3), 3)
    reshaped_points = np.around(np.unique(reshaped_points, axis=0), 2)
    hull = ConvexHull(reshaped_points)
    vertices = changer.changePoints(hull.points, MAXVERTICES)
    return vertices


def mainFunc(saveCsvPath: str):
    freadName = r"C:\Users\Yan\Desktop\augment_input.csv";
    changer = Changer()
    saver = Saver()
    # n_lines = Loader.CountRows(freadName)
    last_index = 0
    hop_range = 2
    # while last_index < n_lines:
    meshes, wrist_details = Loader.LoadPointsFromCSV(freadName,hop_range,last_index) # read hop_range rows from the input file
    last_index += hop_range # increment the last index position
    reshaped_meshes = convertPoints(meshes) # conv to standard all non nan values vectorical form
    convexes = []
    # change array shape to (n_records, MAXVERTICES)
    # for each mesh take convex and convert it to MAXVERTICES length
    for mesh in reshaped_meshes:
        # print(mesh.shape)
        hull = ConvexHull(mesh)
        vertices = changer.changePoints(hull.points, MAXVERTICES) 
        convexes.append(vertices)
    convexes = np.array(convexes)
    saver.SavePointsToCSV(saveCsvPath, convexes, wrist_details)

if __name__ == "__main__":
    mainFunc(saveCsvPath=r"C:\Users\Yan\Desktop\convexhull.csv")
