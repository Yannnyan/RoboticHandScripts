import torch
import numpy as np
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

class HandDataset(Dataset):
    def __init__(self, paths):
        self.paths = paths

    def __len__(self):
        # returns the number of items in the dataset
        return len(self.paths.keys())

    def __getitem__(self, index):
        # gets an item at index
        imgs = []
        for j in range(2):
            img = plt.imread(self.paths['object_' + str(index)]['perspective_' + str(j)])
            imgs.append(img)
        cat = np.concatenate(imgs, axis=2)
        s = cat.shape
        cat = cat.reshape(s[2],s[0],s[1])
        tens = torch.from_numpy(cat)
        return tens

def CreateDatasets(paths):
    n = len(paths.keys())
    train_dataset = HandDataset(dict(list(paths.items())[:int(n * (9/10))])) # 90%
    test_dataset = HandDataset(dict(list(paths.items())[int(n * (9/10)):])) # 10 %
    return train_dataset,test_dataset

def CreateDataloder(dataset):
    return DataLoader(dataset, len(dataset),True)







