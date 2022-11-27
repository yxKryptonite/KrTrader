import torch
import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary


class BaseModel(nn.Module):
    """This is a base class for all models"""
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

    def __str__(self):
        return f"Model Info --- {self.__class__.__name__}"

    def __repr__(self):
        return self.__str__()

    def sum(self, input_size):
        summary(self, input_size)
