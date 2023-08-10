import unittest
from ..config.config import *

from core.app.models.server_models_VoxelModel import voxelModel
import numpy as np
import json
import re
from ..Data.meshData import *
import torch
from core.app.models.server_models_Data import Data


class TestData:
    def __init__(self) -> None:
        self.cup_coma_str = re.sub(r"\s+", ',', cup_str)
        self.cylinder_coma_str = re.sub(r"\s+", ',', cylinder_str)
        
        self.str_save_points = {"message": ("1,2,3," * 100).removesuffix(","), "wrist": ("1,2,3," * 2).removesuffix(",")}
        self.cup_points_dict = {"message": self.cup_coma_str, "wrist": ("1,2,3," * 2).removesuffix(",")}
        self.cylinder_points_dict = {"message": self.cylinder_coma_str, "wrist": ("1,2,3," * 2).removesuffix(",")}

        self.cup_data = Data(message=self.cup_points_dict["message"], wrist=self.cup_points_dict["wrist"])
        self.cylinder_data = Data(message=self.cylinder_points_dict["message"], wrist=self.cylinder_points_dict["wrist"])
        
        self.data = {"cup": self.cup_data, "cylinder": self.cylinder_data}


class TestAssertions:
    def __init__(self) -> None:
        pass
    
    def assertions_preprocess_points(self, data: Data, test_instance: unittest.TestCase):
        processed_points = voxelModel.preprocessPoints(voxelModel.parsePoints(data))
        test_instance.assertEqual(type(processed_points), np.ndarray, "type of processed points is: " + str(type(processed_points)))
        # print(processed_points.shape)
        test_instance.assertEqual(processed_points.shape, (25,25,25), "Shape of processed points is: " + str(processed_points.shape))

    def assertions_parse_points(self,data: Data, test_instance: unittest.TestCase):
            points = voxelModel.parsePoints(data)
            test_instance.assertEqual(type(points), np.ndarray, "Type of parsed points is: " + str(type(points)))
            # self.assertEqual(points.shape, (102,3))
            test_instance.assertTrue(np.array_equal(points[:2,:], np.array([[1,2,3],[1,2,3]])), "First 2 vectors are: " + str(points[:2,:]))

    def assertions_reactToProcessed(self, data, test_instance: unittest.TestCase):
        prediction = voxelModel.ModelReaction(data)
        test_instance.assertEqual(type(prediction), np.ndarray, "type of prediction is: " + str(type(prediction)))
        test_instance.assertEqual(prediction.shape, (1,54), "prediction shape is: " + str(prediction.shape))


class TestVoxelModel(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.testData = TestData()
        self.data = self.testData.data
        self.assertions = TestAssertions()

    def setUp(self):
        pass

    def runMethodOverData(self, fun, data):
        print("Testing " + fun.__name__)
        for key in data:
            print("Testing on Case: " + key)
            fun(data[key], self)

    def test_preprocess_points(self):
        self.runMethodOverData(self.assertions.assertions_preprocess_points, self.data)

    def test_parse_points(self):
        self.runMethodOverData(self.assertions.assertions_parse_points, self.data)

    def test_reactToProcessed(self):
        self.runMethodOverData(self.assertions.assertions_reactToProcessed, self.data)        


unittest.main()
