from ..models.server_models_VoxelModel import voxelModel
import numpy as np


class VoxelController:
    def __init__(self) -> None:
        pass
    
    def HandleData(self, msg):
        prediction = voxelModel.ModelReaction(msg)
        string_prediction = np.array2string(prediction[0])
        return string_prediction
    

voxelController = VoxelController()



