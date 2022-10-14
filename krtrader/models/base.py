import torch
import torch.nn as nn
import torch.nn.functional as F

class BaseModel(nn.Module):
    def __init__(self):
        super(BaseModel, self).__init__()
        pass

    def forward(self, x):
        pass

    def visualize(self):
        pass

    def save(self):
        pass

    def load(self, path):
        pass
