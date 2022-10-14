import pandas as pd
import pandas_datareader as dr
import numpy as np
import torch
from models.lstm import LSTMStrategy
from data.dataset import StockDataset
import matplotlib.pyplot as plt

class BackTest():
    def __init__(self, cfg):
        # Load data
        data = dr.data.get_data_yahoo(cfg["name"], start=cfg["start"], end=cfg["end"]) # 2020-2022: inference
        data = data[cfg["features"]]
        data = data.values # (T,)
        self.data = torch.from_numpy(data).float().reshape(len(data), 1)
        # print(data.shape)
        # dataset = StockDataset(data, 365)

        # Load model
        self.strategy = LSTMStrategy()
        self.strategy.load_state_dict(torch.load(cfg["model_save_path"]))

    def run(self):
        self.strategy.eval()
        x, y = self.data[:-1, :], self.data[1:, :]
        print(x.shape , y.shape)
        y_pred = self.strategy(x)
        # print(y_pred)
        # print(y)
        plt.plot(y_pred.detach().numpy(), label='pred')
        plt.plot(y.detach().numpy(), label='true')
        plt.legend()
        plt.show()