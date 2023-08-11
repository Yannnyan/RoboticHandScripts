import torch
import numpy as np
from torch import nn
from core.config.config import *


class CNN_Block(nn.Module):
  def __init__(self, in_channels, out_channels, con_kenel_size, pool_kernel_size, pool_stride, conv_twice):
        super().__init__()
        self.conv_twice = conv_twice
        if conv_twice:
          self.conv1 = nn.Conv3d(in_channels, out_channels, kernel_size=con_kenel_size ,padding='same')
          self.act1 = nn.ReLU()
          self.conv2 = nn.Conv3d(out_channels, out_channels, kernel_size=con_kenel_size ,padding='same')
          self.act2 = nn.ReLU()
          self.max_pool = nn.MaxPool3d(stride=pool_stride, kernel_size=pool_kernel_size)  # Corrected kernel_size
        else:
          self.conv = nn.Conv3d(in_channels, out_channels, kernel_size=con_kenel_size ,padding='same')
          self.act = nn.LeakyReLU(negative_slope=0.01) # nn.ReLU()
          self.max_pool = nn.MaxPool3d(stride=pool_stride, kernel_size=pool_kernel_size)  # Corrected kernel_size
        self.initialize_weights()

  def forward(self, x):
        # print(x.shape)
        if self.conv_twice:
          x = self.conv1(x)
          x = self.act1(x)
          x = self.conv2(x)
          x = self.act2(x)
          x = self.max_pool(x)

        else:
          x = self.conv(x)
          x = self.act(x)
          x = self.max_pool(x)

        return x

  def initialize_weights(self):
        # Initialize the weights using a chosen initialization method
        # For example, let's use He initialization
        if self.conv_twice:
          torch.nn.init.normal_(self.conv1.weight,0, 6e-3)
          torch.nn.init.normal_(self.conv2.weight,0,6e-3)
          if self.conv1.bias is not None:
            torch.nn.init.constant_(self.conv1.bias, 0)
          if self.conv2.bias is not None:
            torch.nn.init.constant_(self.conv2.bias, 0)
        else:
          torch.nn.init.normal_(self.conv.weight,0,6e-3)
          if self.conv.bias is not None:
              torch.nn.init.constant_(self.conv.bias, 0)


class Head_Block(nn.Module):
  def __init__(self, dimensions):
    super().__init__()
    self.hidden_layers = nn.ModuleList()
    self.hidden_layers.append(nn.Flatten())
    for i in range(len(dimensions)-1):
      self.hidden_layers.append(nn.Linear(dimensions[i], dimensions[i+1]))
      if i != len(dimensions) - 1:
        self.hidden_layers.append(nn.LeakyReLU(negative_slope=0.01))
    self.hidden_layers.append(nn.Sigmoid())
    self.init_weights()

  def forward(self, x):
        # print(x.shape)
        for layer in self.hidden_layers:
          x = layer(x)
        return x

  def init_weights(self):
    for layer in self.hidden_layers:
      if isinstance(layer, nn.Linear):
          torch.nn.init.normal_(layer.weight,0,6e-3)
          layer.bias.data.fill_(0)

channel_0 = 16
channel_1 = 32
channel_2 = 64
channel_3 = 32
channel_4 = 16

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        # self.block1 = CNN_Block(1,channel_0,(5,5,5), (2,2,2), 2, conv_twice=False),
        # self.block2 = CNN_Block(channel_0,channel_1,(3,3,3), (2,2,2), 2, conv_twice=False),
        # self.block3 = CNN_Block(channel_1,channel_2,(3,3,3), (2,2,2), 1, conv_twice=False),
        # self.block4 = CNN_Block(channel_2,channel_3,(3,3,3), (2,2,2), 1, conv_twice=False),
        # self.block5 = CNN_Block(channel_3,channel_4,(3,3,3), (2,2,2), 1, conv_twice=False),

        # self.block6 = Head_Block([432,64,54])
        self.hidden_layers = nn.Sequential(
          CNN_Block(1,channel_0,(5,5,5), (2,2,2), 2, conv_twice=False),
          CNN_Block(channel_0,channel_1,(3,3,3), (2,2,2), 2, conv_twice=False),
          CNN_Block(channel_1,channel_2,(3,3,3), (2,2,2), 1, conv_twice=False),
          CNN_Block(channel_2,channel_3,(3,3,3), (2,2,2), 1, conv_twice=False),
          CNN_Block(channel_3,channel_4,(3,3,3), (2,2,2), 1, conv_twice=False),

          Head_Block([432,64,54])
        )

    def forward(self, x):
        # print(x.shape)
        # self.out1 = self.block1(x)
        # self.out2 = self.block2(self.out1)
        # self.out3 = self.block3(self.out2)
        # self.out4 = self.block4(self.out3)
        # self.out5 = self.block5(self.out4)
        # self.out6 = self.block6(self.out5)
        x = self.hidden_layers(x)
        return self.out6


# # Load
PATH = config_VoxelModel[keys_voxel.voxelModelPath]
model = CNN()
print(torch.load(PATH,map_location=torch.device('cpu')))
model.load_state_dict(torch.load(PATH,map_location=torch.device('cpu')))
model.eval()

def getModelOutput(cube: np.ndarray):
    """
    runs the model on sample convex array
    """
    return model(torch.from_numpy(cube).to(torch.float32))





