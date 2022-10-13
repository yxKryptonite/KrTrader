import pandas as pd
import pandas_datareader as dr
import numpy as np
import torch
from models.lstm import LSTMStrategy
from data.dataset import StockDataset

# Load data
data = dr.data.get_data_yahoo('AAPL', start='2010-01-01', end='2020-01-01')
data = data['Close']
data = data.values # (T,)
dataset = StockDataset(data, 10)

# Load model

if __name__ == "__main__":
    strategy = LSTMStrategy()
    strategy.eval()
    x, y = dataset[0]
    x = torch.from_numpy(x).float()
    x = x.view(1, 10, 1)
    y_pred = strategy(x)
    print(y_pred)
    print(y)