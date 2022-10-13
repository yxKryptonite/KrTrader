import torch
import torch.nn as nn
import torch.nn.functional as F
from models.base import BaseStrategy

class LSTMStrategy(BaseStrategy):
    def __init__(self):
        super(LSTMStrategy, self).__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=50, num_layers=1)
        self.linear = nn.Linear(50, 1)

    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.linear(x)
        return x