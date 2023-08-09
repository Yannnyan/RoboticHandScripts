import torch
import numpy as np
from torch import nn
from ...config.config import config_ConvexModel

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        # self.flatten = nn.Flatten()
        self.hidden_layers = nn.Sequential(
            nn.Linear(2000*3 + 6, 2048),  # Increase the number of hidden units
            nn.ReLU(),
            nn.Linear(2048, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 54),
            nn.Sigmoid()
        )
        # self.hidden_layers.apply(init_weights)


    def forward(self, x):
        x = torch.flatten(x)
        x = self.hidden_layers(x)
        return x

# # Load
PATH = config_ConvexModel['convModelPath']
model = NeuralNetwork()
model.load_state_dict(torch.load(PATH))
model.eval()

def getModelOutput(convex: np.ndarray):
    """
    runs the model on sample convex array
    """
    return model(torch.from_numpy(convex).to(torch.float32))













