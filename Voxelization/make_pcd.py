from pypcd import pypcd
import csv
import numpy as np
from make_complete_conv import complete_convex
from scipy.spatial import ConvexHull


mesh_wrist_path = r"C:\Users\Yan\Desktop\Robotic hand\data_logs\25.7.23\mesh_wrist.csv"


def getMeshPoints(path):
    mesh_points = []

    with open(path, 'r') as f:
        reader = csv.reader(f)
        first = True
        for row in reader:
            # first is headers
            if first:
                first = False
                continue
            convex = []
            try:
                # pass on all the columns in the ocnvex and add them
                # for col in row[7:]: # CHANGE ME PLS THIS NEEDS TO BE 7:
                for col in row[2:]:
                    convex.append(float(col))
                # put them as convex, target
            except Exception:
                pass
            # mesh_points.append([convex, int(float(row[0]))]) # CHANGE ME PLS THIS NEEDS TO BE 0
            mesh_points.append([convex, row[0]])

            
    return mesh_points

def seperateVectors(convexes):
    convexes_vectors = []
    for conv_targ in convexes:
        convex = conv_targ[0]
        conv_vecs = [(convex[i], convex[i+1], convex[i+2]) for i in range(0,len(convex), 3)]
        convexes_vectors.append([conv_vecs, conv_targ[1]])
    return convexes_vectors


def writePCD(convex, path):
    with open(path, 'w') as f:
        f.write("VERSION .5\n")
        f.write("FIELDS x y z\n")
        f.write("SIZE 4 4 4\n")
        f.write("TYPE F F F\n")
        f.write("COUNT 1 1 1\n")
        f.write("WIDTH " + str(len(convex)) + "\n")
        f.write("HEIGHT 1\n")
        f.write("POINTS " + str(len(convex)) + "\n")
        f.write("DATA ascii\n")
        for (x,y,z) in convex:
            f.write("" + str(x) + " " + str(y) + " " + str(z) + "\n")
        f.close()


def read_pcd(path):
    points = []
    with open(path,'r') as f:
        relevant_rows = f.readlines()[9:]
        for row in relevant_rows:
            points.append(np.fromstring(row,dtype=np.float64, sep=" "))
        f.close()    
    return points

def make_pcd_noConvex(mesh_wrist_path, pcd_dir):

    mesh_points = seperateVectors(getMeshPoints(mesh_wrist_path))

    print("Got ",len(mesh_points)," mesh points, each mesh contains: ", len(mesh_points[0]), " Vectors")

    i = 0
    for convex_target in mesh_points:
        i+=1
        # the filename will consist of the taraget number also
        writePCD(convex_target[0], pcd_dir + "/conv_target_" + str(convex_target[1]) + "_id_" + str(i) + ".pcd")

def make_one_pcd_withConvex(points, pcd_dir):
    complete_conv = complete_convex(ConvexHull(points))

    file_path = "/pcd_temporary.pcd"

    writePCD(complete_conv, pcd_dir + file_path)

    return file_path

def make_pcd_withConvex(mesh_wrist_path, pcd_dir):

    mesh_points = seperateVectors(getMeshPoints(mesh_wrist_path))

    print("Read all mesh points Got: ", len(mesh_points))

    # complete_mesh_points = [[complete_convex(ConvexHull(mesh_target[0])), mesh_target[1]] for mesh_target in mesh_points]
    n = 0
    i = 0
    for mesh_target in mesh_points:
        complete_convex_target = [complete_convex(ConvexHull(mesh_target[0])), mesh_target[1]]
        
        n+=1
        
        print(f"Completed {n} mesh convexes {n}'th mesh, contains: ", len(complete_convex_target[0]), " Vectors")

        i+=1

        # the filename will consist of the taraget number also
        writePCD(complete_convex_target[0], pcd_dir + "/conv_target_" + str(complete_convex_target[1]) + "_id_" + str(i) + ".pcd")

