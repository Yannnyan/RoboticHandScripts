from .server_models_AIModel import AI_Model
import numpy as np
import sys
from ...config.config import *
from ...AI.VoxelModel.VoxelArchitecture import getModelOutput
sys.path.append(config_Scripts[keys_scripts.voxelScripts])

from pipeline import runPipelineShort
import torch


class VoxelModel(AI_Model):
    def __init__(self) -> None:
        super().__init__()
        self.model_react_pipe = [self.parsePoints, self.preprocessPoints, self.reactToProcessed]
    
    def preprocessPoints(self, points):
        voxel_indices = runPipelineShort(points[3:,:], config_Data[keys_data.pcdDir], config_Data[keys_data.voxelsDir])

        cube = np.zeros(config_VoxelModel[keys_voxel.cubeShape])

        for index in voxel_indices:
            cube[index] = 1

        return cube

    def parsePoints(self, msg):
        return super().parsePoints(msg)
    
    def reactToProcessed(self, processed_points):
        cube = processed_points
        cube = np.expand_dims(np.expand_dims(cube, axis=0),axis=0)
        torch_pred = getModelOutput(cube=cube)
        return torch.detach(torch_pred).numpy()
    
    def ModelReaction(self, msg):
        x = msg
        for fun in self.model_react_pipe:
            x = fun(x)
        return x
    

voxelModel = VoxelModel()

