from .server_models_AIModel import AI_Model
from scipy.spatial import ConvexHull
from ...config.config import *
from ...AI.ConvexModel.ConvexArchitecture import getModelOutput

from PointsChanger import Changer
from make_pcd import make_one_pcd_withConvex, read_pcd
import numpy as np

changer = Changer()

class ConvexModel(AI_Model):
    def __init__(self) -> None:
        super().__init__()
        self.model_react_pipe = [self.parsePoints, self.preprocessPoints, self.reactToProcessed]
    
    def preprocessPoints(self, points):
        if config_ConvexModel[keys_convex.toConv]:
            convex = ConvexHull(points)
            
            return changer.changePoints(convex.points, config_ConvexModel[keys_convex.maxPoints])
        
        else:
            pcd_filename = make_one_pcd_withConvex(points[3:,:], config_Data[keys_data.pcdDir])

            processed_points = read_pcd(config_Data[keys_data.pcdDir] + pcd_filename)
            
            fixed_amount_points = changer.changePoints(np.array(processed_points), config_ConvexModel[keys_convex.maxPoints])

            wrist_and_mesh = np.concatenate([points[:2,:], fixed_amount_points])

            return wrist_and_mesh

    def parsePoints(self, msg):
        return super().parsePoints(msg)
    
    def reactToProcessed(self, processed_points):
        return getModelOutput(processed_points)
    
    def ModelReaction(self, msg):
        x = msg
        for fun in self.model_react_pipe:
            x = fun(x)
        return x


convexModel = ConvexModel()