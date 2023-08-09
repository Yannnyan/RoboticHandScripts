import unittest
from ..config.config import *

from core.app.models.server_models_ConvexModel import convexModel
import numpy as np
import json
import re
from ..Data.meshData import *
import torch


class TestConvexModel(unittest.TestCase):
    def setUp(self):
        self.cup_coma_str = re.sub(r"\s+", ',', cup_str)
        self.str_save_points = json.dumps({"message": ("1,2,3," * 100).removesuffix(","), "wrist": ("1,2,3," * 2).removesuffix(",")}).encode()
        self.cup_points = json.dumps({"message": self.cup_coma_str, "wrist": ("1,2,3," * 2).removesuffix(",")}).encode()
    
    def test_preprocess_points(self):
        processed_points = convexModel.preprocessPoints(convexModel.parsePoints(self.cup_points))
        self.assertEqual(type(processed_points), np.ndarray)
        self.assertEqual(processed_points.shape, (2002,3))

    def test_parse_points(self):
        points = convexModel.parsePoints(self.str_save_points)
        self.assertEqual(type(points), np.ndarray)
        self.assertEqual(points.shape, (102,3))
        self.assertTrue(np.array_equal(points[:2,:], np.array([[1,2,3],[1,2,3]])))

        points2 = convexModel.parsePoints(self.cup_points)
        self.assertEqual(type(points2), np.ndarray)
        # self.assertEqual(points.shape, (102,3))
        self.assertTrue(np.array_equal(points2[:2,:], np.array([[1,2,3],[1,2,3]])))

    def test_reactToProcessed(self):
        prediction = convexModel.ModelReaction(self.cup_points)
        self.assertEqual(type(prediction), torch.Tensor)
        self.assertEqual(prediction.size(), torch.Size([54]))


unittest.main()


