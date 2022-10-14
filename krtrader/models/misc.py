import torch
import torch.nn as nn
import torch.nn.functional as F
from models.base import BaseStrategy

class SignalStrategy(BaseStrategy):
    def __init__(self):
        super(SignalStrategy, self).__init__()
        self.buy = []
        self.sell = []

    def forward(self, now, prev):
        """momentum"""
        return now > prev

    def trade(self, result):
        self.buy.append(result)
        self.sell.append(not result)
        return self.buy, self.sell
