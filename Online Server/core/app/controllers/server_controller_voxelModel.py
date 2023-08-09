from ..models.server_models_VoxelModel import voxelModel

class VoxelController:
    def __init__(self) -> None:
        pass
    
    def HandleData(self, msg):
        return voxelModel.ModelReaction(msg)
    

voxelController = VoxelController()



