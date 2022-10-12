import pandas_datareader as dr
import pandas as pd
import csv
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

class StockDataset(Dataset):
    def __init__(self, data, window_size):
        self.data = data
        self.window_size = window_size

    def __len__(self):
        return len(self.data) - self.window_size

    def __getitem__(self, idx):
        x = torch.from_numpy(self.data[idx:idx + self.window_size, :-1]).float()
        y = torch.from_numpy(self.data[idx + self.window_size, [-1]]).float()
        return x, y