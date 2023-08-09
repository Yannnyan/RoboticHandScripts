import numpy as np
from ast import literal_eval


class AI_Model:
    
    def __init__(self) -> None:
        self.model_react_pipe = [self.parsePoints, self.preprocessPoints, self.reactToProcessed]

    def preprocessPoints(self, points) -> np.ndarray:
        pass

    def parsePoints(self, message) -> np.ndarray:
        # message = literal_eval(message.decode("utf-8"))
        
        arr = np.fromstring(str(message.message).strip("[]"), dtype=np.float64,sep=",")
        
        wrist_data = np.fromstring(str(message.wrist).strip("[]"), dtype=np.float64,sep=",")

        all_points = np.concatenate([wrist_data.reshape(-1,3), arr.reshape(-1,3)], axis=0)

        return all_points

    def reactToProcessed(self, processed_points) -> np.ndarray:
        pass

    def ModelReaction(self, msg):
        x = msg
        for fun in self.model_react_pipe:
            x = fun(x)
        return x
    