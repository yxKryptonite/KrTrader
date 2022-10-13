import torch
import torch.nn as nn
import torch.nn.functional as F

class BaseStrategy(nn.Module):
    def __init__(self):
        pass

    def forward(self, x):
        pass

    def visualize(self):
        pass

    def save(self):
        pass

    def load(self, path):
        pass
