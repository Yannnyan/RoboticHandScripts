
import os
import torch
from torch import nn

class HandBlock(nn.Module):

    def __init__(self, in_dim, out_dim, kernel_size= 5, stride=2) -> None:
        super().__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.kernel_size = kernel_size
        self.stride = stride
        self.conv = nn.Conv2d(self.in_dim, self.out_dim, kernel_size=(self.kernel_size,self.kernel_size))
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=(kernel_size, kernel_size), stride=stride)

    def forward(self, x):
        y = self.conv(x)
        z = self.relu(y)
        norm = nn.LayerNorm(z.shape[1:])
        d = norm(z)
        return self.pool(d)
    
class HandBrain(nn.Module):
    def __init__(self):
        super().__init__()

        self.cnn = nn.Sequential(
            # input (8, 447, 1002) 
            HandBlock(8,16),
            # -> (16, 223, 501)
            HandBlock(16,32),
            # -> (32, 111, 250)
            HandBlock(32,16),
            # -> (16, 55, 125)
            HandBlock(16,8)
            # -> (8, 27, 62)
        )
                

    def forward(self, x):
        # Forward pass through the CNN
        features = self.cnn(x)
        
        # print(features.size())
        # Flatten the feature maps for input to the linear layer
        flattened_features = torch.flatten(features, start_dim=1)
        # -> (13x13216 neurons)

        # Define a linear layer for classification
        linear = nn.Sequential(
            nn.Linear(flattened_features.size(1), 54),
            nn.Tanh()
            )
        return (linear(flattened_features) + 1) / 2

# def init_weights(m):
#     print(m)
#     if type(m) == nn.Conv2d:
#         m.weight.data.random_(0,1)
#         print(m.weight)

# brain = HandBrain()
# brain.apply(init_weights)

# inp = torch.rand((8,447,1002))
# print(inp)
# print(brain(inp))
# print(brain(inp).size())



