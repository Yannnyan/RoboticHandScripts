from ..models.server_models_ConvexModel import convexModel
import numpy as np

def serializePrediction(prediction):
    parsed = np.array2string(prediction)
    return parsed


class ConvexController:
    def __init__(self) -> None:
        pass

    def HandleData(self, msg):
        prediction = convexModel.ModelReaction(msg)
        parsed = serializePrediction(prediction)
        return parsed


convexController = ConvexController()


