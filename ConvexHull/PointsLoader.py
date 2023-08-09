
import pandas as pd
import numpy as np
import os
import sys
import threading as thread
import time
from datetime import datetime


class Loader:
    def __init__(self) -> None:
        self.isfirst = True
        self.headers = None
        
       

    def CountRows(csvPath: str) -> int:
        n_lines = 0
        with open(csvPath,"r") as fp:
            for _ in fp:
                n_lines +=1
        return n_lines

    def LoadPointsFromCSV(self, csvPath: str, num_rows, skip_rows):
        """
        Loads an csv of the format:
        Output	w_p_x	w_p_y	w_p_z	w_r_x	w_r_y	w_r_z	point0_x, point0_y, point0_z, ... pointi_x...
        """
        dataframe = None
        if self.isfirst:
            header_frame = pd.read_csv(csvPath, nrows=2,skiprows=0, delimiter=",")
            self.headers = list(header_frame.columns)
            self.isfirst = False
            # dataframe = pd.read_csv(csvPath, nrows=num_rows, skiprows=skip_rows, delimiter=",")
        dataframe = pd.read_csv(csvPath, nrows=num_rows, skiprows=skip_rows, delimiter=",",names=self.headers)
        wrist_det_np = dataframe[['Output'	,'w_p_x',	'w_p_y',	'w_p_z',	'w_r_x'	,'w_r_y',	'w_r_z']].to_numpy()
        nparr = dataframe.drop(columns=['Output'	,'w_p_x',	'w_p_y',	'w_p_z',	'w_r_x'	,'w_r_y',	'w_r_z'])
        del nparr[nparr.columns[-1]]
        # print(nparr.iloc[0,-1])
        nparr = nparr.to_numpy()
        return nparr[1:,:], wrist_det_np[1:,:]
    

class Saver:
    def __init__(self, targetsCSVPath) -> None:
        self.targetsCSVPath = targetsCSVPath
        self.targets = None
        self.counter = 0
        thread.Thread(target=self.log_count).start()


        if os.path.isfile(targetsCSVPath):
            self.targets = open(targetsCSVPath).readlines()
    
    def log_count(self):
        while(True):
            time.sleep(60)
            with open("log.txt","a") as log:
                log.write("Date: " + str(datetime.now()) +" Count is : " + str(self.counter))
 
    def SavePointsToCSV(self, csvPath: str, convexes: np.ndarray, wrist_details: np.ndarray):
        if not os.path.isfile(csvPath):
            # write headers
            pass
        header_names = ['Output'	,'w_p_x',	'w_p_y',	'w_p_z',	'w_r_x'	,'w_r_y',	'w_r_z']
        # header_names = []
        print(convexes.shape)
        for i in range(convexes.shape[1]):
            header_names.append("point" + str(i) + "_x")
            header_names.append("point" + str(i) + "_y")
            header_names.append("point" + str(i) + "_z")
        
        convexes = np.concatenate((wrist_details, convexes.reshape(convexes.shape[0], convexes.shape[1]*3)), axis=1)
        df = pd.DataFrame(convexes, columns=header_names)
        df.to_csv(csvPath,mode="a")
    
    def SavePointsToCSVRegular(self, csvPath:str, convexes: np.ndarray, wrist_details: np.ndarray):
        if not os.path.isfile(csvPath):
            # write headers
            pass
        np.set_printoptions(threshold=sys.maxsize)
        convexes = np.concatenate((wrist_details, convexes.reshape(convexes.shape[0], convexes.shape[1]*3)), axis=1)
        with open(csvPath,"a") as csv:
            np.savetxt(csv, convexes,delimiter=",")
        #     conv_str = np.array2string(convexes.T,separator=",",prefix="",suffix="")
        #     csv.write(conv_str)
        #     csv.write("\n")


    def WritePoints(self, saveCSVPath: str, points: np.ndarray, target_number): 
        self.counter +=1       
        with open(saveCSVPath, "a") as f:
            lst = self.targets[int(target_number)].split(",")[1:4]
            conc = target_number + "," + ",".join(lst) + ","
            f.write(conc)
            for idx,point in enumerate(points):
                if(idx == len(points) - 1):
                    out = "" + str(point[0]) + "," + str(point[1]) + "," + str(point[2])
                else:
                    out = "" + str(point[0]) + "," + str(point[1]) + "," + str(point[2]) + ","
                f.write(out)
                conc += out
            f.write("\n")
            # print(conc)


