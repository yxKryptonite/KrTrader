import torch
import torch.nn as nn
import torch.nn.functional as F
from models.base import BaseModel

class LSTMModel(BaseModel):
    def __init__(self, cfg):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size=cfg["input_size"], hidden_size=cfg["hidden_size"], num_layers=cfg["num_layers"])
        self.linear = nn.Linear(cfg["hidden_size"], cfg["output_size"])

    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.linear(x)
        return x