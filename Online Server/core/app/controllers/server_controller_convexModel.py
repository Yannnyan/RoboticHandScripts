from ..models.server_models_ConvexModel import convexModel

class ConvexController:
    def __init__(self) -> None:
        pass
    
    def HandleData(self, msg):
        return convexModel.ModelReaction(msg)


convexController = ConvexController()


