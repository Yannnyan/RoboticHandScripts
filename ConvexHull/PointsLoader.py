
import pandas as pd
import numpy as np
import os


class Loader:
    def __init__(self) -> None:
        pass
    
    def CountRows(csvPath: str) -> int:
        n_lines = 0
        with open(csvPath,"r") as fp:
            for _ in fp:
                n_lines +=1
        return n_lines

    def LoadPointsFromCSV(csvPath: str, num_rows, skip_rows):
        """
        Loads an csv of the format:
        Output	w_p_x	w_p_y	w_p_z	w_r_x	w_r_y	w_r_z	point0_x, point0_y, point0_z, ... pointi_x...
        """
        dataframe = pd.read_csv(csvPath, nrows=num_rows, skiprows=skip_rows, delimiter=",")
        wrist_det_np = dataframe[['Output'	,'w_p_x',	'w_p_y',	'w_p_z',	'w_r_x'	,'w_r_y',	'w_r_z']].to_numpy()
        nparr = dataframe.drop(columns=['Output'	,'w_p_x',	'w_p_y',	'w_p_z',	'w_r_x'	,'w_r_y',	'w_r_z'])
        del nparr[nparr.columns[-1]]
        print(nparr.iloc[0,-1])
        nparr = nparr.to_numpy()
        return nparr[1:,:], wrist_det_np[1:,:]
    

class Saver:
    def __init__(self) -> None:
        pass
    
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


