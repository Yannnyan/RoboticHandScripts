import numpy as np
from PointsChanger import Changer
from PointsLoader import Loader
from scipy.spatial import ConvexHull
from PointsLoader import Saver
import os
import sys

sys.path.append(r"C:\Users\Yan\Desktop\Robotic hand\Scripts\Voxelization")
from make_pcd import read_pcd


MAXVERTICES = 2000

class FixPointAmountAlgo:

    def __init__(self, read_csv_or_pcd: bool, input_pcd_dir = "", input_csv_path = "", MAXVERTICES = MAXVERTICES) -> None:
        """
        read_csv_or_pcd: boolean, 1 to read csv file, 0 to read pcds from a directory
        """
        if not read_csv_or_pcd and not os.path.isdir(input_pcd_dir):
            print("Error: directory - " , input_pcd_dir, "Doesn't exist. \nTerminating...")
            exit(1)

        if read_csv_or_pcd and not os.path.isfile(input_csv_path):
            print("Error: CSV file - ", input_pcd_dir, "Doesn't exist. \nTerminating...")
            exit(1)

        self.read_csv_or_pcd = read_csv_or_pcd

        self.pcd_dir = input_pcd_dir

        self.csv_path = input_csv_path
        
        self.MAXVERTICES = MAXVERTICES

        
    def convertPoints(self, meshes):
        """
        Conv to standard all non nan values vectorical form
        This function takes all non nan values in the mesh 
        and reshapes it to a vector form, then appends it to to mesh points and returns 
        """
        mesh_points = []
        for mesh in meshes:
            points = mesh[~np.isnan(mesh)]
            reshaped_points = points.reshape(int(points.shape[0]/3), 3)
            # reshaped_points = np.around(np.unique(reshaped_points, axis=0), 2)
            mesh_points.append(reshaped_points)
        return mesh_points

    def convertAndChangeMesh(self, points):
        changer = Changer()

        points = points[~np.isnan(points)]

        reshaped_points = points.reshape(int(points.shape[0]/3), 3)

        # reshaped_points = np.around(np.unique(reshaped_points, axis=0), 2)

        hull = ConvexHull(reshaped_points)

        vertices = changer.changePoints(hull.points, self.MAXVERTICES)

        return vertices


    def runCSVInputAlgo(self, saveCSVPath: str):
        freadName = self.csv_path

        changer = Changer()
        
        saver = Saver()
        
        loader = Loader()
        
        last_index = 416 # 0
        num_rows = 10
        
        lines = 10000
        for i in range(lines):
            print(i)
            print(i / lines)
            try:
                meshes, wrist_details = loader.LoadPointsFromCSV(freadName,num_rows,last_index) # read hop_range rows from the input file
                last_index += num_rows # increment the last index position
                reshaped_meshes = self.convertPoints(meshes) # conv to standard all non nan values vectorical form
                convexes = []
                # change array shape to (n_records, MAXVERTICES)
                # for each mesh take convex and convert it to MAXVERTICES length
                for mesh in reshaped_meshes:
                    # print(mesh.shape)
                    try:
                        hull = ConvexHull(mesh)
                    except:
                        continue
                    vertices = changer.changePoints(hull.points, MAXVERTICES) 
                    convexes.append(vertices)
                convexes = np.array(convexes)
                saver.SavePointsToCSVRegular(saveCSVPath, convexes, wrist_details)
            except:
                continue
    
    def runPCDInputAlgo(self,saveCSVPath, pcd_input_dir_path, targetsCSVPath, noConv=True):
        changer = Changer()
        saver = Saver(targetsCSVPath=targetsCSVPath)

        lst = os.listdir(pcd_input_dir_path)

        for file in lst:
            points = read_pcd(pcd_input_dir_path + "\\" + file)

            conv_points = None

            if not noConv:
                conv = ConvexHull(points)

                conv_points = conv.points[conv.vertices]       
            else:
                conv_points = np.array(points)

            changed_points = changer.changePoints(np.array(conv_points), self.MAXVERTICES)

            target_id = file.split("_")[2]

            saver.WritePoints(saveCSVPath=saveCSVPath, points=changed_points, target_number=target_id)

            

    def runAlgo(self, saveCsvPath: str, targetsCSVPath: str = ""):
        if self.read_csv_or_pcd:
            self.runCSVInputAlgo(saveCSVPath=saveCsvPath)
        else:
            self.runPCDInputAlgo(saveCSVPath=saveCsvPath, pcd_input_dir_path=self.pcd_dir, targetsCSVPath=targetsCSVPath, noConv=True)

def runCSVAlgorithm(output_csv_path: str, input_csv_path: str, NVertices = MAXVERTICES):
    # path1 = r"C:\Users\Yan\Desktop\convexhull.csv"
    # path2 = r"test.csv"
    # path = r"C:\Users\Yan\Desktop\Robotic hand\data_logs\8.8.2023\pointsAlgo_noconv"

    # conv_path_csv = r"C:\Users\Yan\Desktop\Robotic hand\data_logs\8.8.2023\pointsAlgo_noconv\convexhull.csv"

    algo = FixPointAmountAlgo(read_csv_or_pcd=True, input_csv_path=input_csv_path,MAXVERTICES=NVertices)

    algo.runAlgo(saveCsvPath=output_csv_path)


def runPCDAlgorithm(output_csv_path,pcd_dir_path: str, targetsCSVPath: str = "", NVertices = MAXVERTICES):

    algo = FixPointAmountAlgo(read_csv_or_pcd=False, input_pcd_dir=pcd_dir_path, MAXVERTICES=NVertices)

    algo.runAlgo(saveCsvPath=output_csv_path, targetsCSVPath=targetsCSVPath)
