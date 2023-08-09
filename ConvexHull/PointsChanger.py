
import random
import numpy as np

class Changer:
    
    def ifBigger(self, conv: np.ndarray, max_num: int):
        num_rows = conv.shape[0]
        folds = np.array_split(np.arange(num_rows), max_num)
        to_add = max_num
        conv_ind = np.array([])
        for fold in folds:
            if(to_add > 0):
                ind = np.random.choice(a=fold,size=1,
                                    replace=False)
                conv_ind = np.concatenate([conv_ind, ind])
                to_add -= 1
            else:   
                break
        return conv[np.int32(conv_ind),:]
    
    def ifSmaller(self, conv: np.ndarray, max_num: int) -> np.ndarray:
        num_rows = conv.shape[0]
        # num_points_per_line = np.ceil(max_num / num_rows)
        to_add = max_num - num_rows
        while(to_add > 0):
            rand_pointi = random.randint(0,num_rows - 1)
            before_pointi = rand_pointi - 1
            vec_dif = conv[rand_pointi] - conv[before_pointi]
            rand_ratio = random.random()
            new_point = conv[before_pointi] + vec_dif * rand_ratio
            conv = np.insert(conv,rand_pointi, new_point,axis=0)
            to_add -= 1
        return conv
    
    def changePoints(self, arr, max_num):
        """
        This function overrites the array to fit max_num vectors,
        i.e for small arrays it expands them, and for big arrays it degrades them to max_num vectors
        """
        if(len(arr) == max_num):
            return arr
        elif(len(arr) < max_num):
            return self.ifSmaller(arr, max_num)
        else:
            return self.ifBigger(arr, max_num)




