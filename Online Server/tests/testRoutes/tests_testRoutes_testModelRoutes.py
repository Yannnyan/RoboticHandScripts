import unittest
from ..config.config import *
from ..Data.meshData import *
import requests
import re
import json



class RoutesTesting(unittest.TestCase):
    def setUp(self) -> None:
        self.ConvexURL = "http://localhost:8000/convexmodel"
        self.VoxelURL = "http://localhost:8000/voxelmodel"
        self.cup_coma_str = re.sub(r"\s+", ',', cup_str)
        self.points_dict = {"message": self.cup_coma_str, "wrist": ("1,2,3," * 2).removesuffix(",")}
        # self.str_save_points = json.dumps().encode()

    def testPostConvexModel(self):
        response = requests.post(self.ConvexURL, data=json.dumps(self.points_dict).encode())
        print("ConvexModel response: \n",response.text)

    def testPostVoxelModel(self):
        response = requests.post(self.VoxelURL, data=json.dumps(self.points_dict).encode())
        print("VoxelModel Response: \n", response.text)


unittest.main()


