import unittest
from ..config.config import *

from core.app.models.server_models_VoxelModel import voxelModel
import numpy as np
import json
import re
from ..Data.meshData import *
import torch
from core.app.models.server_models_Data import Data

class TestVoxelModel(unittest.TestCase):
    def setUp(self):
        self.cup_coma_str = re.sub(r"\s+", ',', cup_str)
        self.str_save_points = json.dumps({"message": ("1,2,3," * 100).removesuffix(","), "wrist": ("1,2,3," * 2).removesuffix(",")}).encode()
        self.cup_points = json.dumps({"message": self.cup_coma_str, "wrist": ("1,2,3," * 2).removesuffix(",")}).encode()
        points_dict = {"message": self.cup_coma_str, "wrist": ("1,2,3," * 2).removesuffix(",")}
        self.cup_data = Data(message=points_dict["message"], wrist=points_dict["wrist"])

    def test_preprocess_points(self):
        
        processed_points = voxelModel.preprocessPoints(voxelModel.parsePoints(self.cup_data))
        self.assertEqual(type(processed_points), np.ndarray)
        # print(processed_points.shape)
        self.assertEqual(processed_points.shape, (25,25,25))

    def test_parse_points(self):
        points = voxelModel.parsePoints(self.cup_data)
        self.assertEqual(type(points), np.ndarray)
        # self.assertEqual(points.shape, (102,3))
        self.assertTrue(np.array_equal(points[:2,:], np.array([[1,2,3],[1,2,3]])))

    def test_reactToProcessed(self):
        prediction = voxelModel.ModelReaction(self.cup_data)
        self.assertEqual(type(prediction), np.ndarray)
        self.assertEqual(prediction.shape, (1,54))
        # print(prediction)


unittest.main()


