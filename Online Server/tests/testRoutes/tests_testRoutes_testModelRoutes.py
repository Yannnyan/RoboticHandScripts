import unittest
from ..config.config import *
from ..Data.meshData import *
import requests
import re
import json

class RoutesTesting(unittest.TestCase):
    def setUp(self) -> None:
        self.URL = "http://localhost:8000/convexmodel"
        self.cup_coma_str = re.sub(r"\s+", ',', cup_str)
        # self.str_save_points = json.dumps().encode()

    def testPostConvexModel(self):
        points_dict = {"message": self.cup_coma_str, "wrist": ("1,2,3," * 2).removesuffix(",")}
        response = requests.post(self.URL, data=json.dumps(points_dict).encode())
        print(response.text)

    def testPostVoxelModel(self):
        pass


unittest.main()


