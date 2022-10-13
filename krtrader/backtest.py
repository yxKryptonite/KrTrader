import pandas as pd
import pandas_datareader as dr
import numpy as np
import torch
from models.lstm import LSTMStrategy
from data.dataset import StockDataset
import matplotlib.pyplot as plt

# Load data
data = dr.data.get_data_yahoo('AAPL', start='2010-01-01', end='2022-10-12') # 2020-2022: inference
data = data['Close']
data = data.values # (T,)
data = torch.from_numpy(data).float().reshape(len(data), 1)
print(data.shape)
# dataset = StockDataset(data, 365)

# Load model
strategy = LSTMStrategy()
strategy.load_state_dict(torch.load('krtrader/ckpt/lstm.pth'))

if __name__ == "__main__":
    strategy.eval()
    x, y = data[:-1, :], data[1:, :]
    print(x.shape , y.shape)
    y_pred = strategy(x)
    # print(y_pred)
    # print(y)
    plt.plot(y_pred.detach().numpy(), label='pred')
    plt.plot(y.detach().numpy(), label='true')
    plt.legend()
    plt.show()