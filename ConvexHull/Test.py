import unittest
from PointsLoader import Loader
from PointsChanger import Changer
import numpy as np

class TestCode(unittest.TestCase):
    
    def test_changer(self):
        points = Loader.LoadPointsFromCSV(r"C:\Users\Yan\Desktop\augment_input.csv",2,0)[0,:]
        points = points[~np.isnan(points)]
        reshaped_points = points.reshape(int(points.shape[0]/3), 3)
        reshaped_points = np.around(np.unique(reshaped_points, axis=0), 2)
        changer = Changer()
        max_p = 2000
        changed_points = changer.changePoints(reshaped_points, max_p)
        self.assertEqual(len(changed_points), max_p)
        max_p = int(len(reshaped_points) / 2)
        changed_points = changer.changePoints(reshaped_points, max_p)
        self.assertEqual(len(changed_points), max_p)
        


        




if __name__ == '__main__':
    unittest.main()








